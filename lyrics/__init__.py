from flask import Flask

from lyrics.admin import init_admin
from .database import init_db
from lyrics.models import Song
from lyrics.session import RedisSessionInterface


def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('config.py')

    app.session_interface = RedisSessionInterface()

    init_db(app)
    init_admin(app)
    from lyrics.views import auth
    app.register_blueprint(auth.bp)

    from lyrics.views import songs
    app.register_blueprint(songs.bp)

    from lyrics.views import user
    app.register_blueprint(user.bp)

    return app
