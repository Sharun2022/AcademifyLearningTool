"""
This module defines the database models used in the application.

It defines the User, Post, Comment,
and Like models used to store user information,
blog posts, comments, and post likes respectively in the database.
"""
# Import necessary modules and classes for
# database and user authentication
from . import db  # Import the database object
from flask_login import UserMixin
# Import UserMixin class for user authentication
from sqlalchemy.sql import func  # Import func for database functions


# Define the User Model
class User(db.Model, UserMixin):
    """User Model."""

    # Define columns for the User table
    id = db.Column(db.Integer,
                   primary_key=True)
    # Primary key for user identification
    email = db.Column(db.String(150), unique=True)
    # User's email, must be unique
    username = db.Column(db.String(150), unique=True)
    # User's username, must be unique
    password = db.Column(db.String(150))
    # User's hashed password
    image_file = db.Column(db.String(20),
                           nullable=False,
                           default='default.jpg')
    # User's profile image
    date_created = db.Column(db.DateTime(timezone=True),
                             default=func.now())
    # Date of user creation
    # Define relationships to other models (Post, Comment, Like)
    posts = db.relationship('Post', backref='user',
                            passive_deletes=True)
    # One-to-many relationship with posts
    comments = db.relationship('Comment',
                               backref='user',
                               passive_deletes=True)
    # One-to-many relationship with comments
    likes = db.relationship('Like',
                            backref='user',
                            passive_deletes=True)
    # One-to-many relationship with likes


# Define the Post Model
class Post(db.Model):
    """Post Model."""

    # Define columns for the Post table
    id = db.Column(db.Integer, primary_key=True)
    # Primary key for post identification
    title = db.Column(db.String(100), nullable=False)
    # Title of the post, must not be null
    text = db.Column(db.Text, nullable=False)
    # Content of the post, must not be null
    date_created = db.Column(db.DateTime(timezone=True),
                             default=func.now())
    # Date of post creation
    author = db.Column(db.Integer, db.ForeignKey('user.id',
                                                 ondelete="CASCADE"),
                       nullable=False)
    # Foreign key referencing user id
    # Define relationship to comments and likes
    comments = db.relationship('Comment',
                               backref='post',
                               passive_deletes=True)
    # One-to-many relationship with comments
    likes = db.relationship('Like',
                            backref='post', passive_deletes=True)
    # One-to-many relationship with likes


# Define the Comment Model
class Comment(db.Model):
    """Comment Model."""

    # Define columns for the Comment table
    id = db.Column(db.Integer, primary_key=True)
    # Primary key for comment identification
    text = db.Column(db.String(200), nullable=False)
    # Content of the comment, must not be null
    date_created = db.Column(db.DateTime(timezone=True), default=func.now())
    # Date of comment creation
    author = db.Column(db.Integer, db.ForeignKey('user.id',
                                                 ondelete="CASCADE"),
                       nullable=False)
    # Foreign key referencing user id
    post_id = db.Column(db.Integer, db.ForeignKey('post.id',
                                                  ondelete="CASCADE"),
                        nullable=False)
    # Foreign key referencing post id


# Define the Like Model
class Like(db.Model):
    """Like Model."""

    # Define columns for the Like table
    id = db.Column(db.Integer, primary_key=True)
    # Primary key for like identification
    date_created = db.Column(db.DateTime(timezone=True),
                             default=func.now())
    # Date of like creation
    author = db.Column(db.Integer, db.ForeignKey('user.id',
                                                 ondelete="CASCADE"),
                       nullable=False)
    # Foreign key referencing user id
    post_id = db.Column(db.Integer, db.ForeignKey('post.id',
                                                  ondelete="CASCADE"),
                        nullable=False)
    # Foreign key referencing post id
