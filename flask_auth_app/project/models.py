from flask_login import UserMixin
from . import db


# class User
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True, unique=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))


#class Entries call db.model.py
class Entries(db.Model):
    bhid = db.Column(db.Integer)
    date = db.Column(db.Date)
    id = db.Column(db.Integer, db.ForeignKey('user.id'))
    comments = db.Column(db.String(1500))
    numeggspres = db.Column(db.Integer)
    alive = db.Column(db.Integer)
    dead = db.Column(db.Integer)
    activespecies = db.Column(db.String(45))
    other = db.Column(db.String(45))
    cowbird = db.Column(db.String(45))
    repairs = db.Column(db.String(1000))
    entryId = db.Column(db.Integer, primary_key=True)


