age = int(input("enter age: "))

if age >= 100:
    print("you are too old to sign up")
elif age >= 18:
    print("You are signed up")
elif age < 0:
    print("You haven't been born yet")
else: 
    print("You must be 18+ to sign up")
