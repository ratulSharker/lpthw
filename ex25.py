def break_words(stuff):
    """This function will break up words for us"""
    words = stuff.split(" ")
    return words

def sort_words(words):
    """Sort Words"""
    return sorted(words)

def print_first_word(words):
    """Remove the first word, then print it"""
    first_word = words.pop(0)
    print(first_word)
    
def print_last_word(words):
    """Remove last word, then print it"""
    last_word = words.pop(-1)
    print(last_word)

def sort_scentence(sentence):
    words = break_words(sentence)
    return sort_words(words)

def print_first_and_last(sentence):
    """Print the first and last words of sentence"""
    words = break_words(sentence)
    print_first_word(words)
    print_last_word(words)

def print_first_and_last_sorted(scetnence):
    """Print the first and last words of sentence after sorting"""
    words = break_words(scetnence)
    sorted_words = sort_words(scetnence)
    print_first_word(sorted_words)
    print_last_word(sorted_words)

    