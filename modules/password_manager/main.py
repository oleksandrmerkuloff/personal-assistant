import os

from db.models import PasswordRecord

BASE_DIR = os.getcwd()
STORAGE_PATH = BASE_DIR + '/storage/'


def main():
    if not os.path.isdir(STORAGE_PATH):
        os.mkdir(STORAGE_PATH)
    
    test_record = PasswordRecord(name='name', password='test', salt='test', url='google.com')
    test_record.save(file_path=STORAGE_PATH)


if __name__ == '__main__':
    main()
