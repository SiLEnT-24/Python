#bank transactions

balance = 1000

while True:
    print("1 for current balance")
    print("2 for deposit amount")
    print("3 for withdraw amount")
    print("4 for exit")

    choice = int(input("Enter your choice: "))
    if choice == 1:
        print(f"Current balance: {balance}")

    elif choice == 2:
        deposit = int(input("Enter amount to deposit: "))
        balance += deposit
        print(f"Amount deposited: {deposit}")
        if balance >0:
            balance = balance
            print("Balance amount- ", balance)
        else:
            print("Insufficient balance")

    elif choice == 3:
        withdraw = int(input("Enter amount to withdraw: "))
        if withdraw <=0:
            print("Invalid balance")
        elif withdraw > balance:
            print("Insufficient balance")
        else:
            balance -= withdraw
            print(f"Amount withdrawn: {balance}")

    elif choice == 0:
        print("Thank you for using ATM ")
        break
    else:
        print("Invalid Choice")
            
