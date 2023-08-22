from flask import Blueprint, render_template, redirect, url_for, request, flash
from . import db
from .models import User
from flask_login import login_user, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from .forms import RegistrationForm

# Create a blueprint named "auth" for authentication-related routes
auth = Blueprint("auth", __name__)

# Login Route
@auth.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get("email")
        password = request.form.get("password")

        # Query the database for a user with the provided email
        user = User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password, password):
                flash("Logged in!", category='success')
                login_user(user, remember=True)  # Log in the user and remember them
                return redirect(url_for('views.home'))  # Redirect to the home page
            else:
                flash('Password is incorrect.', category='error')
        else:
            flash('Email does not exist.', category='error')

    return render_template("login.html", user=current_user)  # Render the login template

# Sign Up Route
@auth.route("/sign-up", methods=['GET', 'POST'])
def sign_up():
    if current_user.is_authenticated:
        return redirect(url_for('views.home'))  # Redirect if the user is already authenticated
    form = RegistrationForm()

    if form.validate_on_submit():
        hashed_password = generate_password_hash((form.password.data), method='sha256')
        # Create a new user instance with hashed password and add to the database
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash('Your account has been created! You can now log in', 'success')
        return redirect(url_for('auth.login'))  # Redirect to the login page

    return render_template('signup.html', form=form, user=current_user)  # Render the sign-up template

# Logout Route
@auth.route("/logout")
@login_required  # Require the user to be logged in to access this route
def logout():
    logout_user()  # Log the user out
    return redirect(url_for("views.home"))  # Redirect to the home page
