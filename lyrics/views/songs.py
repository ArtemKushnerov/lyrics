from flask import Blueprint, render_template
from werkzeug.exceptions import abort

from lyrics.models import Song, Album

bp = Blueprint('songs', __name__)


@bp.route('/', methods=['GET'])
def list_songs():
    songs = Song.query.order_by(Song.name).all()
    return render_template('songs/song_list.html', songs=songs)


@bp.route('/<song_id>', methods=['GET'])
def get_song(song_id):
    song = Song.query.filter_by(uuid=song_id).first()
    if not song:
        abort(404)
    return render_template('songs/song.html', song=song)


@bp.route('/album/<album_id>', methods=['GET'])
def get_album(album_id):
    print('start album')
    album = Album.query.filter_by(uuid=album_id).first()
    print('album')
    if not album:
        abort(404)
    return render_template('songs/album.html', album=album)


@bp.route('/albums', methods=['GET'])
def list_albums():
    albums = Album.query.order_by(Album.name).all()
    return render_template('songs/album_list.html', albums=albums)
