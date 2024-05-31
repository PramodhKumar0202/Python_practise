def show_balance():
    print(f"your balance is ${balance:.2f}")

def deposit():
    amount =float(input("enter amount to be deposited: "))

    if amount < 0:
        print("please enter valid amount")
        return 0
    else:
        return amount
 
def withdraw():
    amount =float (input("enter amount to be withdrawn:"))

    if amount > balance :
        print("insuffient balance")
    elif  amount < 0:
        print("amount must be greater than 0 ")
        return 0
    else:
        return amount  
    

   
balance =0
is_running =True

while is_running:
    #print("banking program")
    print("1.show_balance")
    print("2.deposit")
    print("3.withdraw")
    print("4.Exit")
  

    choice = input("enter your choice (1-4) : ")
    if choice == '1':
        show_balance()
        #print("")
    elif choice == '2':
        balance += deposit()
        #print("")
    elif choice == '3':
        balance-= withdraw()
       # print("")
    elif choice =='4':
        is_running = False
    else:
        print("that is not a valid choice") 

print("thank you") 





    