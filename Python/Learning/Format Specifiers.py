price1 = 3000.14159
price2 = -9870.65
price3 = 1200.34

print(f"Print 1 is ${price1:.1f}")
print(f"Print 2 is ${price2:.2f}")
print(f"Print 3 is ${price3:.3f}")


print(f"Print 1 is ${price1:10}")
print(f"Print 2 is ${price2:010}")
print(f"Print 3 is ${price3:^10}")
print(f"Print 3 is ${price3:<10}")
print(f"Print 3 is ${price3:>10}")

print(f"Print 1 is ${price1:+}")
print(f"Print 2 is ${price2:+}")
print(f"Print 3 is ${price3:+}")

print(f"Print 1 is ${price1: }")
print(f"Print 2 is ${price2:,}")
print(f"Print 3 is ${price3:,}")
