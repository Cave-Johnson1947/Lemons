import math

a = float(input("Thickness: "))

z = float(input("radius: "))

total = (math.pi * pow(z, 2) * a)

print(f"{round(total, 2)} cubic units")

s = float(input("How many slices in the pizza: "))

c = (total / s) 

print(f"{round(c, 2)} cubic units for each slice")