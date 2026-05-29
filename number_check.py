# number_check.py
# Author: Gael Morales Hernandez
#
# Reads a float and classifies it as integer or decimal,
# positive, negative, or zero, and checks if it falls between 0 and 100.

print("Enter a number:")
num = float(input())

def num_type(n):
    if n.is_integer():
        print("The number is an integer")
    else:
        print("The number is a decimal")

    if n > 0:
        print("The number is positive")
    elif n < 0:
        print("The number is negative")
    else:
        print("The number is zero")

    if 0 <= n <= 100:
        print("The number is between 0 and 100")
    else:
        print("The number is not between 0 and 100")

num_type(num)
