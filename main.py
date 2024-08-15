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


def main():
    try:
        text = read_book(args.book_filepath)
        words = text.split()
        num_words = count_words(words)

        print(f"There are {num_words} words in this book!")

        print("These are amount of times each character appears in the book:")
        print(count_characters(text))

    except FileNotFoundError:
        print("Could not find the specified file")

    except UnicodeDecodeError:
        print("Got a Unicode Decode Error, is the file plain text?")


main()
