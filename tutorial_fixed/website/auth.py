"""
Authentication Blueprint.

This module defines authentication-related routes
and functionalities using a Flask Blueprint. It handles user
registration, login, logout, and user account management.

Attributes:
    None

Functions:
    login(): Authenticate the user and log them in.
    sign_up(): Register a new user.
    logout(): Log out the current user.

"""
# Import necessary modules and packages
from flask import Blueprint, render_template, redirect, url_for, request, flash
from . import db
from .models import User
from flask_login import login_user, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from .forms import RegistrationForm

# Create a blueprint named "auth" for authentication-related routes
auth = Blueprint("auth", __name__)


# Define the route for user login
@auth.route("/login", methods=['GET', 'POST'])
def login():
    """Authenticate the user and log them in."""
    if request.method == 'POST':
        email = request.form.get("email")
        password = request.form.get("password")

        # Query the database for the user based on the provided email
        user = User.query.filter_by(email=email).first()

        # Check if the user exists and
        # if the provided password matches the hashed password
        if user and check_password_hash(user.password, password):
            flash("Logged in!", category='success')
            # Log in the user and redirect to the home page
            login_user(user, remember=True)
            return redirect(url_for('views.home'))
        else:
            flash('Incorrect email or password.', category='error')

    # Render the login template
    return render_template("login.html", user=current_user)


# Define the route for user sign-up
@auth.route("/sign-up", methods=['GET', 'POST'])
def sign_up():
    """Register a new user."""
    if current_user.is_authenticated:
        return redirect(url_for('views.home'))

    # Create a registration form instance
    form = RegistrationForm()

    # Validate and process the submitted form data
    if form.validate_on_submit():
        password_data = form.password.data
        hashed_password = generate_password_hash(password_data,
                                                 method='sha256')

        # Create a new User object and add it to the database
        user = User(username=form.username.data,
                    email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()

        # Flash a success message and redirect to the login page
        flash('Your account has been created! You can now log in.', 'success')
        return redirect(url_for('auth.login'))

    # Render the sign-up template
    return render_template('signup.html', form=form, user=current_user)


# Define the route for user logout
@auth.route("/logout")
@login_required
def logout():
    """Log out the current user."""
    logout_user()
    return redirect(url_for("views.home"))
