name = input("Enter your name: ")

while name == "":
    print("You did not put in a name")
    name = input("Enter your name: ")

print(f"Hello {name}")

age = int(input("Enter your age: "))

while age < 0:
    print("Age can't be negative")
    age = int(input("Enter your age: "))

print(f"You are {age} years old")

food = input("Enter a food (q to quit): ")

while not food == "q":
    print(f"You like {food}")
    food = input("Enter a new food (q to quit): ")

print("Bye")

num = int(input("Enter a # between 1 - 10: "))

while num < 1 or num > 10:
    print(f"{num} is not valid")
    num = int(input("Enter a # between 1 - 10: "))

print(f"Your number is {num}")