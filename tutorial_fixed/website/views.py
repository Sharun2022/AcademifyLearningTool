"""
This module defines the routes and views for the web application.

It contains routes for various pages
like the home page, blog page, subjects page,
and specific subjects' year pages.
Additionally, it includes routes for handling
user profiles, posts, comments, likes,
and more. Each route corresponds to a
specific functionality of the web application.

Blueprint:
    The module initializes a Flask Blueprint named "views" that groups together
    routes and views related to the application's functionality.

Routes:
    - `/`: Home page displaying all posts.
    - `/home`: Alias for the home page.
    - `/blog`: Blog page displaying paginated posts.
    - `/subjects`: Page displaying subjects' information.
    - `/years_maths` to `/years_phy`:
    Routes for different subjects' year pages.

Each route provides functionality for
rendering corresponding HTML templates and
interacting with the application's database
to retrieve necessary data.

Note:
    The routes are designed to work
    with the `Flask-Login` extension, ensuring that
    users need to be logged in to access certain pages and functionality.

For detailed information on each route's
purpose and functionality, refer to the
inline comments within the code.
"""

import os
from pathlib import Path
from PIL import Image
import secrets
from flask import (
    Blueprint,
    render_template,
    request,
    flash,
    redirect,
    url_for,
    jsonify,
    abort
)
from flask_login import login_required, current_user
from .models import Post, User, Comment, Like
from .forms import RegistrationForm, UpdateAccountForm, PostForm
from . import db  # Import the database instance

# Create a Blueprint named "views" for different views
views = Blueprint("views", __name__)


# Defines a function called "not_blank" that takes a parameter called 'comment'
def not_blank(comment):
    """
    Check if a given comment is not blank.

    This function takes a comment as input
    and removes leading and trailing whitespace.
    It then checks if the resulting text is
    empty or not. If the text is not empty,
    the function returns the non-empty text; otherwise, it returns None.

    Args:
        comment (str): The input comment to be checked.

    Returns:
        str or None: The non-empty text if
        the comment is not blank, otherwise None.
    """
    valid = False  # Initialize valid as False
    while not valid:  # Start a loop until valid input is received
        text = comment.strip()  # Remove leading and trailing whitespace
        if text != "":  # Check if text is not empty
            return text  # Return the non-empty text
        else:  # If text is empty
            break  # Exit the loop


# Defines Route for the home page
@views.route("/")
@views.route("/home")
def home():
    """
    Render the home page.

    This function queries all posts from
    the database and renders the "home.html" template
    with the retrieved posts and the current user.

    Returns:
        rendered_template: The rendered HTML template.
    """
    posts = Post.query.all()
    return render_template("home.html", user=current_user, posts=posts)


# Defines Route for the blog page
@views.route("/blog")
@login_required
def blog():
    """
    Render the blog page.

    This function retrieves the requested
    page number from the URL, queries and paginates posts,
    and then renders the "blog.html" template with
    the paginated posts and the current user.

    Returns:
        rendered_template: The rendered HTML template.
    """
    page = request.args.get('page', 1, type=int)
    posts = Post.query.order_by(
        Post.date_created.desc()).paginate(page=page, per_page=4)
    return render_template("blog.html", user=current_user, posts=posts)


# Defines Route for the subjects page
@views.route("/subjects")
@login_required
def subjects():
    """
    Render the subjects page.

    This function renders the "subjects.html" template with the current user.

    Returns:
        rendered_template: The rendered HTML template.
    """
    return render_template("subjects.html", user=current_user)


# Defines Routes for various years in different subjects
@views.route("/years_maths")
@login_required
def years_maths():
    """
    Render the Mathematics year page.

    This function renders the
    "years_maths.html" template with the current user.

    Returns:
        rendered_template: The rendered HTML template.
    """
    return render_template("years_maths.html", user=current_user)

@views.route("/years_chem")
@login_required
def years_chem():
    """
    Render the Chemistry year page.

    This function renders the "years_chem.html" template with the current user.

    Returns:
        rendered_template: The rendered HTML template.
    """
    return render_template("years_chem.html", user=current_user)

