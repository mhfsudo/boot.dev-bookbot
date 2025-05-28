def get_word_count (text):
    count = 0
    words = text.split()
    for word in words:
        count += 1
    return count

def get_character_count (text):
    words_count = {}
    lower_words = text.lower()
    characters = list(lower_words)

    for characters in lower_words:
        if characters in words_count:
            words_count[characters] += 1
        else:
            words_count[characters] = 1
    return words_count