from flask import Flask

from lyrics.admin import init_admin
from .models import init_db
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

    return app
