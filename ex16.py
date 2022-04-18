from sys import argv

script, file_name = argv

print(f"We're going to erase file {file_name}")
print("If you don't want that, hit CTRL+C")
print("If you do want that, hit RETURN")

input("?")

print("Opening the file")
target = open(file_name, "w")

print("Truncating the file. Goodbye {file_name}")
target.truncate()

print("Now i'm going to ask you for three lines.")

line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")

print("I'm going to write these to the file.")

# target.write(line1)
# target.write("\n")
# target.write(line2)
# target.write("\n")
# target.write(line3)
# target.write("\n")
target.write(f"""{line1}
{line2}
{line3}
""")

print("Writing complete, now closing the file")
target.close()