from flask import Blueprint, render_template
from werkzeug.exceptions import abort

from lyrics.models import Song

bp = Blueprint('songs', __name__)


@bp.route('/', methods=['GET'])
def list_songs():
    songs = Song.query.all()
    return render_template('songs/song_list.html', songs=songs)


@bp.route('/<int:song_id>', methods=['GET'])
def get_song(song_id):
    song = Song.query.filter_by(id=song_id).first()
    if not song:
        abort(404)
    print(song.text)
    return render_template('songs/song.html', song=song)
