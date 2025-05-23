# Accessisphere: E-Commerce Platform for Accessibility Products

Accessisphere is a full-stack database-driven e-commerce platform dedicated to making assistive and accessibility products easily available to those who need them. Built with a responsive frontend, secure Flask backend, and a MySQL relational database, the application provides a seamless shopping experience tailored to accessibility needs.

## Key features

* **User authentication & authorization** – secure sign-up, login, password hashing, and session management.
* **Product catalog** – browse, search, and filter by category, price, and accessibility tags.
* **Shopping cart & orders** – add/remove items, review cart, place orders, view order history.
* **Admin dashboard** – add, edit, or remove products; monitor orders; manage inventory.
* **Real-time interactions** – AJAX-based updates for cart and product filtering.
* **Relational database** – normalized MySQL schema with user, product, order, and inventory tables.

## 🗂️ Folder Structure

```plaintext
DBMS/
├── SQL/
│   └── script.sql             # SQL schema and seed data
└── frontend/
    ├── index.html             # Homepage
    ├── login.html             # Login screen
    ├── signup.html            # Signup screen
    ├── student_dashboard.html # Student dashboard (profile, courses)
    ├── admin_dashboard.html   # Admin interface (students, courses)
    └── styles.css             # Custom CSS styles
```


1. **Clone the Repository**

   ```bash
   git clone https://github.com/palak-b19/DBMS.git
   cd DBMS
   ```



2. **Configure Environment Variables**

   ```ini
   FLASK_APP=app.py
   FLASK_ENV=development
   SECRET_KEY=your_secret_key_here
   MYSQL_USER=your_mysql_username
   MYSQL_PASSWORD=your_mysql_password
   MYSQL_DB=accessisphere_db
   MYSQL_HOST=localhost
   MYSQL_PORT=3306
   ```


## Project Structure

```text
DBMS/                  # Repository root
├── app/               # Flask application package
│   ├── templates/     # Jinja2 templates
│   ├── static/        # CSS, JS, images
│   ├── models.py      # SQLAlchemy models
│   ├── routes.py      # View functions and endpoints
│   └── __init__.py
├── database/          # SQL scripts
│   ├── schema.sql     # Schema definitions
│   └── seeds.sql      # Sample data
├── migrations/        # Flask-Migrate files (if used)
├── .env               # Environment variables (not checked in)
├── requirements.txt   # Python dependencies
├── README.md          # Project documentation
└── app.py             # Entry point for Flask
```






