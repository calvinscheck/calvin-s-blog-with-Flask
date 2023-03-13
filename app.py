# Setting up general stuff
from flask import Flask, redirect, url_for, render_template
app = Flask(__name__)
app.config.from_object('config')


# Documenting all my articles
blog_posts_dictionary = {
        'article1': 'The foundation of happiness',
        'article2': 'Life means balance',
        'article3': 'The power of words',
        'article4': 'Upcoming article',
    }


# Defining which route should render what HTML file
@app.route('/')
def index():
    return render_template('index.html', posts=blog_posts_dictionary)

@app.route('/blog-posts')
def blog_posts():
    return render_template('blog-posts.html', posts=blog_posts_dictionary)

@app.route('/post-page')
def postpage():
    return render_template('post-page.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/my-account')
def my_account():
    return render_template('my-account.html')


# Making all articles existing accessible via the URL. Otherwise, return Error Message!
@app.route('/post-page/<placeholder>')
def post_page(placeholder):
    if placeholder in blog_posts_dictionary:
        return render_template('post-page.html', article_name = blog_posts_dictionary[placeholder])
    else: 
        return render_template('post-page.html', article_name = "does not exist yet")


app.run()