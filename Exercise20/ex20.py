# imports argv from sys module
from sys import argv

# assigns argv elements to variables
script, input_file = argv

# function that prints the whole file by just printing what it reads.
def print_all(f):
    print(f.read())

# puts the location at the beginning of the file
def rewind(f):
    f.seek(0)

# prints one line at a time, with the line number being given by line_count
def print_a_line(line_count, f):
    print(line_count, f.readline())

# open file and return file object
current_file = open(input_file)

print("First let's print the whole file:\n")

# calls print_all above with the file object
print_all(current_file)

print("Now let's rewind, kind of like a tape.")

# calls rewind on file object
rewind(current_file)

print("Let's print three lines:")

# prints first line
current_line = 1
print_a_line(current_line, current_file)

# prints second line
current_line += 1
print_a_line(current_line, current_file)

# prints third line
current_line += 1
print_a_line(current_line, current_file)
