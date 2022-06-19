from app import db, login, admin
# from flask_login import UserMixin
# from flask_security import RoleMixin
from werkzeug.security import generate_password_hash, check_password_hash
# from sqlalchemy import Sequence
# from sqlalchemy.ext.declarative import declarative_base

class User(db.Model):
    __tablename__ = 'User'
    __table_args__ = {'extend_existing': True}

    id = db.Column(db.Integer(), db.Sequence('user_seq'), primary_key=True)
    # UserID = db.Column(db.Integer(), primary_key=True)
    Username = db.Column(db.String)
    # Password = db.Column(db.String)
    Password_hash = db.Column(db.String(128))
    # Is_Admin = db.Column(db.Boolean)
    LastName = db.Column(db.String)
    FirstName = db.Column(db.String)
    EmailAddress = db.Column(db.String)
    def set_password(self, password):
        self.Password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.Password_hash, password)

    def __repr__(self):
        return '<User {}>'.format(self.Username)
