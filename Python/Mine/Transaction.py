balance = 1000

while True:
    transaction = input("Enter transaction type d for deposit, w for withdrawal or q for quit to exit: ").lower()
    
    if transaction == 'q':
        print(f"Final balance: {balance}")
        break
        
    if transaction not in ['d', 'w']:  # Check for single letters since input uses d/w/q
        print("Invalid transaction")
        continue
        
    amount = int(input("Enter the amount: "))
    
    if transaction == "d":    
        balance = balance + amount
        print(f"New balance: {balance}")
    elif transaction == "w":  
        if amount > balance:
            print("You cannot have a negative balance!")
        else:
            balance = balance - amount
            print(f"New balance: {balance}")