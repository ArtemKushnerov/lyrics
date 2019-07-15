from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView

from .models import Song
from .models import db

admin = Admin()


def init_admin(app):
    admin.init_app(app)
    admin.add_view(ModelView(Song, db.session))
