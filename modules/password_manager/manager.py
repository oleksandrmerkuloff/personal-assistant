from typing import Any

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


def get_password() -> None:
    name = input('If you searching by name write it here or skip for an id search: ').strip()
    id = input('Write an id here or keep it empty: ').strip()
    if name:
        password = PasswordModel.get_single_record(file_path=STORAGE_PATH, name=name)
    else:
        password = PasswordModel.get_single_record(file_path=STORAGE_PATH, id=id)
    for key, value in password.items():
        print(f'{key}: {value}')


def get_passwords_list() -> list[Any]|str:
    name = input('Write part or full name for interesting passwords for you: ').strip()
    if not name:
        return 'You can\'t use an empty value for name!'
    return PasswordModel.get_records_list(file_path=STORAGE_PATH, name=name) 


def delete_password() -> None:
    password_id = input('Write password id for delete: ').strip()
    if PasswordModel.delete(file_path=STORAGE_PATH, id=password_id):
        print('Success!')
    else:
        print('Try again!')