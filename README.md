# 🐾 FluffyTails - Pet Adoption System

A clean, responsive Flask web application for pet adoption, browsing dogs and cats, managing user adoptions via a shopping cart, and administering pets and user accounts.

---

## 🚀 Quick Start on Windows

### Option 1: One-Click Launch
- Double-click **`run.bat`** (or right-click `run.ps1` and select **Run with PowerShell**).
- This will automatically verify/activate the Windows virtual environment (`venv`), install dependencies if needed, and start the local web server.

### Option 2: Manual Setup (Terminal / PowerShell)

1. **Open PowerShell or Command Prompt** in the project directory:
   ```powershell
   cd "c:\Users\jitu3\OneDrive\Desktop\Project2"
   ```

2. **Activate the Windows Virtual Environment**:
   ```powershell
   .\venv\Scripts\activate
   ```

3. **Install Dependencies** (if not already installed):
   ```powershell
   pip install -r requirements.txt
   ```

4. **Run the Application**:
   ```powershell
   python app.py
   ```

5. Open your browser and navigate to:
   👉 **[http://127.0.0.1:5000](http://127.0.0.1:5000)**

---

## 🔑 Default Accounts

| Role | Email | Password | Access |
|---|---|---|---|
| **Admin** | `admin@gmail.com` | `admin123` | Full access: Add/delete pets, view registered users, admin dashboard |
| **User** | Register any account via `/signup` | User choice | Browse pets, add to cart, complete adoptions, view profile |

---

## 📁 Project Architecture

```
Project2/
│── app.py                 # Core Flask backend (routes, models, auth, carts)
│── app.db                 # SQLite database (Users, Pets, Cart)
│── requirements.txt       # Python package dependencies
│── run.bat                # Windows Batch one-click launcher
│── run.ps1                # Windows PowerShell launcher
│── README.md              # Project documentation
│── venv/                  # Windows Python 3.12 Virtual Environment
│── static/                # Static assets (images, banners, styling)
│   ├── ADS.jpg
│   ├── image.png          # FluffyTails logo
│   ├── image2.webp
│   └── index.css
└── templates/             # Jinja2 HTML Templates
    ├── base.html          # Global layout, navigation header & footer
    ├── index.html         # User landing page & pet highlights
    ├── dashboard.html     # Welcome guest dashboard
    ├── LogIn.html         # User / Admin login page
    ├── SignUp.html        # New user registration page
    ├── profile.html       # User profile details
    ├── cart.html          # Adoption cart & checkout
    ├── dogs.html          # Dog adoption & breed catalog
    ├── cats.html          # Cat adoption & breed catalog
    ├── checklist.html     # Adopter preparation checklist
    ├── admin_dashboard.html # Pet inventory management (add/delete)
    ├── admin.html         # User administration panel
    └── ...
```

---

## 🛠 Features & Improvements

- **Fully Windows-Native**:
  - Removed all macOS artifact folders (`__MACOSX`, `.DS_Store`, and macOS binaries).
  - Flattened nested folders so the app lives directly at root.
  - Normalized SQLite Windows path separators (`replace('\', '/')`).
- **Clean Authentication**:
  - Secure Bcrypt password hashing.
  - Role-based authorization (`admin` vs `user`) with protected routes.
- **Cart & Adoption Workflow**:
  - Users can browse dogs or cats, add pets to cart, view details, remove pets, or complete adoption with 1 click.
  - Cascade deletion protection prevents orphan foreign key entries when pets are deleted or adopted.
- **Admin Capabilities**:
  - Admin dashboard displaying all inventory with quick deletion.
  - Add pet form supporting breeds, distance, age, and photo URLs.
  - Admin panel to inspect all registered users and roles.
- **Responsive & Modern UI**:
  - Clean purple/lavender aesthetic.
  - Styled flash alerts for user feedback.
  - Navigation links dynamically adapt based on authentication state.
