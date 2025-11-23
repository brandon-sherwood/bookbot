def word_count(file_contents):
    text = file_contents.split()
    num_words = len(text)
    return num_words


def character_count(file_contents):
    character = {}

    for char in file_contents:
        lower_char = char.lower()
        if lower_char in character:
            character[lower_char] += 1
        else:
            character[lower_char] = 1

    return character


def sort_on(character):
    return character["num"]


def sorted_characters(character):
    char_list = []

    for i in character:
        char_dict = {"char": i, "num": character[i]}
        char_list.append(char_dict)

    char_list.sort(reverse=True, key=sort_on)

    return char_list
