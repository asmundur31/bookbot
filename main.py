from stats import get_num_words, get_text_book, get_num_characters, sort_by_count
import sys

def main():
    if(len(sys.argv) != 2):
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    text = get_text_book(sys.argv[1])
    num_words = get_num_words(text)
    num_characters = get_num_characters(text)
    sorted_characters = sort_by_count(num_characters)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for d in sorted_characters:
        print(f"{d['char']}: {d['count']}")
    print("============= END ===============")

if __name__ == "__main__":
    main()