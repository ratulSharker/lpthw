
language_file = open("languages.txt")
language_output_file = open("language-encoded.txt", "w")

def readline(language_file, language_output_file):
    line = language_file.readline()
    
    encoded_line = line.encode("utf-8")
    
    if line:
        readline(language_file, language_output_file)
    
    language_output_file.write(f"{encoded_line}")
    language_output_file.write("\n")
    
    

readline(language_file, language_output_file)

language_file.close()
language_output_file.close()