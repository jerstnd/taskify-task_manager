from taskify import db
from flask_login import UserMixin

class ToDo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    todo_list = db.Column(db.String(150))
    todo_complete = db.Column(db.Boolean)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))
    todo = db.relationship('ToDo')

class Notes(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    note = db.Column(db.String(5000))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))