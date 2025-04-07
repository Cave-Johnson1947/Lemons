age = int(input("Age: "))
born = input("Born in the U.S.? (Yes/No): ").lower()
years_of_residency = int(input("Years of residency: "))

if age >= 35 and born == "yes" and years_of_residency >= 14:
    print("You are eligible to run for president!")
else:
    print("You are not eligible to run for president.")