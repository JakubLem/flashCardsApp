import config
from reader.read import read
from app.app import app

def main():
    flashcards = read(config.JSON_FILE_PATH)
    app(flashcards)


if __name__ == "__main__":
    main()