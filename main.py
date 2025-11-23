import sys
from stats import word_count
from stats import character_count
from stats import sorted_characters


def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()

    return file_contents


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    path_to_book = sys.argv[1]

    frankenstein = get_book_text(path_to_book)
    frankenstein_words = word_count(frankenstein)
    frankenstein_characters = character_count(frankenstein)
    frankenstein_sort_chars = sorted_characters(frankenstein_characters)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path_to_book}")
    print("----------- Word Count ----------")
    print(f"Found {frankenstein_words} total words")
    print("--------- Character Count -------")
    for i in frankenstein_sort_chars:
        char = i["char"]
        num = i["num"]
        if char.isalpha():
            print(f"{char}: {num}")


if __name__ == "__main__":
    main()
