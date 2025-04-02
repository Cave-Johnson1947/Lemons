import random

cat_name = ["Whiskers", "Fluffy", "Mr. Whiskers", "Kitty", "Paws"]
cat_breed = ["Persian", "Maine Coon", "Siamese", "Ragdoll", "Bengal"]
cat_age = ["5", "12", "8", "10", "2"]

while True:
    name = random.choice(cat_name)
    breed = random.choice(cat_breed)
    age = random.choice(cat_age)

    print(f"Welcome {name}. Who is a {breed} cat and is {age} years old.")

    user_input = input("Would you like to see a new cat? (y for more, n to quit or a to adopt): ").lower()
    
    if user_input == "a":
        print(f"Thank you so much for adopting {name}. The {age} year old {breed} cat!")
        break
    if user_input == "n":
        print("Goodbye, hope you see a cat that you like!")
        break