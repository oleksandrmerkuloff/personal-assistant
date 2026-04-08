from dotenv import load_dotenv

from settings import create_storage
from manager import add_password, get_passwords_list, delete_password, get_password
from crypto import decrypt_password


load_dotenv()


def main():
    create_storage()

    state = True
    while state:
        command = input('Write a command: ').strip().lower()
        if command == 'add':
            add_password()
        elif command == 'single':
            get_password()
        elif command == 'list':
            passwords = get_passwords_list()
            for password in passwords:
                print()
                for key, value in password.items():
                    if key == 'password':
                        value = decrypt_password(value)
                    print(f'{key}: {value}')
            print()
        elif command == 'delete':
            delete_password()
        elif command == 'exit':
            state = False


if __name__ == '__main__':
    main()
