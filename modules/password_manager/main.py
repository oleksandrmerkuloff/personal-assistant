import os


BASE_DIR = os.getcwd()
STORAGE_PATH = BASE_DIR + '/storage/'


def storage_initial():
    if not os.path.isdir(STORAGE_PATH):
        os.mkdir(STORAGE_PATH)
        
        with open(STORAGE_PATH + 'users.csv', 'x') as file:
            pass

        with open(STORAGE_PATH + 'passwords.json', 'x') as file:
            pass


def main():
    storage_initial()


if __name__ == '__main__':
    main()
