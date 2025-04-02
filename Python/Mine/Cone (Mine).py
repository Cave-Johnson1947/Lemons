import math

r = float(input("Enter the radius of the cone: "))
h = float(input("Enter the height of the cone: "))

volume = (math.pow(r, 2) * h * math.pi) / 3

print("The volume of the cone is:", round(volume, 2), "cubic units")