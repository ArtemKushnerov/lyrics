"""empty message

Revision ID: 97f232f82a45
Revises: 6b4811de12ff
Create Date: 2019-07-16 09:51:31.985338

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
from sqlalchemy import orm

from lyrics import Song
from lyrics.models import Album, User
from lyrics.utils import shortuuid

revision = '97f232f82a45'
down_revision = '6b4811de12ff'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('album', sa.Column('uuid', sa.String(length=8), nullable=True))
    op.create_index(op.f('ix_album_uuid'), 'album', ['uuid'], unique=True)
    op.add_column('song', sa.Column('uuid', sa.String(length=8), nullable=True))
    op.create_index(op.f('ix_song_uuid'), 'song', ['uuid'], unique=True)
    op.add_column('user', sa.Column('uuid', sa.String(length=8), nullable=True))
    op.create_index(op.f('ix_user_uuid'), 'user', ['uuid'], unique=True)

    # ### end Alembic commands ###

    def get_entity_with_uuid(e):
        e.uuid = shortuuid()
        return e

    bind = op.get_bind()
    session = orm.Session(bind=bind)
    songs = [get_entity_with_uuid(s) for s in session.query(Song).all()]
    albums = [get_entity_with_uuid(a) for a in session.query(Album).all()]
    users = [get_entity_with_uuid(u) for u in session.query(User).all()]
    session.add_all(songs)
    session.add_all(albums)
    session.add_all(users)
    session.commit()


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_user_uuid'), table_name='user')
    op.drop_column('user', 'uuid')
    op.drop_index(op.f('ix_song_uuid'), table_name='song')
    op.drop_column('song', 'uuid')
    op.drop_index(op.f('ix_album_uuid'), table_name='album')
    op.drop_column('album', 'uuid')
    # ### end Alembic commands ###
