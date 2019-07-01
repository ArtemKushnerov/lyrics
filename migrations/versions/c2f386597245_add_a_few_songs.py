"""Add a few songs

Revision ID: c2f386597245
Revises: 194a38d5797a
Create Date: 2019-07-01 17:56:44.281162

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
from sqlalchemy import orm

from lyrics.models import Song

revision = 'c2f386597245'
down_revision = '194a38d5797a'
branch_labels = None
depends_on = None


def upgrade():
    bind = op.get_bind()
    session = orm.Session(bind=bind)
    songs = [
        Song(name='If I Fell', text='If I fell in love with you\nWould you promise to be true...', album='A Hard Day\'s Night'),
        Song(name='I\'m looking through you', text='I\'m looking through you\nWhere did you go...', album='Rubber Soul'),
        Song(name='Happiness is a warm gun', text='She\'s not a girl who misses much \nDo do do do do do, oh yeah...', album='White album'),
    ]
    session.add_all(songs)
    session.commit()


def downgrade():
    pass
