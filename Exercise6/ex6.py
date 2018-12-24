# this is not 10, it is the binary 2.
types_of_people = 10
# This shows one way to make a string variable using an f string.
# The f is needed because of the embedded variable.
# Here the int is converted to a string and that string is put inside a string (#1)
x = f"There are {types_of_people} types of people."

# but here you can just use quotes for a string variable, because there is not variable embedded.
binary = "binary"
# notice that the single quote is escaped without an escape character.
do_not = "don't"
# No problem with the single quote in the f string either.
# strings inside string #2
y = f"Those who know {binary} and those who {do_not}"

# To print a string variable, f string or not, just put the variable in the print parenthesis.
print(x)
print(y)

# f string in an f sting is not a problem.
# string inside a string #3
print(f"I said: {x}")
# the quotes in the quotes are escaped, like before.
# string inside a string #4
print(f"I also said: '{y}'")

# bool variable.
hilarious = False
# The empty braces are where the .format variable will go.
joke_evaluation = "Isn't that joke so funny?! {}"

# Here the .format tells what to put in the empty braces in the string variable.
# the boolean is converted to a string and then inserted, just like the int.
# string inside a string #5
print(joke_evaluation.format(hilarious))

# basic strings
w = "This is the left side of ..."
e = "a string with a right side."

# can be concatinated with a plus.
print(w + e)

