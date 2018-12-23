# this line prints these words
print("I will now count my chickens:")

# This line says there are 30.0 hens because 25 + (5.0) = 30.0, so this division must a float operation.  This means that Python is converting these to float.
print("Hens", 25. + 30. / 6.)
# This line says there are 97 roosters, an integer.  That must mean that % is mod.  100 - 75%4 = 100 - 3 = 97, an integer. (75/4 = 18.75, but 75//4 = 18 and so 75%4=3)
print("Roosters", 100. - 25. * 3. % 4.)

# Print these words
print("Now I will count the eggs:")

# This does (3+2+1-5)+(4%2) - (1/4) + 6 = 1 + 0 -.25 +6 = 6.75
print(3. + 2. + 1. - 5. + 4. % 2. - 1. / 4. + 6.)

# 5 < -2 is False
print("Is it true that 3 + 2 < 5 - 7?")

# False
print(3. + 2. < 5. - 7.)

# 5
print("What is 3 + 2?", 3. + 2.)
#-2
print("What is 5 - 7?", 5. - 7.)

# print these words.
print("Oh, that's why it's False.")

# Bad grammer.  need ?
print("How about some more.")

# True
print("Is it greater?", 5. > -2.)
# True
print("Is it greater or equal?", 5. >= -2.)
#False
print("Is it less than or equal?", 5. <= -2.)
