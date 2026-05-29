# number_compare.py
# Author: Gael Morales Hernandez
#
# Reads three integers and compares each pair,
# printing whether each is greater, lesser, or equal.

number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))
number3 = int(input("Enter the third number: "))

# Comparison of number 1 with number 2
if number1 > number2:
    print(f"{number1} is greater than {number2}")
elif number1 < number2:
    print(f"{number1} is less than {number2}")
else:
    print(f"{number1} is equal to {number2}")

# Comparison of number 1 with number 3
if number1 > number3:
    print(f"{number1} is greater than {number3}")
elif number1 < number3:
    print(f"{number1} is less than {number3}")
else:
    print(f"{number1} is equal to {number3}")

# Comparison of number 2 with number 3
if number2 > number3:
    print(f"{number2} is greater than {number3}")
elif number2 < number3:
    print(f"{number2} is less than {number3}")
else:
    print(f"{number2} is equal to {number3}")
