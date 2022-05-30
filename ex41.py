import random
from urllib.request import urlopen
import sys


def fetch_words() -> list[str]:
    url: str = "http://learncodethehardway.org/words.txt"
    words: list[str] = []

    for word in urlopen(url).readlines():
        words.append(str(word.strip(), encoding="utf-8"))

    return words

if len(sys.argv) == 2 and sys.argv[1] == 'english':
    phrase_first = True
else:
    phrase_first = False

# param `%%%`, `***` & `@@@`
phrases = {
    "class %%%(%%%):":
        "Make a class named %%% that is-a %%%.",

    "class %%%(object):\n\tdef __init__(self, ***)":
        "class %%% has-a __init__ that takes self and *** param.",

    "class %%%(object):\n\tdef ***(self, @@@)":
        "class %%% has-a function *** that takes self and @@@ params.",
    
    "*** = %%%()":
        "Set *** to and instance of class %%%.",

    "***.***(@@@)":
        "From *** get the *** function, call it with params self, @@@.",
    
    "***.*** = '***'":
        "From *** get the *** attribute and set it to '***'."
}

def convert(snippet: str, phrase, words: list[str]):
    # collect random names
    class_names : list[str] = [w.capitalize() for w in
                random.sample(words, snippet.count("%%%"))]
    other_names : list[str] = random.sample(words, snippet.count("***"))

    results : list[str] = []
    param_names : list[str] = []

    for i in range(0, snippet.count("@@@")):
        param_count = random.randint(1, 3)
        param_names.append(', '.join(random.sample(words, param_count)))

    for sentence in snippet, phrase:
        result = sentence[:]

        # replace class names
        for class_name in class_names:
            result = result.replace("%%%", class_name, 1)
        
        # replace other names
        for other_name in other_names:
            result = result.replace("***", other_name, 1)
        
        # replace the parameter
        for param in param_names:
            result = result.replace("@@@", param, 1)

        # snippet, phrase
        results.append(result)

    return results


try:
    words : list[str] = fetch_words()
    while True:
        snippets: list[str] = list(phrases.keys())
        random.shuffle(snippets)

        for snippet in snippets:
            phrase : str = phrases[snippet]
            question, answer = convert(snippet, phrase, words)
            if phrase_first:
                question, answer = answer, question
            
            print(question)
            input("> ")
            print(f"Answer : {answer}", end="\n\n")
except EOFError:
    print("\nBye")

