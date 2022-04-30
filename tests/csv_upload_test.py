from flask_login import current_user
from flask_wtf.file import FileField

from app import User
from app.auth import register_form
from app import db
from app.db.models import User, Song
# def test_upload_success(application, client):
#     with application.app_context():
#         email = 'testuser@email.com'
#         password = 'testtest'
#         user = User.query.filter_by(email=email).first()
#         assert user is None
#
#         response = client.post("/register", data=dict(email=email, password=password, confirm=password), follow_redirects=True)
#         response = client.post("/login", data=dict(email=email, password=password),
#                                follow_redirects=True)
#
#         response = client.post("/songs/upload", data=dict(file=FileField()))
#         assert db.session.query(Song).count() != 0


def test_upload_failure(application, client):
    with application.app_context():
        email = 'notauser@email.com'
        password = 'testtest'
        response = client.get("/songs/upload")
        assert db.session.query(Song).count() == 0

