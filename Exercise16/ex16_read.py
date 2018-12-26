from sys import argv

script, filename = argv

print("Opening the file...")
target = open(filename, 'r')

print("I'm going to read and echo the file.")

contents = target.read()

print(contents)
print("And finally, we close it.")
target.close()
