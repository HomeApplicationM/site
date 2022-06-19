# from interplast import create_app
from flask import Blueprint, render_template, flash, redirect
from flask_login import current_user, login_user, logout_user, login_required
from flask import url_for
from datetime import datetime
from app.forms import LoginForm, RegistrationForm
from app.models import User
from app import db, login

login_bp = Blueprint('login', __name__)

# @login.user_loader
# def load_user(user_id):
#     return User.query.get(int(user_id))

@login_bp.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login.login'))
        login_user(user, remember=form.remember_me.data)
        return redirect(url_for('main.home'))
    return render_template('login.html', title='Sign In', form=form)


@login_bp.route('/logout')
# @login_required
def logout():
    logout_user()
    return redirect(url_for('main.home'))

@login_bp.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(
            username=form.username.data,
            first_name=form.firstname.data,
            email_address=form.email.data,
            )
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('login.login'))
    return render_template('register.html', title='Register', form=form)

@login_bp.route('/user/<username>')
@login_required
def user(username):
    user = User.query.filter_by(username=username).first_or_404()
    return render_template('profile_page.html', user=user)
