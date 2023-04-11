from flask import Blueprint, render_template, redirect, url_for, send_file
blueprint = Blueprint('simple_pages', __name__)
from app.posts.models import Post

# Defining which route should render what HTML file
@blueprint.route('/')
def index():
    posts = Post.query.all()
    print("Index function called")  # Debug print
    print(posts)  # Debug print
    return render_template('simple_pages/index.html', posts=posts)

@blueprint.route('/contact')
def contact():
    return render_template('simple_pages/contact.html')