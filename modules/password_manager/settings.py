import os
from pathlib import Path


BASE_DIR = os.getcwd()
STORAGE_PATH = Path(BASE_DIR + '/storage/passwords.json')


def create_storage():
    if not os.path.isdir(STORAGE_PATH.parent):
        os.mkdir(STORAGE_PATH.parent)
