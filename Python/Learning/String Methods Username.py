username = input("Enter a username: ")

if len(username) > 12:
    print ("Your username cant be more than 12 characters")
elif not username.find(" ") == -1:
      print("No spaces")
elif not username.isalpha():
     print("No numbers")
else:
    print(f"Welcome {username}")
    