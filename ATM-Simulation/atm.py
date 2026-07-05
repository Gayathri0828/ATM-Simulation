balance=5000
pin=int(input("enter ypur ATM pin: "))
if pin == 1234:
    while True:
        print("Welcome to ATM")
        print("_____ATM MENU____")
        print("1.Check Balance")
        print("2.Deposit")
        print("3.Withdraw")
        print("4.exit")
        choice=int(input("enter your choice: "))
        if choice == 1:
            print("Your balance is ",balance)
        if choice == 2:
            amount=int(input("enter your amount to deposit: "))
            balance=balance+amount
            print("Now total balance is ",balance)
        if choice==3:
            withdraw = int(input("enter amount to withdraw: "))
            if balance >= withdraw:
                balance=balance-withdraw
                print("Now total balance is ",balance)
            else:
                print("Insufficient balance")
        if choice == 4:
            print("Thank you for using our ATM!")
            break
else:
    print("Invalid pin")
