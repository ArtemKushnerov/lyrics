from lyrics.utils import shortuuid
from .database import db


class Entity(db.Model):
    __abstract__ = True

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    uuid = db.Column(db.String(8), unique=True, index=True, nullable=False, default=shortuuid)


class Song(Entity):
    text = db.Column(db.Text(), nullable=False)
    album_id = db.Column(db.Integer, db.ForeignKey('album.id'))

    def __str__(self):
        return self.name


class Translation:
    pass


class Album(Entity):
    songs = db.relationship(Song, backref='album', lazy=True)
    year = db.Column(db.Integer)

    def __str__(self):
        return self.name


class User(Entity):
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)
    avatar = db.Column(db.String(100))
