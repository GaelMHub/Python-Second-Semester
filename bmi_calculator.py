# bmi_calculator.py
# Author: Gael Morales Hernandez
#
# Calculates BMI based on user input (weight, height, sex).
# Uses sex-specific thresholds to provide a diagnosis.
# Validates all inputs before processing.


def male_bmi(weight, height):
    """Calculate and diagnose BMI using male thresholds."""
    bmi = weight / (height * height)
    print(f"BMI: {bmi:.2f}")

    if bmi < 20:
        print("Diagnosis: Underweight")
    elif bmi < 25:
        print("Diagnosis: Normal weight")
    elif bmi < 30:
        print("Diagnosis: Overweight")
    elif bmi < 40:
        print("Diagnosis: Obese")
    else:
        print("Diagnosis: Severely obese")


def female_bmi(weight, height):
    """Calculate and diagnose BMI using female thresholds."""
    bmi = weight / (height * height)
    print(f"BMI: {bmi:.2f}")

    if bmi < 19:
        print("Diagnosis: Underweight")
    elif bmi < 23:
        print("Diagnosis: Normal weight")
    elif bmi < 27:
        print("Diagnosis: Overweight")
    elif bmi < 32:
        print("Diagnosis: Obese")
    else:
        print("Diagnosis: Severely obese")


def main():
    name = input("Enter your name: ")

    while True:
        age = int(input("Enter your age: "))
        if 1 <= age <= 120:
            break

    while True:
        height = float(input("Enter your height in meters: "))
        if 0.50 <= height <= 2.50:
            break

    while True:
        weight = float(input("Enter your weight in kilograms: "))
        if 20 <= weight <= 300:
            break

    print("\nSelect your sex:")
    print("1. Male")
    print("2. Female")
    sex = int(input())

    import os
    os.system("cls" if os.name == "nt" else "clear")

    print("========================================")
    print("         BMI DIAGNOSTIC REPORT")
    print("========================================")
    print(f"Patient : {name}")
    print(f"Age     : {age} years")
    print(f"Weight  : {weight:.2f} kg")
    print(f"Height  : {height:.2f} m")
    print("\nRESULTS:")

    if sex == 1:
        male_bmi(weight, height)
    elif sex == 2:
        female_bmi(weight, height)
    else:
        print("Invalid sex option.")

    print("========================================")


if __name__ == "__main__":
    main()
