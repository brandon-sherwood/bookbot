def word_count(file_contents):
    text = file_contents.split()
    num_words = len(text)
    print(f"Found {num_words} total words")


def character_count(file_contents):
    character = {}

    for char in file_contents:
        lower_char = char.lower()
        if lower_char in character:
            character[lower_char] += 1
        else:
            character[lower_char] = 1

    return character
