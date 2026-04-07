from dotenv import load_dotenv

from settings import create_storage
from manager import add_password


load_dotenv()


def main():
    create_storage()

    state = True
    while state:
        command = input('Add command: ').strip()
        if command == 'add':
            add_password()
        elif command == 'exit':
            state = False


if __name__ == '__main__':
    main()
