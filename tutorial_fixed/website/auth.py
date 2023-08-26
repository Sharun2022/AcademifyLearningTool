"""This module defines authentication-related routes using a Blueprint."""

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
    """Authenticate the user and log them in."""
    if request.method == 'POST':
        email = request.form.get("email")
        password = request.form.get("password")

        user = User.query.filter_by(email=email).first()
        if user and check_password_hash(user.password, password):
            flash("Logged in!", category='success')
            login_user(user, remember=True)
            return redirect(url_for('views.home'))
        else:
            flash('Incorrect email or password.', category='error')

    return render_template("login.html", user=current_user)


# Sign Up Route
@auth.route("/sign-up", methods=['GET', 'POST'])
def sign_up():
    """Register a new user."""
    if current_user.is_authenticated:
        return redirect(url_for('views.home'))

    form = RegistrationForm()
    if form.validate_on_submit():
        password_data = form.password.data
        hashed_password = generate_password_hash(password_data,
                                                 method='sha256')
        user = User(username=form.username.data,
                    email=form.email.data,
                    password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash('Your account has been created! You can now log in.', 'success')
        return redirect(url_for('auth.login'))

    return render_template('signup.html', form=form, user=current_user)


# Logout Route
@auth.route("/logout")
@login_required
def logout():
    """Log out the current user."""
    logout_user()
    return redirect(url_for("views.home"))