@views.route("/years_eng")
@login_required
def years_eng():
    """
    Render the English year page.

    This function renders the "years_eng.html" template with the current user.

    Returns:
        rendered_template: The rendered HTML template.
    """
    return render_template("years_eng.html", user=current_user)

@views.route("/years_re")
@login_required
def years_re():
    """
    Render the Religious Education year page.

    This function renders the "years_re.html" template with the current user.

    Returns:
        rendered_template: The rendered HTML template.
    """
    return render_template("years_re.html", user=current_user)

@views.route("/years_dtg")
@login_required
def years_dtg():
    """
    Render the Digital Technologies year page.

    This function renders the "years_dtg.html" template with the current user.

    Returns:
        rendered_template: The rendered HTML template.
    """
    return render_template("years_dtg.html", user=current_user)


@views.route("/years_phy")
@login_required
def years_phy():
    """
    Render the Physics year page.

    This function renders the "years_phy.html" template with the current user.

    Returns:
        rendered_template: The rendered HTML template.
    """
    return render_template("years_phy.html", user=current_user)


#  Defines a route for all revision pages from Year 8 to 13 
#  Defines a route for all subject pages from DTG, PHY, CHEM, MAT, RE and ENG
@views.route("/year8_maths")
@login_required
def year8_maths():
    return render_template("year8_maths.html", user=current_user)

@views.route("/year8_chem")
@login_required
def year8_chem():
    return render_template("year8_chem.html", user=current_user)

@views.route("/year8_eng")
@login_required
def year8_eng():
    return render_template("year8_eng.html", user=current_user)

@views.route("/year8_re")
@login_required
def year8_re():
    return render_template("year8_re.html", user=current_user)\

@views.route("/year8_dtg")
@login_required
def year8_dtg():
    return render_template("year8_dtg.html", user=current_user)

@views.route("/year8_phy")
@login_required
def year8_phy():
    return render_template("year8_phy.html", user=current_user)

@views.route("/year9_maths")
@login_required
def year9_maths():
    return render_template("year9_maths.html", user=current_user)

@views.route("/year9_chem")
@login_required
def year9_chem():
    return render_template("year9_chem.html", user=current_user)

@views.route("/year9_eng")
@login_required
def year9_eng():
    return render_template("year9_eng.html", user=current_user)

@views.route("/year9_re")
@login_required
def year9_re():
    return render_template("year9_re.html", user=current_user)

@views.route("/year9_dtg")
@login_required
def year9_dtg():
    return render_template("year9_dtg.html", user=current_user)

@views.route("/year9_phy")
@login_required
def year9_phy():
    return render_template("year9_phy.html", user=current_user)

@views.route("/year10_maths")
@login_required
def year10_maths():
    return render_template("year10_maths.html", user=current_user)

@views.route("/year10_chem")
@login_required
def year10_chem():
    return render_template("year10_chem.html", user=current_user)

@views.route("/year10_eng")
@login_required
def year10_eng():
    return render_template("year10_eng.html", user=current_user)

@views.route("/year10_re")
@login_required
def year10_re():
    return render_template("year10_re.html", user=current_user)

@views.route("/year10_dtg")
@login_required
def year10_dtg():
    return render_template("year10_dtg.html", user=current_user)

@views.route("/year10_phy")
@login_required
def year10_phy():
    return render_template("year10_phy.html", user=current_user)

@views.route("/year11_maths")
@login_required
def year11_maths():
    return render_template("year11_maths.html", user=current_user)

@views.route("/year11_chem")
@login_required
def year11_chem():
    return render_template("year11_chem.html", user=current_user)

@views.route("/year11_eng")
@login_required
def year11_eng():
    return render_template("year11_eng.html", user=current_user)

@views.route("/year11_re")
@login_required
def year11_re():
    return render_template("year11_re.html", user=current_user)\
    
@views.route("/year11_dtg")
@login_required
def year11_dtg():
    return render_template("year11_dtg.html", user=current_user)

