# How to calculate area of traingle
# import math

# a = int(input("Enter 1st side:")) 
# b = int(input("Enter 2nd side:"))
# c = int(input("Enter 3rd side:"))

# s = (a + b + c) / 2     #this is semi parameter means half of sides

# area = math.sqrt(s*(s - a)*(s - b)*(s - c))
# print("Area of triangle is", area)




#simple intrest

# principal = float(input("Enter principal amount: "))
# Rate = float(input("Enter rate amount: "))
# Time = float(input("Enter Time in years: "))

# Simple_Intrest = (principal*Rate*Time)/100


# print("Simple intrest is: ", Simple_Intrest)




#Compound Intrest:

# principal = float(input("Enter principal amount: "))
# Rate = float(input("Enter rate amount: "))
# Time = float(input("Enter Time in years: "))

# Amount = principal * (1 + Rate/100) ** Time
# # or
# Amount = principal * pow((1 + Rate/100),Time)
# print(round(Amount,2))
# CI = Amount - principal
# print("Compund intrest is : ", round(CI))



#To check highest value from a list using a for loop and yes using max function we can directly get it
# scores = [10,25,46,5,6,78,45,4,6,0]
# highest = scores[0]
# for score in scores:
#     if highest < score:
#         highest = score

# print(f"Hihest score is {highest}")



# Write a Python program that:

# Stores student names and their marks in a dictionary.

# Uses a for loop and continue statement.

# Prints only those students who scored 35 or more marks.

# ✅ Correct Code (Paste Ready)
# # Dictionary storing student names and their marks
# scores = {
#     "Saurav": 10,
#     "Tarun": 40,
#     "Hemu": 80,
#     "Vicky": 25
# }

# # Loop through dictionary
# for name, marks in scores.items():
#     if marks < 35:
#         continue
#     print(f"{name} scored {marks}")

# ✅ Output
# Tarun scored 40
# Hemu scored 80



#infinite loop for correct password:
# Correct_password = "python"
# while True:
#     user_pass = input("Enter Password: ")
#     if Correct_password == user_pass:
#         print("Correct password!")
#         break
#     else:
#         print("Try again")

# print("logged in")


#using while loop print numbers from 10 to 20 even numbers

# num = 10
# while num <= 20:
#     print(num)
#     num += 2

#using while loop to print numbers from 20 to 10 even numbers

# num = 20
# while num >= 10:
#     print(num)
#     num = num - 2
    



#Roll a dice game
# import random
# while True:
#     choice = input("Press 'Enter' to play game or 'q' to exit: ")
#     choice = choice.strip()
#     choice = choice.lower()
#     if choice == "q":
#         print("Thank you for playing")
#         break
#     elif choice == "":
#         number = random.randint(1,6)
#         print("Your number is",number)
#     else:
#         print("Please enter valid input")




#Count countries starting with letter "i"
# counter = 0
# countries = ["India","Ireland","Australia","Sri_lanka","Iceland","Poland"]
# for country in countries:
#     if country[0].lower() == "i":
#         counter += 1

# print(counter)





# #Count countries name startswith i from the list and print the list
# counter = 0
# data = []
# countries = ["India","Ireland","Australia","Sri_lanka","Iceland","Poland","Indiana","Italy"]
# for country in countries:
#     country = country.lower()
#     if country.startswith("i"):
#         data.append(country)
#         counter += 1
# print(counter)
# print(data)




# users = {
#     "username":"myuser",
#     "password":"test@123",
#     "email":"username.com@gmail.com",
#     "address":"nebula tower sindhi gali"
# }

# sensitive_info = ["password","address"]

# for name in list(users):
#     if name in sensitive_info:
#         print(f"Key:{name},value:{users[name]}")
#         users.pop(name)
# print(users)
        
# # #         #or

# # # # for i in sensitive_info:
# # # #     users.pop(i)

# # # # print(users)


#same que as above but to tell if key that need to be deleted from sensitive info if it is not
#present in dictionary then how to tackle tht error
# users = {
#     "username":"myuser",
#     "password":"test@123",
#     "email":"username.com@gmail.com",
#     "address":"nebula tower sindhi gali"
# }

# sensitive_info = ["password","address","phone"]

# for i in sensitive_info:
#     if i in users:
#         print(f"Deleted key {i} and value {users[i]}")
#         users.pop(i)
#     else:
#         print(f"{i} not present in users")

    
# print(users)



# '''
# Number guessing game
# '''    
# import random
# attempts = 10
# num = 1
# secret_number = random.randint(1,50)
# print(f"Welcome to number guessing game")
# print(f"The secret number is between 1 and 50")
# is_guess_correct = False
# while num <= 10:
#     print(f"You have {attempts} attempts remaining")
#     number = int(input("Enter your guess for secret number which is between 1 and 50: "))
#     if number == secret_number:
#         print(f"Congrats your guess is correct")
#         is_guess_correct = True
#         break
#     else:
#         if number < secret_number:
#             print("Guess a higher number")
#         elif number > secret_number:
#             print("Guess a lower number")
#     attempts -= 1
#     num += 1
# if not is_guess_correct:
#     print("Bad luck your all attempts exhausted")
# print(f"The correct number was {secret_number}")

#or


