from flask import Blueprint, render_template
from .models import Post
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


# Making all articles existing accessible via the URL. Otherwise, return Error Message!
# @blueprint.route('/post-page/<placeholder>')
# def post_page(placeholder):
#     if placeholder in Posts.query.all():
#         return render_template('post-page.html', article_name = blog_posts_dictionary[placeholder])
#     else: 
#         return render_template('post-page.html', article_name = "does not exist yet")
