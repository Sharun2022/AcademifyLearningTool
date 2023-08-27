"""
Forms Module.

This module defines the WTForms classes used
for user registration, updating account details,
and creating posts
in the Flask application. It provides form
validation and data handling for user input.

Attributes:
    None

Classes:
    RegistrationForm: Form for user registration.
    UpdateAccountForm: Form for updating user account details.
    PostForm: Form for creating a new post.

"""
# Import necessary modules and classes for form creation
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from flask_login import current_user
from wtforms import StringField, PasswordField, SubmitField, TextAreaField
from wtforms.validators import (
    DataRequired,
    Length,
    Email,
    EqualTo,
    ValidationError
)
from .models import User  # Import the User model


# Define a class for user registration form
class RegistrationForm(FlaskForm):
    """Form for user registration."""

    # Define fields for the form
    username = StringField('Username', [DataRequired(), Length(6, 20)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', [DataRequired(), Length(8, 20)])
    confirm_password = PasswordField('Confirm Password', validators=[
        DataRequired(), EqualTo('password'), Length(min=8, max=20)
    ])
    submit = SubmitField('Sign Up')  # Submission button

    # Custom validation method to check username uniqueness
    def validate_username(self, username):
        """Validate Method to check same username."""
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError(
                'That username is already taken. '
                'Please choose a different one.'
                )

    # Custom validation method to check email uniqueness
    def validate_email(self, email):
        """Validate Method to check same email."""
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError(
                'That email is taken.'
                'Please choose a different one.')


# Define a class for updating user account form
class UpdateAccountForm(FlaskForm):
    """Form for updating user account details."""

    # Define fields for the form
    username = StringField('Username',
                           validators=[DataRequired(),
                                       Length(6, 20)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    picture = FileField('Update Profile Picture',
                        validators=[FileAllowed(['jpg', 'png'])])
    submit = SubmitField('Update')  # Submission button

    # Custom validation method to check username
    # uniqueness during account update
    def validate_username(self, username):
        """Validate method to check same username."""
        if username.data != current_user.username:
            user = User.query.filter_by(username=username.data).first()
            if user:
                raise ValidationError(
                    'That username is taken.'
                    'Please choose a different one.')

    # Custom validation method to check email uniqueness during account update
    def validate_email(self, email):
        """Validate method to check same email."""
        if email.data != current_user.email:
            user = User.query.filter_by(email=email.data).first()
            if user:
                raise ValidationError
            ('That email is taken. Please choose a different one.')


# Define a class for creating a new post form
class PostForm(FlaskForm):
    """Form for creating a new post."""

    # Define fields for the form
    title = StringField('Title', validators=[DataRequired()])
    text = TextAreaField('Text', validators=[DataRequired()])
    submit = SubmitField('Post')  # Submission button
