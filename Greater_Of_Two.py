# This script compares two numbers entered by the user

# Take input from the user and convert to float
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Compare the numbers and print the result
if num1 > num2:
    print(f"The first number {num1} is greater than the second number {num2}")
elif num1 < num2:
    print(f"The first number {num1} is less than the second number {num2}")
else:
    print("Both numbers are equal.")
