age = int(input("Age: "))
born = input("Born in the U.S.? (Yes/No): ").lower()
years_of_residency = int(input("Years of residency: "))

if age >= 35 and born == "yes" and years_of_residency >= 14:
    print("You are eligible to run for president!")
else:
    print("You are not eligible to run for president.")
    if age < 35:
        print("You are too young. You must be at least 35 years old.")
    if born != "yes":
        print("You must be born in the U.S. to run for president.")
    if years_of_residency < 14:
        print("You have not been a resident for long enough.")