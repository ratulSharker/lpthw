from sys import argv

script, in_file = argv

def print_all(f):
    print(f.read())

def rewind(f):
    f.seek(0)

def print_a_line(line_number, f):
    print(f"Line number: {line_number}, {f.readline()}", end = "")

current_file = open(in_file)

print("First lets print the whole file: \n")

print_all(f = current_file)

print("Now lets rewind, kind of like a tape")

rewind(f = current_file)

print("Lets print three lines")

current_line = 1
print_a_line(line_number = current_line, f = current_file)

current_line = current_line + 1
print_a_line(line_number = current_line, f = current_file)

current_line = current_line + 1
print_a_line(line_number = current_line, f = current_file)