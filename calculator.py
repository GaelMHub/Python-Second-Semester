# calculator.py
# Author: Gael Morales Hernandez
#
# Basic calculator using match-case (Python 3.10+).
# Reads two numbers and an operator, then prints the result.

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
operator = input("Enter an operator (+, -, *, /): ")

match operator:
    case "+":
        result = num1 + num2
        print(f"Result: {result:.2f}")

    case "-":
        result = num1 - num2
        print(f"Result: {result:.2f}")

    case "*":
        result = num1 * num2
        print(f"Result: {result:.2f}")

    case "/":
        if num2 == 0:
            print("Error: Cannot divide by zero.")
        else:
            result = num1 / num2
            print(f"Result: {result:.2f}")

    case _:
        print("Error: Invalid operator.")
