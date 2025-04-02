import random

low = 1
high = 100
guesses = 0
number = random.randint(low, high)
#number = random.randint(1, 20) 
#number = random.randint(low, high) 
#number = random.random() 
#option = random.choice(options) 
#random.shuffle(cards)

while True:
    guess = int(input(f"Enter a number between {low} and {high}: "))
    guesses += 1

    if guess < number:
        print(f"{guess} is too low.")
    elif guess > number:
        print(f"{guess} is too high.")
    else:
        print(f"Congratulations! {guess} is the correct number.")
        break

print(f"It took you {guesses} guesses.")