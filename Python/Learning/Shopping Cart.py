item = input("what item are you buying?: ")
price = float(input("what is the price?: "))
quantity = int(input("how many?: "))

item2 = input("what item are you buying?: ")
price2 = float(input("what is the price?: "))
quantity2 = int(input("how many?: "))

item3 = input("what item are you buying?: ")
price3 = float(input("what is the price?: "))
quantity3 = int(input("how many?: "))

total = price * quantity + price2 * quantity2 + price3 * quantity3

print(f"you have bought {quantity} {item}, {quantity2} {item2}, {quantity3} {item3}")
print(f"your total is: ${round(total, 2)}")