@views.route("/year11_phy")
@login_required
def year11_phy():
    return render_template("year11_phy.html", user=current_user)


@views.route("/year12_maths")
@login_required
def year12_maths():
    return render_template("year12_maths.html", user=current_user)

@views.route("/year12_chem")
@login_required
def year12_chem():
    return render_template("year12_chem.html", user=current_user)

@views.route("/year12_eng")
@login_required
def year12_eng():
    return render_template("year12_eng.html", user=current_user)

@views.route("/year12_re")
@login_required
def year12_re():
    return render_template("year12_re.html", user=current_user)

@views.route("/year12_dtg")
@login_required
def year12_dtg():
    return render_template("year12_dtg.html", user=current_user)

@views.route("/year12_phy")
@login_required
def year12_phy():
    return render_template("year12_phy.html", user=current_user)

@views.route("/year13_maths")
@login_required
def year13_maths():
    return render_template("year13_maths.html", user=current_user)

@views.route("/year13_chem")
@login_required
def year13_chem():
    return render_template("year13_chem.html", user=current_user)

@views.route("/year13_eng")
@login_required
def year13_eng():
    return render_template("year13_eng.html", user=current_user)

@views.route("/year13_re")
@login_required
def year13_re():
    return render_template("year13_re.html", user=current_user)

@views.route("/year13_dtg")
@login_required
def year13_dtg():
    return render_template("year13_dtg.html", user=current_user)

@views.route("/year13_phy")
@login_required
def year13_phy():
    return render_template("year13_phy.html", user=current_user)


# Route to create a new post
@views.route("/create-post", methods=['GET', 'POST'])
@login_required
def create_post():
    """
    Create a new post.

    This route handles both GET and POST requests. When a GET request is made, it renders
    the "create_post.html" template with the current user. When a POST request is made,
    it retrieves the data from the submitted form, validates it, and then adds a new post
    to the database with the current user as the author.

    Returns:
        rendered_template or redirection: Depending on the request method, it either renders
                                          the template or redirects to a different route.
    """
    form = PostForm()  # Create a form instance
    if form.validate_on_submit():  # If the form is submitted and valid
        title = form.title.data  # Get title data from the form
        text = form.text.data  # Get text data from the form
        post = Post(title=title, text=text, author=current_user.id)  # Create a new post object
        db.session.add(post)  # Add the post to the database session
        db.session.commit()  # Commit changes to the database
        flash('Post created!', category='success')  # Flash a success message
        return redirect(url_for('views.blog'))  # Redirect to the 'blog' route
    return render_template('create_post.html', form=form, user=current_user)  # Render the template with the form and user

# Route to delete a post
@views.route("/delete-post/<id>")
@login_required
def delete_post(id):
    """
    Delete a post.

    This route handles the deletion of a post identified by its ID. The ID is passed as a parameter
    in the URL. If the current user is the author of the post, the post is deleted from the database.
    If the post doesn't exist or the current user is not the author, appropriate flash messages are
    displayed.

    Args:
        id (int): The ID of the post to be deleted.

    Returns:
        redirection: Redirects to the "blog" route after the post is deleted or if an error occurs.
    """
    post = Post.query.filter_by(id=id).first()  # Get the post with the provided ID
    if not post:
        flash("Post does not exist.", category='error')  # Flash an error message if the post doesn't exist
    elif post.author != current_user.id:
        flash('You do not have permission to delete this post.', category='error')  # Flash an error message if the user doesn't have permission
    else:
        db.session.delete(post)  # Delete the post from the database session
        db.session.commit()  # Commit changes to the database
        flash('Post deleted.', category='success')  # Flash a success message
    return redirect(url_for('views.blog'))  # Redirect to the 'blog' route

