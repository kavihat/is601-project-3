from flask_login import login_user, login_required, logout_user, current_user
from app import db
from app.db.models import User, Song

# def test_login_real_user(client):
#     response = client.get("/login")
#     assert b"keith" in response.data