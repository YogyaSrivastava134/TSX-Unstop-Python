# This script calculates the area and perimeter of a rectangle based on user input

# Ask the user to enter the length and convert it to a number (float)
length = float(input("Enter the length of the rectangle: "))

# Ask the user to enter the width and convert it to a number (float)
width = float(input("Enter the width of the rectangle: "))

# Calculate the area (length * width)
area = length * width

# Calculate the perimeter (2 * (length + width))
perimeter = 2 * (length + width)

# Print the results
print("Length:", length)
print("Width:", width)
print("Area of the rectangle:", area)
print("Perimeter of the rectangle:", perimeter)