# Route to display posts by a specific user
@views.route("/posts/<username>")
@login_required
def posts(username):
    """
    Display posts by a specific user.

    This route displays the posts authored by a specific user identified by their username.
    The username is passed as a parameter in the URL. If the user exists, their posts are
    retrieved from the database and displayed. If the user doesn't exist, an appropriate
    flash message is displayed.

    Args:
        username (str): The username of the user whose posts are to be displayed.

    Returns:
        render_template: Renders the "user_posts.html" template with the user's posts or an error message.
    """
    page = request.args.get('page', 1, type=int)  # Get the page number from the request arguments
    user = User.query.filter_by(username=username).first()  # Get the user with the provided username
    if not user:
        flash('No user with that username exists.', category='error')  # Flash an error message if the user doesn't exist
        return redirect(url_for('views.blog'))  # Redirect to the 'blog' route
    posts = Post.query.filter_by(user=user)\
        .order_by(Post.date_created.desc())\
            .paginate(page=page, per_page=5)  # Query posts by the user, order by date, and paginate the results
    return render_template("posts.html", user=current_user, posts=posts, username=username)  # Render the template with user, posts, and username


# Defines a route for creating a comment in a post
# Uses HTTP methods (POSTS) for user to submit a comment in this case
@views.route("/create-comment/<post_id>", methods=['POST'])
# Sets the route for the creation of a comment under the posts ID
@login_required  # Requires the user to be logged in
def create_comment(post_id):
    """
    Create a comment in a post.

    This route allows a logged-in user to submit a comment for a specific post.
    The comment text is submitted via a POST request. If the comment is valid,
    it is added to the database as a new comment associated with the post.

    Args:
        post_id (int): The ID of the post for which the comment is being created.

    Returns:
        redirect: Redirects the user back to the page displaying the post with the new comment.
    """
    comment = request.form.get('text')  # Defines comment
    # as the request to get the text the user has entered
    text = not_blank(comment)  # Define text as using the
    # as not blank in terms of the comment that the user is trying to post

    if not text:
        flash('Comment cannot be empty.', category='error')
    else:
        post = Post.query.filter_by(id=post_id).first()  # Get the post with the provided ID
        if post:
            comment = Comment(
                text=text, author=current_user.id, post_id=post_id)  # Create a new Comment object
            db.session.add(comment)  # Add the comment to the database session
            db.session.commit()  # Commit changes to the database
        else:
            flash('Post does not exist.', category='error')  # Flash an error message if the post doesn't exist

    return redirect(url_for('views.blog'))  # Redirect to the 'blog' route


# Route to delete a comment
@views.route("/delete-comment/<comment_id>")
@login_required
def delete_comment(comment_id):
    """
    Delete a comment.

    This route allows a logged-in user to delete a comment. Only the author of the
    comment or the author of the post containing the comment can delete it. If the
    user has the necessary permissions, the comment is removed from the database.

    Args:
        comment_id (int): The ID of the comment to be deleted.

    Returns:
        redirect: Redirects the user back to the relevant page after deleting the comment.
    """
    # Find the comment by its ID
    comment = Comment.query.filter_by(id=comment_id).first()

    # Check if the comment exists
    if not comment:
        flash('Comment does not exist.', category='error')
    # Check if the current user has permission to delete the comment
    elif current_user.id != comment.author and current_user.id != comment.post.author:
        flash('You do not have permission to delete this comment.', category='error')
    else:
        db.session.delete(comment)  # Delete the comment
        db.session.commit()

    return redirect(url_for('views.blog'))

# Route to like/unlike a post
@views.route("/like-post/<post_id>", methods=['POST'])
@login_required
def like(post_id):
    """
    Like or unlike a post.

    This route allows a logged-in user to like or unlike a post. The user can toggle
    their like status for a post. If the user has already liked the post, the like
    is removed. If the user has not liked the post, a new like is added to the database.

    Args:
        post_id (int): The ID of the post to be liked or unliked.

    Returns:
        jsonify: Returns a JSON response with the updated likes count and user's like status.
    """
    post = Post.query.filter_by(id=post_id).first()
    like = Like.query.filter_by(author=current_user.id, post_id=post_id).first()

    # Check if the post exists
    if not post:
        return jsonify({'error': 'Post does not exist.'}, 400)
    # Toggle the like status
    elif like:
        db.session.delete(like)
        db.session.commit()
    else:
        like = Like(author=current_user.id, post_id=post_id)
        db.session.add(like)
        db.session.commit()

    # Return JSON response with likes count and user's like status
    return jsonify({"likes": len(post.likes), "liked": current_user.id in map(lambda x: x.author, post.likes)})

