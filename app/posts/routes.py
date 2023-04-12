from flask import Blueprint, render_template, request, redirect, url_for
from datetime import datetime
from .models import Post, Author
from app.extensions.database import db

blueprint = Blueprint('posts', __name__)


# Documenting all my articles
#blog_posts_dictionary = {
 #       'article1': 'The foundation of happiness',
  #      'article2': 'Life means balance',
   #     'article3': 'The power of words',
    #    'article4': 'Upcoming article',
    #}

# Routes related to blog posts
@blueprint.route('/blog')
def blog_posts():
    all_posts = Post.query.all()
    return render_template('Blog/index.html', posts=all_posts)

@blueprint.route('/post-page')
def postpage():
    return render_template('Blog/post-page.html')

@blueprint.route('/blog/<slug>')
def blog_post(slug):
    post = Post.query.filter_by(slug=slug).first_or_404()
    return render_template('Blog/blog_posts.html', post=post)

# Creating the route where users can submit their own posts
@blueprint.route('/publish-posts', methods=['GET', 'POST'])
def publish_post():
    if request.method == 'POST':
        name = request.form['name']
        slug = request.form['name']
        date_str = request.form['date']
        author_name = request.form['author_name']
        content = request.form['content']
        date = datetime.strptime(date_str, '%Y-%m-%d')

        # Check if the author exists, otherwise create a new one
        author = Author.query.filter_by(name=author_name).first()
        if not author:
            author = Author(name=author_name)
            db.session.add(author)
            db.session.commit()

        # Create a new post
        post = Post(name=name, date=date, slug=slug, author_id=author.id, content=content)
        db.session.add(post)
        db.session.commit()

        return redirect(url_for('simple_pages.index'))

    return render_template('Blog/publish-posts.html')

# Creating the route for making changes to posts in the database via the edit button on the Blog page
@blueprint.route('/edit-post/<int:post_id>', methods=['GET', 'POST'])
def edit_post(post_id):
    post = Post.query.get_or_404(post_id)

    if request.method == 'POST':
        post.name = request.form['name']
        post.slug = request.form['name']
        post.date = datetime.strptime(request.form['date'], '%Y-%m-%d')
        post.author.name = request.form['author_name']
        post.content = request.form['content']
        db.session.commit()
        return redirect(url_for('simple_pages.index'))

    return render_template('Blog/edit_post.html', post=post)


@blueprint.route('/delete-post/<int:post_id>', methods=['POST'])
def delete_post(post_id):
    post = Post.query.get_or_404(post_id)
    db.session.delete(post)
    db.session.commit()
    return redirect(url_for('simple_pages.index'))

# Workaround solution to execute the seed file in order to create a database for the hosted webpage
@blueprint.route('/run-seed')
def run_seed():
  if not Post.query.filter_by(slug='author2').first():
    import app.scripts.seed
    return 'Database seed completed!'
  else:
    return 'Nothing to run.'