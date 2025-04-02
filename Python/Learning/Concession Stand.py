import random

menu = {
    "pizza": 3.00,
    "nachos": 4.50,
    "popcorn": 6.00,
    "fries": 2.50,
    "chips": 1.00,
    "pretzel": 3.50,
    "soda": 3.00,
    "lemonade": 4.25,
}
cart = []
total = 0

print("--------MENU--------")
for key, value in menu.items():
    print(f"{key:10}: ${value:.2f}")
print("--------------------")

while True:
    food = input("What would you like to order? (q to quit): ").lower()
    if food == "q":
        break
    elif menu.get(food) is not None:
        if random.choice([True, False]):  # Randomly decide if the item is in stock
            cart.append(food)
            print(f"Added {food} to your cart.")
        else:
            print(f"Sorry, we don't have {food} in stock right now.")
    else:
        print(f"Sorry, {food} is not on the menu.")

print("-----YOUR ORDER-----")
for food in cart:
    total += menu.get(food)
    print(food, end=" ")

print(f"\nTotal is: ${total:.2f}")