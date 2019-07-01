from . import db


class Song:
    pass


class Author:
    pass


class Translation:
    pass


class Album:
    pass


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))
