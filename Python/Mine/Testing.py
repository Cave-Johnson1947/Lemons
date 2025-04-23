numerator = int(input("Enter a numerator: "))
denominator = int(input("Enter denominator: "))

while int(numerator / denominator) * denominator == numerator:
    print("Divides evenly!")
else:
    print("Doesn't divide evenly.")