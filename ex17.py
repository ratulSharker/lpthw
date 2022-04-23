from sys import argv
from os.path import exists

script, from_file, to_file = argv

print(f"Copying from {from_file} to {to_file}")

source_file = open(from_file); source_file_data = source_file.read()

print(f"The input file is {len(source_file_data)} bytes long")
print(f"Does output file exists {exists(to_file)}")
print("Ready, Hit RETURN to continue, press CTRL+C to abort.")
input()

destination_file = open(to_file, 'w')
destination_file.write(source_file_data)

print("File copied")

source_file.close()
destination_file.close()