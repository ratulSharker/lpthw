import sys

script, input_encoding, error = sys.argv

def print_line(line: str, encoding, errors):
    next_lang = line.strip()
    raw_bytes = next_lang.encode(encoding, errors = errors)
    cooked_string = raw_bytes.decode(encoding, errors = errors)
    
    print(f"{raw_bytes} <=====> {cooked_string}")
    

def main(language_file, encoding, errors):
    line = language_file.readline()
    
    if line:
        print_line(line, encoding, errors)
        main(language_file, encoding, errors)
        
language_file = open("languages.txt", encoding="utf-8")
main(language_file, input_encoding, error)