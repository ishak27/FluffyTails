from flask import Flask, render_template, redirect, request, url_for, flash
from flask_sqlalchemy import SQLAlchemy
import os
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required, current_user
from flask_bcrypt import Bcrypt
from functools import wraps


basedir = os.path.abspath(os.path.dirname(__file__))

app=Flask(__name__)


app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + \
    os.path.join(basedir, "app.db").replace("\\", "/")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False


app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY", "fluffy_tails_secret_key_2025")




db = SQLAlchemy(app)


bcrypt = Bcrypt(app)
login_manager = LoginManager()


login_manager.init_app(app)


login_manager.login_view = "login"


class User(db.Model, UserMixin):


    __tablename__ = "user"


    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False, unique=True)
    password_hash = db.Column(db.String(100), nullable=False)
    mobile = db.Column(db.String(15), nullable=False)
    role = db.Column(db.String(50), nullable=False, default="user")
    

    def set_password(self, password):
        self.password_hash = bcrypt.generate_password_hash(password).decode("utf-8")


    def check_password(self, password):
        return bcrypt.check_password_hash(self.password_hash, password)


class Pet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    age = db.Column(db.String(50), nullable=False)
    breed = db.Column(db.String(100), nullable=False)
    distance = db.Column(db.String(50), nullable=False)
    image_url = db.Column(db.String(300), nullable=False)
    category = db.Column(db.String(10), nullable=False)  # New column (dog or cat)
    

class Cart(db.Model):  # Move Cart model above db.create_all()
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    pet_id = db.Column(db.Integer, db.ForeignKey('pet.id'), nullable=False)
    pet = db.relationship('Pet', backref=db.backref('cart_items', lazy=True))



@login_manager.user_loader
def load_user(user_id):
    return db.session.get(User, int(user_id))




with app.app_context():
    db.create_all()

    admin_email = "admin@gmail.com"
    if not User.query.filter_by(email=admin_email).first():  # Check specific email
        admin_user = User(name="Admin", email=admin_email, mobile="1234567890", role="admin")
        admin_user.set_password("admin123")  # Hash the password
        db.session.add(admin_user)
        db.session.commit()
        print(f"Admin user created: {admin_email} | Password: admin123")

@app.route("/home")
@login_required
def home():
    return  render_template("index.html")

@app.route("/")
def dashboard():
    return render_template("dashboard.html")

@app.route("/dashboard1")
@login_required
def dashboard1():
    return render_template("dashboard1.html")

@app.route('/contact')
def contact():
    return render_template("contactus.html")

@app.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")
        role = request.form.get("role")


        user = User.query.filter_by(email=email, role=role).first()
        if user and user.check_password(password):
            login_user(user)
            flash("Login successful!", "success")
            if user.role == "admin":
                return redirect(url_for("admin_dashboard"))
            else:
                return redirect(url_for("home"))
        else:
            flash("Invalid credentials!", "danger")

    return render_template("LogIn.html")

@app.route("/logout")
@login_required
def logout():
    logout_user()
    flash("Logged out successfully!", "info")
    return redirect(url_for("login"))


@app.route("/signup", methods=["GET", "POST"])
def signup():

    if request.method == "POST":
        name = request.form.get("name")
        email = request.form.get("email")
        password = request.form.get("password")
        confirm_password = request.form.get("confirm_password")
        mobile = request.form.get("mobile")


        if password != confirm_password:
            flash("Passwords do not match!", "danger")
            return redirect(url_for("signup"))


        if User.query.filter_by(email=email).first():
            flash("Email already exists!", "danger")
            return redirect(url_for("signup"))


        new_user = User(name=name, email=email, mobile=mobile)
        new_user.set_password(password)
        db.session.add(new_user)
        db.session.commit()


        flash("Registration successful! Please log in.", "success")
        return redirect(url_for("login"))

    return render_template("SignUp.html")


@app.route("/profile")
@login_required
def profile():
    return render_template("profile.html", user = current_user)

