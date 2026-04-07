import os

from cryptography.fernet import Fernet

from settings import BASE_DIR


def encrypt_password(password: str) -> str:
    key = get_master_key()
    f = Fernet(key)
    token = f.encrypt(password.encode('utf-8'))
    return token.decode('utf-8')


def decrypt_password(encrypted_password: str) -> str:
    key = get_master_key()
    f = Fernet(key)
    return f.decrypt(encrypt_password.encode('utf-8')).decode('utf-8')


def get_master_key() -> bytes:
    key = os.getenv('PASSWORD_MANAGER_KEY')
    if not key:
        generate_master_key()
        key = os.getenv('PASSWORD_MANAGER_KEY', '')
    return key.encode('utf-8')


def generate_master_key() -> None:
    master_key = Fernet.generate_key().decode('utf-8')
    with open(BASE_DIR + '/.env', 'a') as file:
        file.write(f'PASSWORD_MANAGER_KEY={master_key}')
