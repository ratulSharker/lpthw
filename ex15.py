from sys import argv

script, file_name = argv

txt = open(file_name)

print(f"Here is your file {file_name}:", end="\n\n")
print(txt.read())

txt.close()

# Run like `python3 ex15.py ex15_sample.txt`