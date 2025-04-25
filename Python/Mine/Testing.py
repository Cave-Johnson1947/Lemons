def quiz():
    print("Welcome to the 1800s Cost Quiz!")
    print("Answer the following questions to find out how much you would have cost in the 1800s.")
    
    age = int(input("How old are you? "))
    occupation = input("What is your occupation (farmer, blacksmith, teacher, etc.)? ").lower()
    skills = input("Do you have any special skills (yes/no)? ").lower()

    cost = 0

    if age < 18:
        cost += 5  # Young people were cheaper
    elif age < 40:
        cost += 20  # Adults in their prime
    else:
        cost += 15  # Older adults

    if occupation == "farmer":
        cost += 25
    elif occupation == "blacksmith":
        cost += 30
    elif occupation == "teacher":
        cost += 35
    else:
        cost += 20  # Other occupations

    if skills == "yes":
        cost += 10  # Extra for special skills

    print(f"You would have cost approximately {cost} dollars in the 1800s!")

quiz()