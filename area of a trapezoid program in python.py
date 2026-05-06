# Area of a trapezoid
# This program asks the user for the values of base1, base2 and the height.
# It then calculates and displays the area.
# Recreated for standard Python by Wissal Jabaoui

print("Let's calculate the area of a trapezoid!")

# Get user input for the dimensions
base1 = float(input("What is the length of base1 in (cm)? "))
base2 = float(input("What is the length of base2 in (cm)? "))
height = float(input("What is the height in (cm)? "))

# Calculate the area
# Formula: Area = (base1 + base2) / 2 * height
area = (base1 + base2) / 2 * height

# Display the result
print("The area of a trapezoid is: " + str(area))
