import os


BASE_DIR = os.getcwd()
STORAGE_PATH = BASE_DIR + '/storage/'


def create_storage():
    if not os.path.isdir(STORAGE_PATH):
        os.mkdir(STORAGE_PATH)