def admin_required(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if current_user.role != 'admin':
            flash("Access denied!", "danger")
            return redirect(url_for('dashboard'))
        return func(*args, **kwargs)
    return wrapper

@app.route('/add_pet', methods=['GET', 'POST'])
@login_required
@admin_required
def add_pet():
    if request.method == 'POST':
        name = request.form.get('name')
        age = request.form.get('age')
        breed = request.form.get('breed')
        distance = request.form.get('distance')
        image_url = request.form.get('image_url')
        category = request.form.get('category')  # Get category (dog or cat)

        new_pet = Pet(name=name, age=age, breed=breed, distance=distance, image_url=image_url, category=category)
        db.session.add(new_pet)
        db.session.commit()

        flash(f'{name} has been added successfully!', 'success')
        return redirect(url_for('admin_dashboard'))


        # Redirect based on category
        # if category == "dog":
        #     return redirect(url_for('dogs'))
        # else:
        #     return redirect(url_for('cats'))

    return render_template('add_pet.html')

@app.route('/admin/delete_pet/<int:pet_id>', methods=['POST'])
@login_required
@admin_required
def delete_pet(pet_id):
    pet = Pet.query.get_or_404(pet_id)
    # Remove associated cart items to prevent foreign key issues
    Cart.query.filter_by(pet_id=pet.id).delete()
    db.session.delete(pet)
    db.session.commit()

    flash(f'{pet.name} has been deleted!', 'success')
    return redirect(url_for('admin_dashboard'))

@app.route('/admin/dashboard')
@login_required
@admin_required
def admin_dashboard():
    pets = Pet.query.all()
    return render_template('admin_dashboard.html', pets=pets)

@app.route('/admin')
@login_required
@admin_required  # Apply the decorator here
def admin():
    users = User.query.all()
    return render_template("admin.html", users=users)



@app.route("/aboutus")
def aboutus():
    return render_template("aboutus.html")

@app.route("/aboutus2")
def aboutus2():
    return render_template("aboutus2.html")

@app.route("/adoptingpets")
def adoptingpets():
    return render_template("adoptingpets.html")

@app.route('/cats')
def cats():
    pets = Pet.query.all()
    return render_template('cats.html', pets=pets)

@app.route("/catKittenAdoption")
def catKittenAdoption():
    return render_template("catKittenAdoption.html")

@app.route("/dogPuppiesAdoption")
def dogPuppiesAdoption():
    return render_template("dogPuppiesAdoption.html")

@app.route('/dogs')
def dogs():
    pets = Pet.query.all()  # Fetch all pet records
    return render_template('dogs.html', pets=pets)

@app.route("/behaviordog")
def behaviordog():
    return render_template("behavior_dog.html")


@app.route("/behaviorcat")
def behaviorcat():
    return render_template("behavior_cat.html")


@app.route("/learnmore2.html")
def learnmore2():
    return render_template("learnmore2.html")

@app.route("/learnmore3.html")
def learnmore3():
    return render_template("learnmore3.html")

@app.route("/foundation")
def foundation():
    return render_template("Foundation.html")

@app.route("/checklist")
def checklist():
    return render_template("checklist.html")

@app.route("/welcome")
def welcome():
    return render_template("welcome.html")







@app.route('/add_to_cart/<int:pet_id>', methods=['POST'])
@login_required
def add_to_cart(pet_id):
    pet = Pet.query.get_or_404(pet_id)
    target_url = request.referrer or (url_for('dogs') if pet.category == 'dog' else url_for('cats'))

    # Check if pet is already in the cart
    existing_item = Cart.query.filter_by(user_id=current_user.id, pet_id=pet_id).first()
    if existing_item:
        flash('This pet is already in your cart!', 'warning')
        return redirect(target_url)

    new_cart_item = Cart(user_id=current_user.id, pet_id=pet.id)
    db.session.add(new_cart_item)
    db.session.commit()
    
    flash(f'{pet.name} added to your cart!', 'success')
    return redirect(target_url)

@app.route('/cart')
@login_required
def cart():
    cart_items = Cart.query.filter_by(user_id=current_user.id).all()
    return render_template('cart.html', cart_items=cart_items)

@app.route('/remove_from_cart/<int:cart_id>', methods=['POST'])
@login_required
def remove_from_cart(cart_id):
    item = Cart.query.get_or_404(cart_id)
    
    if item.user_id != current_user.id:
        flash("You can't remove this item!", 'danger')
        return redirect(url_for('cart'))

    db.session.delete(item)
    db.session.commit()
    flash('Item removed from cart.', 'success')
    return redirect(url_for('cart'))

@app.route('/adopt_all_pets', methods=['POST'])
@login_required
def adopt_all_pets():
    cart_items = Cart.query.filter_by(user_id=current_user.id).all()

    if not cart_items:
        flash("Your cart is empty!", "warning")
        return redirect(url_for('cart'))

    adopted_names = []
    for item in cart_items:
        if item.pet:
            adopted_names.append(item.pet.name)
            # Remove this pet from any other user's cart as well
            Cart.query.filter_by(pet_id=item.pet.id).delete()
            db.session.delete(item.pet)  # Remove pet from database
        else:
            db.session.delete(item)

    db.session.commit()

    flash(f"Congratulations! You have adopted: {', '.join(adopted_names)}", "success")
    return redirect(url_for('cart'))

if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=5000)
