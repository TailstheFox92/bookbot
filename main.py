import argparse
parser = argparse.ArgumentParser()
parser.add_argument("book_filepath")
args = parser.parse_args()


def read_book():
    with open(args.book_filepath) as f:
        file_contents = f.read()
        return file_contents


def count_words(words):
    count = 0
    for word in words:
        count += 1
    return count


def main():
    try:
        words = read_book().split()
        print(f"There are {count_words(words)} words in this book!")

    except FileNotFoundError:
        print("Could not find the specified file")


main()
