player1 = int(input("Enter cards for Player 1: "))  

player2 = int(input("Enter cards for Player 2: "))  

if player1 > player2:
    print("Player 1 wins!")
    print("Thank you for playing!")
elif player1 < player2:
    print("Player 2 wins!")
    print("Thank you for playing!")
elif player1 == player2:
    print("It's a tie!")
    print("Thank you for playing!")