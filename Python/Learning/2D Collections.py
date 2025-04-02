["apple", "banana", "cherry"]
["celery", "beet", "carrot"]
["chicken", "beef", "pork"]

grocery_list = [["apple", "banana", "cherry"], ["celery", "beet", "carrot"], ["chicken", "beef", "pork"]]

for collection in grocery_list:
    for food in collection:
        print(food, end=" ")
    print()