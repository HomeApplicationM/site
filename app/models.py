from app import db, login, admin
from flask_login import UserMixin
from flask_security import RoleMixin
from werkzeug.security import generate_password_hash, check_password_hash

class User(UserMixin, db.Model):
    __tablename__ = 'users'
    __table_args__ = {'extend_existing': True}

    id = db.Column(db.Integer(), db.Sequence('user_seq'), primary_key=True)
    username = db.Column(db.String)
    password_hash = db.Column(db.String(128))
    first_name = db.Column(db.String)
    email_address = db.Column(db.String)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return '<User {}>'.format(self.username)

class PersonOfInterest(db.Model):
    __tablename__ = 'pois'
    __table_args__ = {'extend_existing': True}

    id = db.Column(db.Integer(), db.Sequence('poi_seq'), primary_key=True)
    first_name = db.Column(db.String)
    last_name = db.Column(db.String)
    related_to_user_id = db.Column(db.Integer, db.ForeignKey(User.id))
    birthday = db.Column(db.DateTime)

    def __repr__(self):
        return '<PersonOfInterest {}>'.format(self.first_name)
