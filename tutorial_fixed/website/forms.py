"""This module defines the forms used in the application."""

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
from .models import User


class RegistrationForm(FlaskForm):
    """Form for user registration."""

    username = StringField('Username',
                           validators=[DataRequired(), Length(min=6, max=20)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired(),
                                                     Length(min=8, max=20)])
    confirm_password = PasswordField(
                        'Confirm Password',
                        validators=[
                            DataRequired(),
                            EqualTo('password'),
                            Length(min=8, max=20)
                        ]
                    )
    submit = SubmitField('Sign Up')

    def validate_username(self, username):
        """Validate the uniqueness of the chosen username."""
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError
        ('That username is taken. Please choose a different one.')

    def validate_email(self, email):
        """Validate the uniqueness of the chosen email."""
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError
        ('That email is taken. Please choose a different one.')


class UpdateAccountForm(FlaskForm):
    """Form for updating user account details."""

    username = StringField('Username',
                           validators=[DataRequired(), Length(min=6, max=20)])
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    picture = FileField('Update Profile Picture',
                        validators=[FileAllowed(['jpg', 'png'])])
    submit = SubmitField('Update')

    def validate_username(self, username):
        """Validate the uniqueness of the chosen.

        username during account update.
        """
        if username.data != current_user.username:
            user = User.query.filter_by(username=username.data).first()
            if user:
                raise ValidationError(
                    'That username is taken. Please choose a different one.')

    def validate_email(self, email):
        """Validate the uniqueness of the.

        chosen email during account update.
        """
        if email.data != current_user.email:
            user = User.query.filter_by(email=email.data).first()
            if user:
                raise ValidationError(
                    'That email is taken. Please choose a different one.')


class PostForm(FlaskForm):
    """Form for creating a new post."""

    title = StringField('Title', validators=[DataRequired()])
    text = TextAreaField('Text', validators=[DataRequired()])
    submit = SubmitField('Create Post')

