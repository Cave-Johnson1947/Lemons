import math

ingredient1 = input("Enter 1st ingredient: ")
amount1 = float(input("Enter the amount of the 1st ingredient: "))

ingredient2 = input("Enter 2nd ingredient: ")
amount2 = float(input("Enter the amount of the 2nd ingredient: "))

ingredient3 = input("Enter 3rd ingredient: ")
amount3 = float(input("Enter the amount of the 3rd ingredient: "))

servings = int(input("How many servings: "))
ingredientS1 = amount1 * servings
ingredientS2 = amount2 * servings
ingredientS3 = amount3 * servings

print(f"The total amount of {ingredient1} is {ingredientS1}")
print(f"The total amount of {ingredient2} is {ingredientS2}")
print(f"The total amount of {ingredient3} is {ingredientS3}")