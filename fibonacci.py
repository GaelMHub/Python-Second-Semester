# fibonacci.py
# Author: Gael Morales Hernandez
#
# Reads the number of iterations from the user and prints
# the Fibonacci sequence up to that many terms.

# Ask the user for the number of iterations
times = int(input("Enter the number of iterations: "))

# Validate that the number is greater than 0
if times <= 0:
    # Error message if the number is 0 or negative
    print("Please enter a positive integer greater than 0.")
else:
    # Initial values of the Fibonacci sequence
    a = 0
    b = 1

    # Loop that runs the indicated number of times
    for i in range(times):
        # Print the current value of 'a'
        print(a, end=" ")
        
        # Calculate the next number in the sequence
        c = a + b
        
        # Update the values for the next iteration
        a = b
        b = c
