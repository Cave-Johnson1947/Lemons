tons_of_food = 0.07
num_people = 25

tons_of_food_per_person = tons_of_food / num_people
print(tons_of_food_per_person)

tons_taken = float(input("How many tons of food did you take? "))
if tons_taken == tons_of_food_per_person:
    print("Good job, you took the right amount of food!")
else:
    print("You took the wrong amount of food!")