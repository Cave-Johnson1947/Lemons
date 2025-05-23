import time
menu = ["Banana", "Carrot", "Blueberries", "Rice", "Cheese", "Gay Beans",]
reservation_times = ["7:00", "7:30", "8:00", "4:29",]
specials = ["Lobster Bisque", "Truffle Mac and Cheese", "Stuffed Mushrooms"]

def print_menu():
    print("Here is the menu:")
    for item in menu:
        print(f"{item}")

        
def ask_specials():
    print("Today's specials are:")
    for item in specials:
        print(f"{item}")


def make_reservation():
    print("Here are the available reservation times:")
    for time in reservation_times:
        print(f"{time}")
    while True:
        reservation_time = input("Please enter your desired reservation time: ")
        if reservation_time in reservation_times:
            reservation_times.remove(reservation_time)
            print(f"Your reservation for {reservation_time} has been confirmed.")
            break
        else:
            print("Sorry, that time is not available. Please choose another time.")


def order_takeout():
    print("Here is the menu for takeout:")
    time.sleep(1)
    for item in menu:
        print(f"{item}")

    order_list = []

    while True:
        choice = input("Please enter the item you would like to order (or 'done' to finish): ")

        if choice.lower() == "done":
            break
        elif choice in menu:
            order_list.append(choice)
            print(f"{choice} has been added to your order.")
        else:
            print("Sorry, that item is not on the menu. Please choose another item.")

    if order_list:
        print("Your order has been placed! You ordered:")
        for item in order_list:
            print(f"{item}")
    else:
        print("You didn't order anything.")
        
    print("Thank you! Your food will be ready in 30 minutes.")

    


def exit_program():
    print("Thank you for visiting Jackson's Pizzeria!")
    print("Have a great day!")
    exit()


def print_options():
    print("Welcome to Jackson's Pizzeria!")
    time.sleep(0.5)
    print("How can I help you?")
    time.sleep(0.5)
    print("1. Take a look at the menu.")
    time.sleep(0.5)
    print("2. Ask about daily specials.")
    time.sleep(0.5)
    print("3. Make a reservation.")
    time.sleep(0.5)
    print("4. Order take out.")
    time.sleep(0.5) 
    print("5. Exit.")

    option = input("Please enter a number from 1 to 5: ")

    if option == "1":
        print_menu()
    elif option == "2":
        ask_specials()
    elif option == "3":
        make_reservation()
    elif option == "4":
        order_takeout()
    elif option == "5":
        exit_program()
    else:
        print("Invalid option. Please try again.")

    print("Returning to main menu in 5 seconds...")
    time.sleep(5)

def run_chatbot():
    while True:
        print_options()

run_chatbot()