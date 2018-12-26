# imports argv so we can use command line arguments
from sys import argv
#decode the argv and save to variables as strings
script, filename = argv
# open the input file as read text (default). Closes automatically by default.
#  Returns the file object type io.TextIOWrapper object.  
txt = open(filename)

print(f"Here's your file {filename}:")
# call io.TextIOWrapper method on file object.
print(txt.read())

# close for practice
txt.close()

print("Type the filename again:")
# read from std io filename
file_again = input(">")
# all the same as above.
txt_again = open(file_again)

print(txt_again.read())
txt_again.close()
