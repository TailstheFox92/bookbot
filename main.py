import argparse
parser = argparse.ArgumentParser()
parser.add_argument("book_filepath")
args = parser.parse_args()


def read_book(book_path):
    with open(book_path) as f:
        return f.read()


def count_words(words):
    return len(words)


def count_characters(text):
    text = text.lower()
    characters = {}
    for char in text:
        if char not in characters.keys():
            characters[char] = 1
        else:
            characters[char] += 1
    return characters


def convert_dict(char_count):
    new_char_count = []
    for char in char_count:
        if char.isalpha():
            new_char_count.append({"char": char, "num": char_count[char]})
    return new_char_count


# A function that takes a dictionary and returns the value of the "num" key
# This is how the `.sort()` method knows how to sort the list of dictionaries
def sort_on(char_count):
    return char_count["num"]


def main():
    try:
        book_path = args.book_filepath
        text = read_book(book_path)  # The text within the book
        words = text.split()  # The list of words within the book
        num_words = count_words(words)  # The amount of words in the book
        # A dictionary containing the amount of times each word appears in the
        # book
        char_count = count_characters(text)
        char_list = convert_dict(char_count)
        char_list.sort(reverse=True, key=sort_on)
        print(f"--- Begin report of {book_path} ---")
        print(f"{num_words} in the document\n")
        for item in char_list:
            print(f"The '{item["char"]}' character was found {item["num"]} "
                  "times")
        print("--- End report ---")

    except FileNotFoundError:
        print("Could not find the specified file")

    except UnicodeDecodeError:
        print("Got a Unicode Decode Error, is the file plain text?")


main()
