# Flask Auth CRUD

A Flask-based web application that demonstrates **user authentication** and **CRUD (Create, Read, Update, Delete) operations** with a PostgreSQL database.

## Features
- 🔑 User registration & login with JWT authentication  
- 🔒 Password hashing using bcrypt for secure storage  
- 📦 CRUD operations on `users` and `items` tables  
- 🎨 HTML templates for login, adding, updating, filtering, and listing data  
- 📝 Logging of user activity and errors  

## Tech Stack
- **Backend**: Flask (Python)  
- **Database**: PostgreSQL  
- **Authentication**: JWT + bcrypt password hashing  
- **Frontend**: HTML templates with Flask integration  

## Database Schema
**Users Table**
- id (integer, primary key)  
- username (varchar)  
- email (varchar)  
- age (integer)  
- password (hashed varchar)  

**Items Table**
- id (integer, primary key)  
- name (varchar)  
- quantity (integer)  
- price (numeric)  

## ⚙️ Setup
```bash
# 1. Clone repo
git clone https://github.com/nilakay/flask-auth-crud.git
cd flask-auth-crud

# 2. Create a virtual environment & install dependencies
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# 3. Setup PostgreSQL (use db.yaml for credentials)

# 4. Run the app
flask run
