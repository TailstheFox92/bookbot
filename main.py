import argparse
parser = argparse.ArgumentParser()
parser.add_argument("book_filepath")
args = parser.parse_args()


def read_book(book_path):
    with open(book_path) as f:
        return f.read()


def count_words(words):
    return len(words)


# def count_characters(book):
#     characters = {}


def main():
    try:
        text = read_book(args.book_filepath)
        words = text.split()
        num_words = count_words(words)

        print(f"There are {num_words} words in this book!")

    except FileNotFoundError:
        print("Could not find the specified file")

    except UnicodeDecodeError:
        print("Got a Unicode Decode Error, is the file plain text?")


main()
