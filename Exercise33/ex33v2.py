def print_zero_to_number(number, inc=1):
    i = 0
    numbers = []

    for i in range(0,number, inc):
        print(f"At the top i is {i}.")
        numbers.append(i)

        print("Numbers now: ", numbers)

        print(f"At the bottom i is {i}.")

    print("The numbers:")

    for num in numbers:
        print(num)

number = int(input("Give me a number >:"))
increment = int(input("And an increment >:"))
print_zero_to_number(number, increment)
