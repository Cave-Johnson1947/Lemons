response = input("would you like food ? (Y/N) ")

if response == "Y":
    print("Have some food")
else:
    print("NO food for you")


name = input("Enter your name: ")

if response == "":
    print("TYPE YOUR NAME")
else:
    print(f"Hello {name}")


for_sale = True

if for_sale:
    print("This is for sale")
else:
    print("This item is NOT for sale")