"""This module initializes a Flask app and sets up a SQLite database."""

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager

# Initialize the SQLAlchemy database object
db = SQLAlchemy()
DB_NAME = "database.db"

def create_app():
    """Create and configure a Flask app instance."""
    # Initialize the Flask app
    app = Flask(__name__)

    # Configure app settings
    app.config['SECRET_KEY'] = "helloworld"  # Secret key for session security
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    # SQLite database URI
    db.init_app(app)  # Initialize the SQLAlchemy database with the app

    # Import and register blueprints (views and authentication)
    from .views import views
    from .auth import auth
    app.register_blueprint(views, url_prefix="/")
    app.register_blueprint(auth, url_prefix="/")

    # Import database models and create database tables
    from .models import User
    with app.app_context():
        db.create_all()  # Create database tables
        print("Created database!")

    # Initialize and configure the Flask LoginManager
    login_manager = LoginManager()
    login_manager.login_view = "auth.login"  # Set the login view
    login_manager.init_app(app)

    # Define a user loader function for the LoginManager
    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))

    return app

def create_database(app):
    """Create the database if it doesn't exist."""
    if not path.exists("website/" + DB_NAME):
        db.create_all(app=app)  # Create database tables
        print("Created database!")
