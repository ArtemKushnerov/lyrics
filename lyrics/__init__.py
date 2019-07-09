from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from lyrics.session import RedisSessionInterface

db = SQLAlchemy()
migrate = Migrate()


def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('config.py')
    app.session_interface = RedisSessionInterface()

    db.init_app(app)
    migrate.init_app(app, db)
    from lyrics.blueprints import auth

    app.register_blueprint(auth.bp)
    from lyrics.blueprints import songs

    app.register_blueprint(songs.bp)
    return app
