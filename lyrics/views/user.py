from flask import Blueprint, request, redirect, url_for, render_template, g
from werkzeug.utils import secure_filename

from lyrics.config import INCOGNITO_PIC_ADDRESS, S3_BUCKET
from lyrics.helpers import upload_file_to_s3
from lyrics.models import db
from lyrics.views.auth import login_required

bp = Blueprint('user', __name__)

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@bp.route("/avatars", methods=["POST"])
@login_required
def avatars():
    if "user_file" not in request.files:
        return "No user_file key in request.files"
    file = request.files["user_file"]
    if file.filename == "":
        return "Please select a file"
    if file and allowed_file(file.filename):
        file.filename = secure_filename(file.filename)
        avatar = upload_file_to_s3(file, S3_BUCKET)
        g.user.avatar = avatar
        db.session.add(g.user)
        db.session.commit()
        return redirect(url_for('user.profile'))
    else:
        return redirect("/")


@bp.route('/profile', methods=['GET', 'POST'])
@login_required
def profile():
    user = g.user
    if not user.avatar:
        user.avatar = INCOGNITO_PIC_ADDRESS
    return render_template('auth/profile.html', user=g.user)
