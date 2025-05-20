# Accessisphere: E-Commerce Platform for Accessibility Products

Accessisphere is a full-stack database-driven e-commerce platform dedicated to making assistive and accessibility products easily available to those who need them. Built with a responsive frontend, secure Flask backend, and a MySQL relational database, the application provides a seamless shopping experience tailored to accessibility needs.

## Key features

* **User authentication & authorization** – secure sign-up, login, password hashing, and session management.
* **Product catalog** – browse, search, and filter by category, price, and accessibility tags.
* **Shopping cart & orders** – add/remove items, review cart, place orders, view order history.
* **Admin dashboard** – add, edit, or remove products; monitor orders; manage inventory.
* **Real-time interactions** – AJAX-based updates for cart and product filtering.
* **Relational database** – normalized MySQL schema with user, product, order, and inventory tables.

## Tech Stack

* **Frontend**: HTML5, CSS3, JavaScript (vanilla)
* **Backend**: Python 3.x, Flask, Flask-Login, Flask-WTF
* **Database**: MySQL 8.x (or MariaDB)
* **Version Control**: Git & GitHub

## Getting Started

Follow these steps to get the project running on your local machine.

### Prerequisites

* **Python 3.7+**: Ensure Python is installed and available on your `PATH`.
* **MySQL**: Install MySQL server (8.x) or compatible (MariaDB).
* **Git**: For cloning the repository and version control.

### Installation & Setup

1. **Clone the Repository**

   ```bash
   git clone https://github.com/palak-b19/DBMS.git
   cd DBMS
   ```

2. **Create a Virtual Environment**

   ```bash
   python3 -m venv venv
   source venv/bin/activate    # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Configure Environment Variables**

   Create a `.env` file in the root directory with the following:

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

5. **Initialize the Database**

   * Create the database schema by running the SQL script:

     ```bash
     mysql -u your_mysql_username -p < database/schema.sql
     ```

   * (Optional) Seed with sample data:

     ```bash
     mysql -u your_mysql_username -p accessisphere_db < database/seeds.sql
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






