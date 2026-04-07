from db.models import PasswordModel
from crypto import encrypt_password
from settings import STORAGE_PATH


def add_password():
    name = input('Create unique name for the new record: ').strip()
    password = input('Write a password for the new record: ').strip()
    if not password or not name:
        print('Found empty error!')
        print('"Password" and "Name" are required! Try again please!')
        return None
    url = input('Paste an url for the new record: ').strip()

    encrypted_password = encrypt_password(password)

    new_password = PasswordModel(
        name=name,
        encrypted_password=encrypted_password,
        url=url
        )
    return new_password.save(STORAGE_PATH)



def get_password():
    pass


def get_passwords_list():
    pass


def delete_password():
    pass