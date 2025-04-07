import math

# Ask user for the radius of the circle
radius = float(input("Enter the radius of the circle: "))

# Calculate area and circumference
area = math.pi * radius ** 2
circumference = 2 * math.pi * radius

# Display the results
print(f"Area: {round(area, 2)}")
print(f"Circumference: {round(circumference, 2)}")
print("\nCircle Area Formula:")
print("Area = πr²")
print("\nCircle Circumference Formula:")
print("Perimeter = 2 * π * r")