numbers = (1, 2, 3, 4, 5)

for number in numbers:
    print(number)

for number in reversed(numbers):
    print(number, end=" ")

fruits = {"apple", "orange", "banana", "coconut"}

for fruit in fruits:
    print(fruit)

name = "Jackson"

for character in name:
    print(character, end = " ")

print("  ")

my_dictionary = {"A":1,
                "B":2,
                "C":3}

for key, value in my_dictionary.items():
    print(f"{key} = {value}")
