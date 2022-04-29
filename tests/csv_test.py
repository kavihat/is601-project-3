"""This test the csv logging"""
import os
from app import config

def is_path_exist():
    upload_dir = config.Config.UPLOAD_FOLDER
    assert os.path.exists(upload_dir) is True

def is_file_exist():
    upload_dir = config.Config.BASE_DIR
    assert os.path.isfile(os.path.join(upload_dir + '/uploads/music.csv')) is True

def test_csv_file_exists(client):
    client.get("/")
    is_path_exist()
    is_file_exist()