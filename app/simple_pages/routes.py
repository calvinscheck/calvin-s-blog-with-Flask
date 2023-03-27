from flask import Blueprint, render_template, redirect, url_for, send_file
blueprint = Blueprint('simple_pages', __name__)

# Defining which route should render what HTML file
@blueprint.route('/')
def index():
    return render_template('simple_pages/index.html')

@blueprint.route('/contact')
def contact():
    return render_template('simple_pages/contact.html')

@blueprint.route('/my-account')
def my_account():
    return render_template('simple_pages/my-account.html')