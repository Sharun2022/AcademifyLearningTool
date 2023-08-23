import os
from pathlib import Path
from PIL import Image
import secrets 
from flask import Blueprint, render_template, request, flash, redirect, url_for, jsonify, abort
from flask_login import login_required, current_user
from .models import Post, User, Comment, Like
from .forms import RegistrationForm, UpdateAccountForm, PostForm
from . import db

views = Blueprint("views", __name__)

# Defines function called not_blank that has a parameter called 'comment'
def not_blank(comment):
    valid = False # Defines valid as being a false input
    while not valid: # When not valid loop
        text = comment.strip() # Remove leading and trailing whitespace
        if text !="": #  Test if text to whitespace
            return text # Return text
        else: # If valid input
            break # Break loop

@views.route("/")
@views.route("/home")
def home():
    posts = Post.query.all()
    return render_template("home.html", user=current_user, posts=posts)

@views.route("/blog")
@login_required
def blog():
    page = request.args.get('page', 1, type=int)
    posts = Post.query.order_by(Post.date_created.desc()).paginate(page=page, per_page=4)
    return render_template("blog.html", user=current_user, posts=posts)

# Defines a route for the subjects page
@views.route("/subjects")
@login_required
def subjects():
    return render_template("subjects.html", user=current_user)

# Defines routes for various years in different subjects
@views.route("/years_maths")
@login_required
def years_maths():
    return render_template("years_maths.html", user=current_user)

@views.route("/years_chem")
@login_required
def years_chem():
    return render_template("years_chem.html", user=current_user)

@views.route("/years_eng")
@login_required
def years_eng():
    return render_template("years_eng.html", user=current_user)

@views.route("/years_re")
@login_required
def years_re():
    return render_template("years_re.html", user=current_user)

@views.route("/years_dtg")
@login_required
def years_dtg():
    return render_template("years_dtg.html", user=current_user)

@views.route("/years_phy")
@login_required
def years_phy():
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
    post = Post.query.filter_by(id=id).first()  # Get the post with the provided ID
    if not post:
        flash("Post does not exist.", category='error')  # Flash an error message if the post doesn't exist
    elif current_user.id != post.id:
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


# Defines a route for deleting a comment
@views.route("/delete-comment/<comment_id>")
@login_required
def delete_comment(comment_id):
    comment = Comment.query.filter_by(id=comment_id).first()

    # Check if the comment exists
    if not comment:
        flash('Comment does not exist.', category='error')
    # Check if the current user is the author of the comment or the post author
    elif current_user.id != comment.author and current_user.id != comment.post.author:
        flash('You do not have permission to delete this comment.', category='error')
    else:
        db.session.delete(comment)
        db.session.commit()

    return redirect(url_for('views.blog'))

# Defines a route for liking a post
@views.route("/like-post/<post_id>", methods=['POST'])
@login_required
def like(post_id):
    post = Post.query.filter_by(id=post_id).first()
    like = Like.query.filter_by(author=current_user.id, post_id=post_id).first()

    # Check if the post exists
    if not post:
        return jsonify({'error': 'Post does not exist.'}, 400)
    # Toggle like status
    elif like:
        db.session.delete(like)
        db.session.commit()
    else:
        like = Like(author=current_user.id, post_id=post_id)
        db.session.add(like)
        db.session.commit()

    # Return JSON response with likes count and user's like status
    return jsonify({"likes": len(post.likes), "liked": current_user.id in map(lambda x: x.author, post.likes)})

# Defines a function to save a user's profile picture
def save_picture(form_picture):
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

# Defines a route for the user's account page
@views.route("/account", methods=['GET', 'POST'])
@login_required
def account():
    form = UpdateAccountForm()
    if form.validate_on_submit():
        if form.picture.data:
            picture_file = save_picture(form.picture.data)
            current_user.image_file = picture_file
        current_user.username = form.username.data
        current_user.email = form.email.data
        db.session.commit()
        flash('Your account has been updated')
        return redirect(url_for('views.account'))
    elif request.method == 'GET':
        form.username.data = current_user.username
        form.email.data = current_user.email
    image_file = url_for('static', filename='profile_pics/' + current_user.image_file)
    return render_template('account.html', user=current_user, image_file=image_file, form=form)

# Defines a route for updating a post
@views.route("/update-post/<id>", methods=['GET', 'POST'])
@login_required
def update_post(id):
    post = Post.query.filter_by(id=id).first()
    # Check if the current user is the author of the post
    if post.author != current_user.id:
        abort(403)
    form = PostForm()
    if form.validate_on_submit():
        post.title = form.title.data
        post.text = form.text.data
        db.session.commit()
        flash('Your Post Has Been Updated!', category='success')
        page = request.args.get('page', 1, type=int)
        posts = Post.query.order_by(Post.date_created.desc()).paginate(page=page, per_page=4)
        return render_template("blog.html", user=current_user, posts=posts)

    elif request.method == 'GET':
        form.title.data = post.title
        form.text.data = post.text
        image_file = url_for('static', filename='profile_pics/' + current_user.image_file)
    return render_template('update_post.html', form=form, user=current_user, post=post, image_file=image_file)
