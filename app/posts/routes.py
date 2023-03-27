from flask import Blueprint, render_template
blueprint = Blueprint('posts', __name__)


# Documenting all my articles
blog_posts_dictionary = {
        'article1': 'The foundation of happiness',
        'article2': 'Life means balance',
        'article3': 'The power of words',
        'article4': 'Upcoming article',
    }

# Routes related to blog posts
@blueprint.route('/blog-posts')
def blog_posts():
    return render_template('Blog/index.html', posts=blog_posts_dictionary)

@blueprint.route('/post-page')
def postpage():
    return render_template('Blog/post-page.html')

# Making all articles existing accessible via the URL. Otherwise, return Error Message!
@blueprint.route('/post-page/<placeholder>')
def post_page(placeholder):
    if placeholder in blog_posts_dictionary:
        return render_template('post-page.html', article_name = blog_posts_dictionary[placeholder])
    else: 
        return render_template('post-page.html', article_name = "does not exist yet")
