from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()


def init_db(app):
    db.init_app(app)
    migrate.init_app(app, db)


class Song(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.Text())
    album = db.Column(db.String(100))
    name = db.Column(db.String(100))


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
