# from interplast import create_app
from flask import Blueprint, render_template, flash, redirect
from flask_login import current_user, login_user, logout_user, login_required
from flask import url_for
from datetime import datetime
from app.forms import LoginForm, RegistrationForm, AddBirthday
from app.models import User, PersonOfInterest
from app import db, login

birthdays_bp = Blueprint('birthdays', __name__)

@birthdays_bp.route('/add_birthday', methods=['GET', 'POST'])
@login_required
def add_birthday():
    form = AddBirthday()
    if form.validate_on_submit():
        poi = PersonOfInterest(
            first_name=form.first_name.data,
            last_name = form.last_name.data,
            birthday=form.birthday.data,
            related_to_user_id=current_user.id
            )
        db.session.add(poi)
        db.session.commit()
        flash('Congratulations, you added a new birthday!')
    return render_template('add_birthday.html', title='Add a Birthday', form=form)
