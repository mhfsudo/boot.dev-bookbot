from stats import get_word_count
from stats import get_character_count

def main():
    filepath = "/Users/mhf/Git/Personal/boot.dev-bookbot/books/frankenstein.txt"
    text = get_book_text(filepath)
    count = get_word_count(text)
    print(f"{count} words found in the document")
    character_count = get_character_count(text)
    print(f"count {character_count}")

def get_book_text (filepath):
    with open(filepath) as f:
        return f.read();

if __name__ == '__main__':
    main()