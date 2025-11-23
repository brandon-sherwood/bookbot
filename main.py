from stats import word_count
from stats import character_count


def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()

    return file_contents


def main():
    frankenstein = get_book_text("books/frankenstein.txt")
    frankenstein_words = word_count(frankenstein)
    frankenstein_characters = character_count(frankenstein)
    print(frankenstein_characters)


if __name__ == "__main__":
    main()
