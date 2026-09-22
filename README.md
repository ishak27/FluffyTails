# 🐾 FluffyTails - Online Pet Adoption & Care Platform

**FluffyTails** is a full-featured, web-based pet adoption and shelter management platform designed to connect animal lovers with pets in need of a loving forever home.

It provides users with an intuitive interface to browse dogs and cats, learn about pet care, and manage adoptions through a unified cart system, while offering administrators robust tools to manage pet listings and user records.

---

## ✨ Features

* **Pet Catalog & Search**:
  * Browse dogs, puppies, cats, and kittens with filters for breed, age, and location distance
  * Detailed pet profile cards with high-quality photos and companion details
* **Adoption Cart & Checkout**:
  * Save favorite pets to an adoption cart
  * Review cart items and complete multi-pet adoption in a single click
  * Dynamic cart updates and empty-state messaging
* **Educational & Care Resources**:
  * **Adoption Checklist**: Step-by-step preparation guide for first-time adopters
  * **Dog Age Calculator**: Interactive conversion chart translating dog years to human years across breeds
  * **Pet FAQs & Behavior Guides**: Comprehensive advice on pet behavior, training, and smooth transition
* **User Authentication & Profiles**:
  * Secure user registration and login with encrypted passwords (Bcrypt)
  * Dedicated user profile page displaying account details and role status
* **Admin Portal**:
  * Admin dashboard for monitoring all active pet listings
  * Add new pets with custom images, breeds, age, distance, and categories (`dog`/`cat`)
  * Delete pet listings with automatic cascade cleanup of cart entries
  * Admin panel to inspect all registered users with contact details and role badges

---

## ⚙️ How It Works

1. **Browsing & Discovery**:
   * Visitors browse available pets across categories (Dogs & Puppies, Cats & Kittens).
   * Each pet profile highlights the animal's breed, age, location distance, and adoption readiness.

2. **Adoption Cart Workflow**:
   * Users create an account or log in to add pets to their adoption cart.
   * Users can review their selections, remove pets individually, or click **"Adopt All Pets"** to finalize the adoption.
   * Upon adoption, the database updates automatically, removing adopted pets from public view.

3. **Admin Pet & User Management**:
   * Administrators log in through the portal to access the **Admin Dashboard** and **User Directory**.
   * Admins can post newly rescued animals into the database or remove entries when adoptions are completed.

---

## 🛠️ Technologies Used

* **Python 3.12** – Core backend programming language
* **Flask** – Lightweight web application framework
* **Flask-SQLAlchemy & SQLite** – Relational database management and ORM modeling
* **Flask-Login** – Session handling, role-based authorization, and route protection
* **Flask-Bcrypt** – Secure password hashing
* **HTML5 & Jinja2** – Semantic templating, dynamic layout inheritance, and components
* **CSS3 & Bootstrap** – Modern purple/lavender styling, responsive grid layouts, and animations
* **FontAwesome** – Vector iconography
* **Git & GitHub** – Version control and collaboration

---

## 📁 Project Structure

```text
FluffyTails/
│
├── app.py                     
├── app.db                     
├── requirements.txt          
├── run.bat                    
├── run.ps1                    
│
├── static/                    
│   ├── ADS.jpg                
│   ├── image.png             
│   ├── image2.webp            
│   ├── img3.png              
│   └── index.css              
│
├── templates/                 
│   ├── base.html              
│   ├── index.html             
│   ├── dashboard.html         
│   ├── LogIn.html             
│   ├── SignUp.html            
│   ├── profile.html           
│   ├── cart.html              
│   ├── dogs.html              
│   ├── cats.html              
│   ├── checklist.html        
│   ├── admin_dashboard.html   
│   ├── admin.html             
│   ├── add_pet.html           
│   ├── aboutus.html           
│   ├── contactus.html         
│   └── ...
│
└── README.md                  
