import sys
from stats import count_words, count_characters, sort_char

if len(sys.argv) < 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

def get_book_text(filepath):
    file_contents = ""
    with open(filepath) as f:
        file_contents = f.read()
    return(file_contents)

def main():
    book_text = get_book_text(sys.argv[1])
    count_char = count_characters(book_text)
    sorted_char_list = sort_char(count_char)

    print(f"""
        ============ BOOKBOT ============
        Analyzing book found at {sys.argv[1]}...
        ----------- Word Count ----------
        Found {count_words(book_text)} total words
        --------- Character Count -------
        """)
    for char_obj in sorted_char_list:
        print(f"""{char_obj["char"]}: {char_obj["num"]}""")

main()