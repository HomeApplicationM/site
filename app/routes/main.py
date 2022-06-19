# from interplast import create_app
from flask import Blueprint, render_template
from datetime import datetime
# from flask_login import login_required

main = Blueprint('main', __name__)

@main.route('/')
@main.route('/home')
@main.route('/index')
def home():
    return render_template(
        'index.html',
        title='Home Page',
        year=datetime.now().year,
    )


@main.route('/contact')
def contact():
    return render_template(
        'contact.html',
        title='Contact',
        year=datetime.now().year,
        message='Contact us'
    )


@main.route('/about')
def about():
    return render_template(
        'about.html',
        title='About',
        year=datetime.now().year,
        message=''
    )