# import random
# attempts = 10
# print("Welcome to the dice roll game")
# secret_number = random.randint(1,50)
# num = 1
# if_guess_correct = False
# while num <= 10:
#     print(f"You have {attempts} attemps remaining")
#     number = int(input("Enter your guess between 1 to 50: "))
#     if number == secret_number:
#         print(f"Your guess is correct")
#         if_guess_correct = True
#         break
#     else:
#         if number < secret_number:
#             print("Guess higher")
#         elif number > secret_number:
#             print("Guess lower")
#     attempts -= 1
#     num += 1
# if not if_guess_correct :
#     print("Bad luck Your attemptes got exhausted") 
# else:
#     print(f"the correct number was {secret_number} ")


# def calculate_total(*prices):
#     total = 0
#     for price in prices:
#         total += price
#     return total

# print(calculate_total(100,200,300,400)) 

# def details_of_students(**details):
#     print(details)

# details_of_students(name = "saurav",age = 20)


# def create_user(**data):
#     for key, value in data.items():
#         print(f"{key} : {value}")

# create_user(name="Saurav", email="abc@gmail.com", role="admin")


# def create_user(**data):
#     for key,value in data.items():
#         print(f"{key} : {value}")

# create_user(name = "Saurav",age = 20,gmail = "saurav@gmail.com")


# def add(a,b):
#     return a + b

# def sub(a,b):
#     return a - b

# def calculator(operation,x,y):
#     return operation(x,y)

# print(calculator(add,5,5))
# print(calculator(sub,10,5))



#simple banking applcation
# print("===================================================")
# print("Welcome to saurav bank")
# balance = 0.0
# def check_balance():
#     print("===================================================")

#     print(f"your current balance is {balance} Rupees")

#     print("===================================================")


# def deposit(amount):
#     global balance
#     if amount > 0:
#         balance += amount
#     elif amount < 0:
#         print("===================================================")
        
#         print("Cannot deposit a negative or zero amount amount")

#         print("===================================================")

# def withdraw(amount):
#     global balance
#     if amount < 0:
#         print("===================================================")

#         print("Cannot withdraw a negative or zero amount amount")

#         print("===================================================")
#     elif amount > balance:
#         print("===================================================")

#         print(f"Cannot withdraw amount more than current balance : {balance} Rupess")

#         print("===================================================")
#     else:
#         print("===================================================")

#         balance -= amount

#         print("===================================================")

# while True:
#     print("===================================================")
#     print("1. check balance")
#     print("2 .Deposit an amount")
#     print("3 Withdraw amount")
#     print("4 exit")

#     choice = input("Enter chocie: ")
#     if choice == "1":
#         check_balance()
#     elif choice == "2":
#         amt = float(input("Enter amount in rupees: "))
#         deposit(amt)
#     elif choice == "3":
#         amt = float(input("Enter amount to withdraw: "))
#         withdraw(amt)
#     elif choice == "4":
#         break

#     else:
#         print("Pls enter valid input")

# print()
 

# print("Thank you")


# print("===================================================")
# print("Welcome to saurav bank")
# balance = 0.0
# kyc_documents = {}

# def check_balance():
#     print("===================================================")

#     print(f"your current balance is {balance} Rupees")

#     print("===================================================")


# def deposit(amount):
#     global balance
#     if amount > 0:
#         balance += amount
        
#     elif amount < 0:
#         print("===================================================")
        
#         print("Cannot deposit a negative or zero amount amount")

#         print("===================================================")

# def withdraw(amount):
#     global balance
#     if amount < 0:
#         print("===================================================")

#         print("Cannot withdraw a negative or zero amount amount")

#         print("===================================================")
#     elif amount > balance:
#         print("===================================================")

#         print(f"Cannot withdraw amount more than current balance : {balance} Rupess")

#         print("===================================================")
#     else:
#         print("===================================================")

#         balance -= amount
        

#         print("===================================================")

# def update_kyc(docs):
#     global kyc_documents
#     kyc_documents.update(docs)

# def check_kyc():
#     if len(kyc_documents) == 0:
#         print("kyc not done")
#     else:
#         for doc in kyc_documents:
#             print(f"{doc} : {kyc_documents[doc]}")


# while True:
#     print("===================================================")
#     print("1 check balance")
#     print("2 Deposit an amount")
#     print("3 Withdraw amount")
#     print("4 check kyc" )
#     print("5 Update kyc")
#     print("6 exit")

#     choice = input("Enter chocie (1 to 6): ")
#     if choice == "1":
#         check_balance()
        
#     elif choice == "2":
#         amt = float(input("Enter amount in rupees: "))
#         deposit(amt)
#         print(f"{amt} deposited sucessfully")

#     elif choice == "3":
#         amt = float(input("Enter amount to withdraw: "))
#         withdraw(amt)
#         print(f"{amt} withdrawn sucessfully")

#     elif choice == "4":
#         check_kyc()

#     elif choice == "5":
#         Kyc_docs = {}
#         n_documents = int(input("Enter the number of dcouments you want to add: "))
#         for i in range(n_documents):
#             key = input("Enter the type of document: ")
#             value = input("Enter the number of document: ")
#             Kyc_docs[key] = value
#         update_kyc(Kyc_docs)
#         print(f"Kyc updated")

#     elif choice == "6":
#         print("Quiting the application")
#         break

#     else:
#         print("Pls enter valid input")

# print()
 

# print("Thank you")




    

