from sys import argv
from os.path import exists

script, from_file, to_file = argv

print(f"Copying from {from_file} to {to_file}")

(open(to_file, 'w', closefd=True)).write((open(from_file, closefd = True)).read())