# Function to save a user's profile picture
def save_picture(form_picture):
    """
    Save a user's profile picture.

    This function takes a user's uploaded profile picture and saves it on the server.
    It generates a unique filename using the `secrets` module and resizes the image
    to a smaller size before saving.

    Args:
        form_picture (FileStorage): The uploaded profile picture file.

    Returns:
        str: The filename of the saved profile picture.
    """
    path = Path("website/static/profile_pics")
    random_hex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(form_picture.filename)
    picture_fn = random_hex + f_ext
    picture_path = os.path.join(path, picture_fn)
    output_size = (125, 125)
    i = Image.open(form_picture)
    i.thumbnail(output_size)
    i.save(picture_path)

    return picture_fn

# Route to view and update user account details
@views.route("/account", methods=['GET', 'POST'])
@login_required
def account():
    """
    View and update user account details.

    This route allows logged-in users to view and update their account details.
    It handles both GET and POST requests. For GET requests, the user's current
    account information is displayed in a form. For POST requests, the user's
    account details are updated based on the submitted form data.

    Returns:
        rendered_template: If the request method is GET, renders the account.html
                          template with the user's account information and the form.
                          If the request method is POST and the form data is valid,
                          redirects the user to the account page with a success message.
                          If the form data is invalid, re-renders the account.html
                          template with the user's account information and the form,
                          along with error messages.
    """
    form = UpdateAccountForm()
    if form.validate_on_submit():
        if form.picture.data:
            picture_file = save_picture(form.picture.data)  # Save the uploaded picture
            current_user.image_file = picture_file  # Update user's profile picture
        current_user.username = form.username.data  # Update username
        current_user.email = form.email.data  # Update email
        db.session.commit()  # Commit changes to the database
        flash('Your account has been updated!', 'success')
        return redirect(url_for('views.account'))  # Redirect to the account page
    elif request.method == 'GET':
        form.username.data = current_user.username
        form.email.data = current_user.email
    image_file = url_for('static', filename='profile_pics/' + current_user.image_file)
    return render_template('account.html',user=current_user, image_file=image_file, form=form)

# Route to update a post
@views.route("/update-post/<id>", methods=['GET', 'POST'])
@login_required
def update_post(id):
    """
    Route to update a post.

    This route allows logged-in users to update their own posts.
    It handles both GET and POST requests. For GET requests, the
    form is pre-filled with the current post's information. For
    POST requests, the updated post data is processed and saved
    to the database.

    Args:
        id (int): The ID of the post to be updated.

    Returns:
        rendered_template: If the request method is GET, renders the update_post.html
                          template with the pre-filled form and the post's information.
                          If the request method is POST and the form data is valid,
                          redirects the user to the blog page with a success message.
                          If the form data is invalid, re-renders the update_post.html
                          template with the form, post's information, and error messages.
    """
    post = Post.query.filter_by(id=id).first()
    # Check if the current user is the author of the post
    if post.author != current_user.id:
        abort(403)  # Permission denied
    form = PostForm()
    if form.validate_on_submit():
        post.title = form.title.data  # Update post title
        post.text = form.text.data  # Update post text
        db.session.commit()  # Commit changes to the database
        flash('Your Post Has Been Updated!', category='success')
        page = request.args.get('page', 1, type=int)
        posts = Post.query.order_by(Post.date_created.desc()).paginate(page=page, per_page=4)
        return render_template("blog.html", user=current_user, posts=posts)

    elif request.method == 'GET':
        form.title.data = post.title
        form.text.data = post.text
        image_file = url_for('static', filename='profile_pics/' + current_user.image_file)
    return render_template('update_post.html', form=form, user=current_user, post=post, image_file=image_file)

