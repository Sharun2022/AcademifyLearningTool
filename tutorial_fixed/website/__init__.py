"""
Flask Application Package Initialization.

This module serves as the package initializer for the Flask application.
It sets up the main Flask app instance,
configures app-wide settings, initializes extensions, and registers blueprints.

Attributes:
    None

Functions:
    create_app(): Creates and configures the main Flask app instance.
    create_database(app): Creates the database if it doesn't exist.

"""

# Import necessary modules and packages
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

    # Set the URI for the SQLite database
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'

    # Initialize the SQLAlchemy database with the Flask app
    db.init_app(app)

    # Import and register blueprints for
    # different app sections (views and authentication)
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

    # Set the login view to redirect unauthorized users to the login page
    login_manager.login_view = "auth.login"
    login_manager.init_app(app)

    # Define a user loader function for the LoginManager
    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))

    return app


def create_database(app):
    """Create the database if it doesn't exist."""
    # Check if the database file doesn't exist
    if not path.exists("website/" + DB_NAME):
        # Create database tables based on defined models
        db.create_all(app=app)
        print("Created database!")
