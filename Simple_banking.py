print("===================================================")
print("Welcome to saurav bank")
balance = 0.0
kyc_documents = {}

def check_balance():
    print("===================================================")

    print(f"your current balance is {balance} Rupees")

    print("===================================================")


def deposit(amount):
    global balance
    if amount > 0:
        balance += amount
        
    elif amount < 0:
        print("===================================================")
        
        print("Cannot deposit a negative or zero amount amount")

        print("===================================================")

def withdraw(amount):
    global balance
    if amount < 0:
        print("===================================================")

        print("Cannot withdraw a negative or zero amount amount")

        print("===================================================")
    elif amount > balance:
        print("===================================================")

        print(f"Cannot withdraw amount more than current balance : {balance} Rupess")

        print("===================================================")
    else:
        print("===================================================")

        balance -= amount
        

        print("===================================================")

def update_kyc(docs):
    global kyc_documents
    kyc_documents.update(docs)

def check_kyc():
    if len(kyc_documents == 0):
        print("kyc not done")
    else:
        for doc in kyc_documents:
            print(f"{doc} : {kyc_documents[doc]}")


while True:
    print("===================================================")
    print("1 check balance")
    print("2 Deposit an amount")
    print("3 Withdraw amount")
    print("4 check kyc" )
    print("5 Update kyc")
    print("6 exit")

    choice = input("Enter chocie (1 to 6): ")
    if choice == "1":
        check_balance()
        
    elif choice == "2":
        amt = float(input("Enter amount in rupees: "))
        deposit(amt)
        print(f"{amt} deposited sucessfully")

    elif choice == "3":
        amt = float(input("Enter amount to withdraw: "))
        withdraw(amt)
        print(f"{amt} withdrawn sucessfully")

    elif choice == "4":
        check_kyc()

    elif choice == "5":
        Kyc_docs = {}
        n_documents = int(input("Enter the number of dcouments you want to add: "))
        for i in range(n_documents):
            key = input("Enter the type of document: ")
            value = input("Enter the number of document: ")
            Kyc_docs[key] = value
        update_kyc(Kyc_docs)
        print(f"Kyc updated")

    elif choice == "6":
        print("Quitinf the application")
        break

    else:
        print("Pls enter valid input")

print()
 

print("Thank you")
