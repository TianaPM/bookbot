import sys

from stats import get_num_words
from stats import get_num_characters
from stats import sort_dict

def get_book_text(book):
    with open(book) as f:
        text = f.read()
    return text

def main():
    
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    path = sys.argv[1]
    text = get_book_text(path)
    num_of_words = get_num_words(text)
    dict_of_chars = get_num_characters(text)
    sorted_list = sort_dict(dict_of_chars)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_of_words} total words")
    print("--------- Character Count -------")

    for item in sorted_list:
        if item["char"].isalpha() == False:
            pass
        else:
            print(f"{item["char"]}: {item["num"]}")

    print("============= END ===============")


main()