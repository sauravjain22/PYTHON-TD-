# name = "python"
# name = "j" + name[1:]
# print(name)

# language = "Python"
# version = 3.13

# version = str(version)

# print(language + version)

# age = 25
# print("Age is " ,age)

# entered_password = input("Enter password: ")
# saved_password = "admin123"

# if (saved_password == entered_password):
#     print("Password matched")

# else:
#     print("Didnt match")


# print("saurav","jain" ,sep="")


# numbers  = [1,2,3,4]
# for x in numbers:
#     print((map(numbers,x**2)))
    

# print("Hello everyone this is day 50 of learning")


# import math

# a = int(input("Enter 1st side:")) 
# b = int(input("Enter 2nd side:"))
# c = int(input("Enter 3rd side:"))

# s = (a + b + c) / 2

# area = math.sqrt(s*(s - a)*(s - b)*(s - c))
# print("Area of triangle is", area)



# text = "corporate@example.com"

# username = text[:9]
# domain = text[10:]

# print(username)
# print(domain)


# city = "new delhi"

# print(city.capitalize())
# print(city.title())

# words = ["Python", "is", "powerful"]

# sentence = " ".join(words)
# print(sentence)

# name = "Saurabh jain"
# age = "22"
# message = "Welcome abroad dear"

# s1 = 'string'
# s2 = "string"
# s3 = """
# This is multi line comment"""

# name  = "Saurav"
# print(name[2])

# text = "corporate@gmail.com"
# username = text[:9]
# mail = text[10:]
# print(username)
# print(mail)

# name = "Saurav"
# name[0] = "u"
# print(name)

# classroom = "tenth"
# Division = "JISKO"
# print(classroom.upper())
# print(Division.lower())

# city = "mumbai meri jaan"
# print(city.capitalize())
# print(city.title())

# email = "  Sauravatplay@gmail.com  "
# clean_email = email.lstrip()
# print(clean_email)
# print(email)

# message = "Hello user"
# updated_message = message.replace("user","Saurav")
# print(updated_message)

# email = "Sauravjain@"
# print(email.find("a"))
# print(email.index("@"))

# tune = "one one one two one"
# print(tune.count("one"))

# file_name = "jain.pdf"
# print(file_name.endswith(".pdf"))
# print(file_name.startswith("eai"))

# data = "saurav,vicky,lokesh"
# final_data = data.split(",")
# print(final_data)

# words = ["Python", "is" , "powerful"]
# sentence = " ".join(words)
# print(sentence)

# user_name = "sauravjain44"
# print(user_name.isalnum())
# print(user_name.isdigit())
# print(user_name.isalpha())

# password = "sauravjain440"
# if len(password) >= 6:
#     print("Strong pass")
# else:
#     print("Weak pass")


# name = input("Enter your name : ").strip().title()
# mail = input("Enter mail :").strip().lower()

# if "@" in mail and mail.endswith(".com"):
#     print("Registration successful")

# else:
#     print("Invalid email")


# name = "Saurav"
# age = 22
# print(f"I am {name},and i am {age} years old")

# Employee = "Saurabh jain"
# Salary = 200000
# Bonus = 5000
# Final_salary = Salary + Bonus

# print(f"The Employee name for most eligible at google is {Employee}")
# print(f"The salary of {Employee} is {Salary}")
# print(f"The diwali bonus is {Bonus}")
# print(f"So total salalry is {Final_salary}")

# number1 = 5
# number2 = 10

# print(f"The addition for two numbers is {number1 + number2}")
# print(f"The multiplication for two numbers is {number1*number2}")


# from datetime import datetime

# now = datetime.now()

# print(f"Report generated on: {now:%d-%m-%Y %H:%M:%S}")

# from datetime import datetime
# now = datetime.now()
# print()

# marks = 80
# print(f"Result {'Pass' if marks >= 70 else 'Fail'}")


# print("Hello\nWorld")

# print("Item\tQuantity\tprice")
# print("Pipe\t10\t100")

# print("Item\tQty\tPrice")
# print("Pipe\t10\t320")


# name = [1,2,3,4]
# print(2 in name)

# dictionary = {
#     "name":"Saurav",
#     "Age":20
# }

# print("name" in dictionary)

# dictionary = {
#     "name":"Saurav",
#     "Age":20
# }

# # print("Saurav" in dictionary)

# dictionary = {
#     "name":"Saurav",
#     "Age":20
# }

# print("Saurav" in dictionary.values())

# name  = "Python is fun everyone should learn it"
# print("fun" not in name)

# a = input("Enter hobby: ").lower()
# b = input("Enter hobby: ").lower()
# if a == b:
#         print("You got matched")
# else:
#         print("Not matched")


# text = "I love python programming"
# text = text.replace("love","live")
# print(text)

# text = "My nume is saurav jain"
# print(text.replace("nume","name"))

# count = "i got punishment to type python thousand times puthon puthon puthon"
# print(count.replace("puthon","python"))

# marks = [60, 70, 80]
# marks[1] = 75
# print(marks)

# orders = ["order1","order2","order3"]
# orders.append("order4")
# print(orders)

# old_users = ["Aman","Rahul"]
# # new_users = ["Saurabh","Tarun"]
# # old_users.extend(new_users)
# # print(old_users)

# # old_users = []

# old_users.insert(1,"Tarun")
# print(old_users)

# prices = ["500","800","640","825"]
# prices.sort()
# print(prices)

# days = ["Mon", "Tue", "Wed"]
# days.reverse()
# print(days)


# original = [1,2,3]
# backup = original.copy()
# backup.append(4)
# print(original)
# print(backup)

# numbers = [1,2,3,4,5]
# sqaures = []

# for n in numbers:
#     sqaures.append(n*n)

# print(sqaures)

# shift = ["Day", "Night"]

# weekly_schedule = shift * 3
# print(weekly_schedule)


# data = ["a","b","c","d","a","a"]
# # data = [x for x in data if x!="a"]
# # print(data)
# while "a" in data:
#     data.remove("a")
# print(data)

# nums = [1,2,54,6,78,89,7]
# nums.sort(reverse=True)
# print(nums)


# name = [[10,20],[20,30]]
# print(name[1][1])

# a = 1,2,3,4
# print(type(a))


# student1 = (1,2,3,4)
# student2 = (5,6,7,8)
# students = student1 + student2
# print(students)

# marks = 20,30,40,50
# print(min(marks))
# marks = 20,30,40,50
# print(sum(marks))

# list = [1,2,3,4]
# print(id(list))
# list.append(4)
# print(id(list))

# data = [10, 20, 10, 30, 40, 20, 50]
# data2 = set(data)
# print(data2)


# student1 = {"English","Maths","cs","chemistry","physics"}
# student2 = {"English","biology","chemistry","physics"}

# common_subjects = student1.intersection(student2)
# Unique_subjects = student1.union(student2)
# print(common_subjects,Unique_subjects)

# fs = frozenset({1,2,3})
# print(fs,type(fs))


# set1 = {1,2,3}
# set1 = frozenset(set1)
# print(set1)
# print(type(set1))

# students = {
#     "name" : "saurav",
#     "age" : 22
# }

# print(students)
# print(students.values())
# print(students.keys())

# print(students["name"])
# print(students["age"])

# students.update({"name":"Tarun"})
# # print(students)

# students.pop("age")
# print(students)
# new_student = students.copy()
# print(new_student)

# print(len(students))
# for key in students:
#     print(key, students[key])

# for k, v in students.items():
#     print(k, v)
# squares = {x: x*x for x in range(1, 6)}
# print(squares)

# squares = {x: x*x for x in range(1,101)}
# print(squares)

# students = {
#     "Rollno_1" : {"name":"Saurabh jain","age":22},
#     "Rollno_2" : {"name":"Tarun jain","age":23}
# }

# # print(students["Rollno_1"])
# # print(students["Rollno_2"]["age"])

# users = {
#     "admin": "admin123",
#     "user1": "user123"
# }

# # username = input("Enter your username: ").lower()

# # if username in users:
# #     print("User Exists")
# # else:
# #     print("Invalid User pls sign up")


# Merged_data = students | users
# print(Merged_data)

# sentence = "python is easy and python is powerful"
# words = sentence.split()

# freq = {}

# for word in words:
#     freq[word] = freq.get(word, 0) + 1

# print(freq)

# sentence = input("Enter something : ")
# words = sentence.split()
# freq = {}
# for word in words:
#     freq[word] = freq.get(word,0) +1

# print(freq)

# student = {
#     "name":"saurav",
#     "age":20
# }

# # if "marks" not in student:
# #     student["marks"] = 0

# # print(student)

# print("name" in student)
# print(20 in student.values())
# print("namesss" not in student)

# groceries_prices = {"milk":20,"bread":30,"eggs":40,"milk":30}
# # added_groceries= {"bun":46,"jam":79}
# # groceries_prices.update(added_groceries)
# # print(groceries_prices)
# print(groceries_prices)


# students = {
#     "name":"saurav"
# }
# print(students)

# students = {
#     7:"saurav"
# }
# print(students)


# students = {
#    True :"saurav"
# }
# print(students)


# students = {
#     (80,90):"saurav"
# }
# print(students)


# students = {
#     7.53:"saurav"
# }
# print(students)

# import copy
# l1 = [1,2,[10,20,30],"python"]
# l2 = copy.copy(l1)
# l1[2][0] = 5
# print(l2)

# import copy
# l1 = [1,2,[10,20,30],"python"]
# l2 = copy.deepcopy(l1)
# l1[0] = 5
# # print(l2)

# emp = {
#     "name": "Saurabh",
#     "skills": ["Python", "SQL"]
# }

# emp2 = emp.copy()
# emp2["skills"].remove("Python")

# print(emp)
# print(emp2)
# a = [1, 2, 3,4]
# b = a
# print(b)

# import copy
# original = [1,2,[10,20]]
# shallow = copy.copy(original)
# original[0] = 500
# original[2][0] = 600
# print(original)
# print(shallow)

# import copy

# a = [1, 2, [3, 4]]
# b = copy.copy(a)

# b[2] = [100, 200]
# print(a)
# print(b)

# student = ["marks","90","23yrold"]
# for i in student:
#     print(i)

# a = "apple"
# for i in range(10):
#     print(a)

# age= int(input('Enter your age: '))

# if age>= 18:
#     print("You are eligible to vote")

# print("rest of the programm")

# balance = 5000
# withdrwal_amount = int(input("Enter amount to withdraw: "))
# Remaining_balance = balance - withdrwal_amount
# if withdrwal_amount <= balance:
#     print(f"{withdrwal_amount} debited successfully from balance {balance} and remaining balance is {Remaining_balance}")

# number = int(input("Enter a number: "))

# if number % 2 == 0:
#     print(F"Entered number {number} is a Even number")
# else:
#     print(f"Entered number {number} is a odd number")


# number = int(input("Enter a number: "))

# if number < 0:
#     print("Negative")

# else:
#     print("Positive")

# number = int(input("Enter a number: "))

# print("Positive") if number > 0 else print("Negative")


# salary = 60000
# bonus = 5000 if salary > 50000 else 2000
# print(bonus)
# age = int(input("Enter your age: "))
# print("Adult") if age >= 18 else print("Minor")

# total = 0
# for i in range(1,51):
#     total += i

# print(total)

# s1 = "Hello world"
# for char in s1:
#     print(char)

# students = {
#     "name":"Saurav",
#     "age":20,
#     "Salary":30000
# }

# for i in students:
#     print(i)

# students = {
#     "name":"Saurav",
#     "age":20,
#     "Salary":30000
# }

# for i in students:
#     print(i,students[i])

# students = {
#     "name":"Saurav",
#     "age":20,
#     "Salary":30000
# }

# for i in students.items():
#     print(i)



# students = {
#     "name":"Saurav",
#     "age":20,
#     "Salary":30000
# }

# for i in students.items():
#     print(i[1])

# student = [10,20,30,40]
# for stud in range(len(student)):
#     s = stud + 1
#     print(f"The s roll number for student {s} is {student[stud]} ")


# total = 1
# for i in range(1,51):
#     total *= i

# print(total)

# total = 0
# scores = [10,25,46,5,6,78,45,4,6,0]
# for i in scores:
#     total = total + i

# print(total)

# scores = [10,25,46,5,6,78,45,4,6,0]
# highest = scores[0]
# for score in scores:
#     if highest < score:
#         highest = score

# print(f"Hihest score is {highest}")


# for i in range(3):
#     for j in range(3):
#         break
#     print(i)

# for i in range(3):
#     for j in range(3):
#         break
#     print(i)


# scores = [10,45,66,98,75,32]
# for marks in scores:
#     if marks < 35:
#         continue
#     print(marks)



# scores = {
#     "Saurav":10,
#     "Tarun" : 40,
#     "Hemu" : 80,
#     "Vicky" : 25
# }
# # for marks in scores.values():
# #     if marks < 35:
# #         continue
# #     print(scores.keys(),marks)

# for name , marks in scores.items():
#     if marks > 35:
#         print(name,marks)
# i = 0
# while i < 5:
#     i += 1
#     if i == 3:
#         continue
#     print(i)

# i = 6
# while i > 5:
#     print(i)
#     i += 1

# i = 1
# while i < 5:
#     print(i)
#     i += 1


# correct_password = "admin123"
# attempts = 3

# while attempts > 0:
#     input_password = input("Enter password: ")
#     if input_password == correct_password:
#         print("Login successfull")
#         break
#     attempts -= 1
#     print(f"Wrong password now total {attempts} remaining")

# if attempts == 0:
#     print("Account locked")

# data = [10,20,30,40]
# index = 0
# while index < len(data):
#     print(data[index])
#     index += 1

# while True:
#     num = int(input("Entet 0 to Exit! "))
#     if num == 0:
#         print("Exited successfully")
#         break
#     print("You entered num",num)

# i = 0
# while i < 5:
#     i += 1
#     if i == 3:
#         continue
#     print(i)

# Correct_password = "python"
# while True:
#     user_pass = input("Enter Password: ")
#     if Correct_password == user_pass:
#         print("Correct password!")
#         break
#     else:
#         print("Try again")

# print("logged in")
# import random
# random.seed(10)
# print(random.randint(1,100))

# import random

# data = ["img1", "img2", "img3", "img4"]
# random.shuffle(data)
# print(data)

# import random

# numbers = []

# for _ in range(5):
#     numbers.append(random.randint(1, 50))

# print("Random numbers:", numbers)
# print("Maximum value:", max(numbers))



# import random
# numbers = []
# for i in range(5):
#     numbers.append(random.randint(1,50))

# print(f'Random numbers',numbers)
# print(f"")

# import random
# # print(random.random())
# # print(random.randint(1,100))
# print(random.randrange(0,100,2))
# import random
# names = ["saurav","Tarun","Vicky"]
# correct = random.choice(names)

# if correct == "saurav":
#     print("saurav found")
#     break
# else:
#     print(correct)
        

# import random
# fruits = ["Apple","orange","Mango"]
# # random.shuffle(fruits)
# # print(fruits)    
# while True:
#     name = random.choice(fruits)
#     if fruits == "orange":
#         print("selected",name)

# for i in range(3):        # Outer loop
#     for j in range(2):    # Inner loop
#         print("i:", i, "j:", j)

# for i in range(3):
#     for j in range(2):
#         print("i",i,"j",j)

    
# for i in range(5):
#     for j in range(5):
#         print("*",end="")
#     print()
# for i in range(1, 11):
#     for j in range(1, 13):
#         print(i, "x", j, "=", i*j)
#     print()
#     print()

# for i in range(3):
#     for j in range(3):
#         print(i*j, end=" ")
#     print()
# 0 0 0
# 0 1 0
# 0 2 0
# 1 0 0
# 1 1 1 
# 1 2 2
# 2 0 0 
# 2 1 2


# for i in range(1,6):
#     for j in range(1,1+i):
#         print("*",end="")
#     print()



# for i in range(5,0,-1):
#     for j in range(i-1,0,-1):
#         print("*",end="")
# #     print()

# *
# **
# ***
# ****
# #Roll a dice game
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

# def greet(name):
#     return f"Hello {name}"

# print(greet("Saurav"))


# def greet():
#     print("Welcome user good morning")
#     print("have a nice day")

# greet()
# names = ["Saurav","Tarun"]

# def greet(name):
#         print(f"Welcome {name} good morning")
#         print("have a nice day")
# for name in names:
#     if name[0].startswith("S"):
          
#         greet(name)
#         print()



# number = int(input("Enter number: "))
# def even_odd(number):
#     if number % 2 == 0:
#         print("Even")
#     else:
#         print("Odd")

# even_odd(number)


# def add(num1,num2):
#     result = num1 + num2
#     print(f"Result : {result}")

# add(10,5)
# add(5,-4)

# def add(num1,num2):
#     result = num1 + num2
#     return result

# val1 = int(input("Enter 1st number: "))
# val2 = int(input("Enter 2nd number: "))
# val = add(val1,val2)
# print(f"The addition of {val1} and {val2} is {val}")


# def arithmetic(num1,num2):
#     add = num1 + num2
#     sub = num1 - num2
#     multiplication = num1*num2
#     return add,sub,multiplication

# val1 = int(input("Enter 1st number: "))
# val2 = int(input("Enter 2nd number: "))
# res1,res2,res3 = arithmetic(val1,val2)
# print(f"The addition of {val1} and {val2} is {res1}")
# print(f"The subtraction of {val1} and {val2} is {res2}")
# print(f"The multiplication of {val1} and {val2} is {res3}")


# def greet(name,age):
#     return f"Your name is {name} and age is {age}"


# details = greet("saurav",22)
# print(details)


# def create_user(**data):
#     for key, value in data.items():
#         print(f"{key} : {value}")

# create_user(name="Saurav", email="abc@gmail.com", role="admin")


# def demo(a, b, c=10, *args, **kwargs):
#     print(a, b, c)
#     print(args)
#     print(kwargs)
# demo(10,20,10,20,30,40,name = "Saurav",age = 22)

# def test(*args):
#     print(len(args))

# test(1,2,3,4,5,6,7,8,9,10)


# def length_checker(*args):
#     print(len(args))

# tens = ("Saurav","idjas",20,40,50)

# length_checker(*tens)



# def student_details(sid,sname,*marks):
#     if len(marks) == 0:
#         print(f"Student id {sid} with name {sname} did not appear for any exam")
#     else:
#         percentage = sum(marks) / len(marks)
#         print(f"Student id {sid} with name {sname} got {percentage} %")


# student_details(10,"Saurav",40,60,50)
# student_details(5,"saurav")



# def student_details(sid,sname,**marks):
#     if len(marks) == 0:
#         print(f"Student id {sid} with name {sname} did not appear for any exam")
#     else:
#         percentage = sum(marks.values()) / len(marks)
#         print(f"Student id {sid} with name {sname} got {percentage} %")


# student_details(10,"Saurav",subj = 40, subj2 = 60, subj3 = 50)
# student_details(5,"saurav")

# def student_details(sid,sname,*extra,**marks):
#     if len(marks) == 0:
#         print(f"Student id {sid} with name {sname} did not appear for any exam")
#     else:
#         percentage = sum(marks.values()) / len(marks)
#         print(f"Student id {sid} with name {sname} got {percentage} %")
#         print(f"student {sname} does {extra}")

#     print()

# student_details(10,"Saurav","Football",subj = 40, subj2 = 60, subj3 = 50)
# student_details(5,"saurav","tennis","Badminton",subj = 10,subj2 = 40)


# def add(a,b):
#     '''
#     Docstring for add
    
#     :param a: Description
#     :param b: Description
#     returns a + b
#     '''
#     return a + b

# # print(add(4,4))
# # help(add)


# doc = add.__doc__

# print(doc)


# def divide(a,b):
#     """
#     Docstring for divide
    
#     :param a: int
#     :param b: int
#     return a / b in float
#     """
#     if b == 0:
#         return "Cannot divide denominator as zero"
#     else:
#         result = a / b
#         return result
    

# print(divide(4,0))


# def fac(num):
#     factorial = 1
#     while num > 1:
#         factorial *= num
#         num -= 1
#     return factorial

# n = int(input("Enter number to get factorial: "))
# print(fac(n))


# def fact(num):
#     if num == 1:
#         return 1
#     else:
#         factorial = num * fact(num-1)
#         return factorial
    
# n = int(input("Enter number to get factorial: "))
# print(fact(n))

# x = 10

# def add():
#     x = 15
#     print(x)


# print(x)
# add()



# x = 10

# def add():
#     global x
#     x = 15
#     print(x)

# add()
# print(x)



# def add(number):
#     return number + 1

# def square(number):
#     return number ** 2

# num = int(input("Enter a number: "))
# res_1 = add(num)
# res_2 = square(res_1)

# print(f"Output for number is {res_2}")


# add = lambda x,y : x + y

# print(add(10,5))

# square = lambda x: x**2

# print(square(5))

# check = lambda x: "Even" if x % 2 == 0 else "odd"

# print(check(5))

    # numbers = [1,2,3,4]

    # sqaured = list(map(lambda x:x**2,numbers))
    # print(sqaured)


# numbers = [1,2,3,4]

# odd = lambda x: True if x % 2 != 0 else False
# filtered_output = filter(odd,numbers)

# print(list(filtered_output))


# numbers = [1,2,3,4,5,6,7]
# even = list(filter(lambda x: x % 2 == 0,numbers))
# print(even)

# numbers = [1,2,3,4,5,6,7]

# def even(x):
#     return x % 2 == 0

# even = tuple(filter(even,numbers))
# print(even)


# users = [
#     {"name": "Saurabh", "active": True},
#     {"name": "Rahul", "active": False},
#     {"name": "Aman", "active": True}
# ]

# active_users = list(filter(lambda user:user["active"],users))

# print(active_users)

# print(list(filter(lambda x:x , [0,5,"","hi"])))

# prices = [100, 200, 300]

# final_prices = list(map(lambda price: price * 1.18, prices))
# print(final_prices)

# prices = [100,200,300]
# final_prices = list(map(lambda price : price * 2,prices))
# print(final_prices)
import math

# num = int(input("Enter number: "))
# output = math.sqrt(num)
# print(output) 

# radius = int(input("Enter radius: "))
# AOT = math.pi * (radius ** 2)
# print(AOT)

# import datetime as dt
# t = dt.time(8,5,26)
# print(t)

# import math_operations
# square = math_operations.square_root(25)
# print(square)


# print((-9) ** 0.5)

# import math
# num = int(input("Enter number: "))
# def sqaure(num):
#     if num < 0:
#         return("sqaure root not defined for negative numbers")
#     return math.sqrt(num)


# print(sqaure(num))

# import math_operations
# # print(__name__)
# import math_operations
# math_operations.greet()


# import sys
# print(sys.path)

# # import test_operations

# import sys

# sys.path.append(r"C:\Users\ADMIN\Desktop\PYTHON(TUTORIALS)\Saurabh python 2")

# import test_operations
# test_operations.greet 

# from math_operations import square , add
# print(add(10,5))
# print(square(5))


# file = open("practise.txt","r")
# content = file.read()
# print(content)


# try:
#     with open("practise.txt", "r") as file:
#         print(file.read())
# except FileNotFoundError:
#     print("File does not exist!")




# try:
#     with open("pracdstise.txt","r") as file:
#         print(file.read())
# except FileNotFoundError:
#     print("File does not exits")


# with open("practise.txt", "r") as file:
#     print(file.readline(2))


# with open("practise.txt","r") as file:
#     print(file.readline())


# with open("test.txt","w") as ft:
#     ft.write("This is created automatically by w mode in file section\n This is second line")
# with open("test.txt","r") as f:
#     print(f.read(7))


# with open("practise.txt", "r") as file:
#     lines = file.readlines()
#     print(lines[4])

# with open("practise.txt", "r") as file:
#     for line in file:
#         print(line.strip())


# with open("practise.txt","r") as f:
#     content = f.read()
#     a = 10/0
#     print(content)

# import os
# filename = "C:/Users/ADMIN/Desktop/PYTHON(TD)/practise.txt"
# if os.path.exists(filename):
#     print("file exists")
# else:
#     print("File does not exits")



# import os
# filename = input("Enter File name absolute or relative: ")

# if os.path.exists(filename):
#     print(f"{filename} file exists")
# else:
#     print("File does not exits,creating it")
#     content = input(f"Enter content you want in {filename} ")
#     with open(filename,"w") as cf:
#         cf.write(content)
    

# try:
#     filename = input("Enter name of file to check wheather it exists or not: ")
#     with open(filename,"r") as f:
#         content = f.read()
#         print(content)
    

# except FileNotFoundError:
#     print("File does not exits pls recheck file name")



# age = 24
# if age > 18:
#     print("you are adult")



# try:
#     num1 = int(input("Enter first number: "))
#     num2 = int(input("enter Second number: " ))
#     Result = num1/num2
#     print(Result)
# except ZeroDivisionError:
#         if num2 == 0:
#             print("Denominator cannot be zero")
# except ValueError as VE:
#     print(f"{VE} input should be only digits")



# try:
#     with open("datta.txt","r") as f:
#         content = f.read()
#         print(content)
# except FileNotFoundError as FNF:
#     print("pls enter valid file name")
#     print(FNF)


# try:
#     with open

# try:
#     with open("datadhsd.txt","r") as f:
#         content = f.read()
        
# except FileNotFoundError as FNF:
#     print("pls enter valid file name")
#     print(FNF)
# except SyntaxError as SE:
#     print(SE)
# else:
#     print(content)
# finally:
#     print("this code will always executed")


# import io
# try:
#     with open("datadhsd.txt","w") as f:
#         content = f.read()
# except FileNotFoundError as FNF:
#     print("pls enter valid file name")
#     print(FNF)
# except SyntaxError as SE:
#     print(SE)
# except io.UnsupportedOperation as UO:
#     print(UO)
# else:
#     print(content)
# finally:
#     print("this code will always executed")


# salary = float(input("Enter your salary: "))

# if salary < 0:
#     raise ValueError("Salary cannot be less than zero")
# else:
#     print(f"Your salary is {salary}")


# try:
#     num = int(input("Enter number: "))
# except ValueError:
#     print("Invalid number")
# else:
#     print("Valid number")


# try:
#     num = int(input("Enter number: "))
# except ValueError:
#     print("Invalid number")
# else:
#     print("valid number")


# import logging

# try:
#     num = int(input("Enter numb: "))
# except Exception as e:
#     logging.error(f"Error occurred: {e}")

# import logging

# def process_payment():
#     try:
#         call_external_api()
#     except TimeoutError:
#         logging.error("API timeout")
#         retry()
#     except Exception as e:
#         logging.critical(e)

# import json
# students = {'student1':{'roll':101,'name':'saurav','percentage':85},
# 'student2': {'roll':102,'name':'Tarun','percentage':68}}
# with open("students_data.txt","w") as sd:
#     json.dump(students,sd,indent=4)


# import json

# with open("students_data.txt") as file:
#     students = json.load(file)
#     print(students)


# import json
# with open("config.json","r") as file:
#     config = json.load(file)
    
# maximum_speed = config["max_speed"]
# print(f"your max speed is {maximum_speed}")

# # import json

# with open("config.json", "r") as file:
#     config = json.load(file)

# maZxZx_speed = config["max_speed"]
# minZx_speed = config["min_speed"]

# print("Car max speed is:", maZxZx_speed)
# print("Car min speed is:", minZx_speed)


# import json
# with open("cars.json","r") as cd:
#     data = json.load(cd)
# print(data["cars"][0]["name"])
# print(data["cars"][1]["max_speed"])

# import json
# students = {'student1':{'roll':100,'name':'saurav','percentage':85},
# 'student2': {'roll':102,'name':'hemu','percentage':68}}
# with open("students_data.json","r") as file:
#     data = json.load(file)
# data.update(students)

# with open("students_data.json","a") as fh:
#     json.dump(data,fh,indent=4)

import re
message = "The current version of python is 3.13"
# # print("python" in message)
# # print(message.find("python")) #find is used for finding index of characters
# match_obj = re.search("python",message)
# print((match_obj))


import re

# pattern = "abc"
# text = "abc is here"

# result = re.search(pattern, text)

# print(result)


# pattern = "abc"
# message = "abc is here"
# result = re.search(pattern,message)
# print(result)
# import re
# message = "The current version of python is 3.13"
# match_object = re.search("[0-9].[0-9][0-9]",message)
# print(match_object)


# import re
# message = "The current version of python is 3.13"
# match_object = re.search("[0-9][.][0-9][0-9]",message)
# print(match_object)

# import re
# Text = "Python is very easy programming language"
# pattern = r"[a-z][a-z]"
# result = re.search(pattern,Text)
# print(result)

# import re
# Text = "Python is very easy programming language"
# pattern = input("Enter pattern to find: ")
# result = re.search(pattern,Text)
# print(result)

# import re
# pattern = r"[a-z][a-z][a-z]\D"
# text = "Python is very intresting langauage and i m learning its python3.1 version"
# result = re.search(pattern,text)
# print(result)

# import re
# pattern = r"[a-z][a-z][a-z]\s"
# text = "Python is very intresting langauage and i m learning its python3.1 version"
# result = re.search(pattern,text)
# print(result)



# import re
# text = "My cars max speed is 120 and min is 20"
# pattern = r"\d+"
# result = re.findall(pattern,text)
# print(result)


# import re
# text = "My cars max speed is 120 and min is 20"
# pattern = r"\d+"
# result = re.sub(pattern,"***",text)
# print(result)


# import re
# logs = """
# ERROR 2026-03-02 SpeedSensor failed
# INFO 2026-03-02 Engine started
# ERROR 2026-03-02 Camera disconnected
# """

# # errors = re.findall(r"ERROR.*",logs)
# # print(errors)


# import re
# # text = "Car bike truck"
# # # result = re.search("Car",text)
# # # print(result)
# # text = "car cor c9r "
# # result = re.findall("c.r",text)
# # print(result)

# # text = "a ab abb abbb"
# # result = re.findall("ab*",text)
# # print(result)

# fruits = "apple banana cherry"
# # result = re.search(r"^Hello", "Hello world")
# # print(result)

# import re
# pattern = r"[a-z]{4}"
# text = "The Python is a programming language"
# match_obj = re.search(pattern,text)
# print(match_obj)

# import re
# pattern = r"[A-Z][a-z]+"
# text = "The Python is a programming language"
# match_obj = re.search(pattern,text)
# print(match_obj)

# import re
# pattern = r"^[a-z]{8}"
# text = "python is a programming langauage"
# result = re.search(pattern,text)
# print(result)

# import re
# pattern = r"[a-z]{8}$"
# text = "python is a programming language"
# result = re.search(pattern,text)
# print(result)

# import re
# pattern = r"(is)"
# text = "python is a programming language"
# result = re.search(pattern,text)
# print(result)

# import re
# pattern = r"[A-Z][a-z]+[-][0-9]{10}"
# text = "python is a programming language and Saurav-9403338964,Tarun-8275461815,Mummy-9892505651"
# result = re.findall(pattern,text)
# print(result)

# import re
# pattern = r"[A-Z][a-z]+[-][0-9]{10}"
# text = "python is a programming language and Saurav-9403338964,Tarun-8275461815,Mummy-9892505651"
# result = re.finditer(pattern,text)
# for r in result:
#     print(r)

# import re
# s1 = "Sunday ,Monday, Tuesday ,Monday, Sunday"
# pat = "Sunday"
# replacement = "Friday"
# result = re.sub(pat,replacement,s1)
# print(result)


# import re
# s1 = "Sunday ,Monday, Tuesday ,Monday, Sunday, 556454"
# pat = r"\d"
# replacement = "*"
# result = re.sub(pat,replacement,s1)
# print(result)


# import re
# s1 = "Sunday ,Monday, Tuesday ,Monday, Sunday , +91-6464219642,+91-62454974"
# pat = r"[+-]"
# replacement = ""
# result = re.sub(pat,replacement,s1)
# print(result)


# import re

# import re

# text = "car bike car bus"

# print(re.findall("car", text))

# import re
# pattern = r"\d+"
# compiled_pattern = re.compile(pattern)
# text = "python is a programming language and Saurav-9403338964,Tarun-8275461815,Mummy-9892505651"
# result = re.findall(compiled_pattern,text)
# print(result)
'''
Valid emaiil
Alice alice-cool_123@gmail.com 9403338964
Carol Carol_123@example.com 9892505651
John John.den.123@devdomain.edu 8275461815
Invalid email:
_123abc@example.com
_123abc@gmail.edu-com'''

# import re
# with open("Student_details.txt","r") as fh:
#     data = fh.read()
# pattern = r"\b[a-zA-z]+[\w.-]+[@][a-z]+[.][a-z]+\b"
# match_obj = re.finditer(pattern,data)
# for d in match_obj:
#     print(d)


# name = "Saurav"
# value  = 100
# float = 3.14
# None
# True
# False

# price = 10
# print(price + price + price)

# a = b = c = 10
# print(a + b + c)


# import keyword
# print(keyword.kwlist)

# name = "Saurabh"
# name[0] = "t"
# print(name)
# print(name[2:])
# print(name.lower())
# print(name.upper())
# print(name.strip())
# name = "t" + name[1:]
# print(name)

# age = 20
# print("Age is " + str(age))
# print("Age is " + age)

# print(complex(5))

# # val = 3 + 4j
# # print(type(val))
# a = input("Enter number 1: ")
# b = input("Enter number 2: ")
# print(int(a) + int(b))

# print("10" + "10")
# msg = "I love java"
# # print(msg.replace("java","Python"))

# # items = ['a', 'b', 'c']
# # print("$".join(items))
# print(msg.find("j"))
# print(len(msg))

# a = 5
# b = True
# print(a + b)

# a = int(input("Enter a number: "))
# if a % 2 == 0:
#     print(f"{a} is Even Number")
# else:
#     print(f"{a} is a odd number")

# a = 5
# b = 10

# print(a == b)

# Rohan_marks = int(input("Enter your marks: "))
# if Rohan_marks >= 40:
#     print("Congrats You are passed")
# else:
#     print("Sorry you are failed")

# day = input("Enter day: ")
# if day == "Saturday" or day == "Sunday":
#     print("Woah its a holiday")
# else:
#     print("Sorry its not a holiday")

# users = ["Saurabh","Tarun","Vicky"]
# User_name = input("Enter username to search: ")
# User_index = users["User_name"]
# if User_name in users:
#     print(f"User found at {User_index}")
# else:
#     print(f"{User_name} not found")


# print("Apple","Banana","Mango",sep="-")

# print("Age:", 22, sep=" ")

# print("Saurav", 22, "India",sep="/")

# print("Hello",end=" ")
# print("World")

# print("2026","02","01",sep="-",end="/")

# f = open("Opening.txt","w")
# print("Hello this content is written by print function",file=f)
# f.close()

# name = "Saurav"
# Age = 22
# print(f"My name is {name} and my age is {Age}")


# print("Saurabh\tJain")

# print(2**3)
# print(pow(2,3))

# score = [10,20,30,25]
# print(max(score))

# a = complex(2,3)
# print(a)

# print(divmod(455,9))

# import math

# a = int(input("Enter 1st side: "))
# b = int(input("Enter 2nd side: "))
# c = int(input("Enter 3rd side: "))

# s = (a + b + c)/2

# Area = math.sqrt(s*(s-a)*(s-b)*(s-c))
# print(f"Area of traingle {Area}")

# city = "new delhi"

# print(city.capitalize())
# print(city.title())

# name = input("Enter your name: ")
# username = "Hello user"
# updated_username = username.replace("user",name)
# print(updated_username)

# data = "Saurav,Jain,23,India"

# info = data.split(",")
# print(info)

# words = ["Python", "is", "powerful"]

# # sentence = " ".join(words)
# print(words,sep=" ")
# from datetime import datetime

# now = datetime.now()

# print(f"Report generated on: {now}")

# marks = 82
# print(f"Result: {'Pass' if marks > 40 else 'fail'}")



# print("Item\tQuantity\tPrice")
# print("Pipe\t10\320")

# import time

# for i in range(1, 6):
#     print(f"\rProcessing {i}/5", end="")
#     time.sleep(1)
# print("Processing completed")

# print("Page 1\fPage 2")
# name = "Saurabh"
# Salary = 200000
# print(f"Employee:\t{name}\nSalary:\t{Salary}")

# print(r"C\Admin\Users\Desktop")

# name = "Saurabh is a humble person"
# print("humble" in name)

# student = {
#     "name":"Saurabh",
#     "Age":20
# }

# print("Saurabh" in student.values())

# Attendance_list = ["Saurbah","Tarun","Vicky"]
# name = input("Enter student name: ")
# if name in Attendance_list:
#     print("Present")
# else:
#     print("Absent")
# text = "hello"
# text = text.replace("h", "H")
# print(text)

# students = ["Saurabh","Tarun","Rahul"]
# print(students[0])
# students[0] = "Vicky"
# print(students)
# print(students[0:])

# orders = ["Order1","order3"]
# orders.insert(1,"Order2")
# print(orders)
# # orders.append("Order3")
# print(orders)

# old_users = ["manish","Sangeeta"]
# New_users = ["Sanajana","Jatin"]
# old_users.extend(New_users)
# print(old_users)

# votes = ["Yes", "No", "Yes", "Yes"]
# print(votes.count("Yes"))

# original = [1, 2, 3]
# backup = original.copy()

# backup.append(4)
# print(original)
# print(backup)

# original = [1,2,3]
# backup = original.copy()
# backup.append(4)
# print(backup)
# import math

# Monthly_sales_Report = [1000,2000,45200,500,45600]
# total_sales = sum(Monthly_sales_Report)
# Highest_sales = max(Monthly_sales_Report)
# Lowest_sales = min(Monthly_sales_Report)
# Avg_sales = total_sales/len(Monthly_sales_Report)
# print(total_sales,Highest_sales,Lowest_sales,Avg_sales)

# Godl = [
#     ["jonathan","Kio","Harsh","Jelly"],
#     ["Spower","Manya","Admino","Saumya"]
# ]

# print(Godl[1][2])

# numbers = [1,2,3,4,5,6]
# # squares = []
# # for n in numbers:
# #     squares.append(n*n)
# # print(squares)

# sqaures = [n*n for n in numbers]
# print(sqaures)
# even = []

# for n in numbers:
#     if n%2 == 0:
#         even.append(n)
# print(even)



# Base_salary = [10000,18000,25000,35600]
# bonus_salary = []
# for b in Base_salary:
#     if b > 15000:
#         bonus_salary.append(b + (b *0.1))
# print(bonus_salary)

# Godl = ["jonathan","Kio","Harsh","Jelly"]
# upper_cased_names = [n.upper() for n in Godl]
# print(upper_cased_names)

# names = ["aman", "saurabh", "neha"]

# upper_names = [name.upper() for name in names]
# print(upper_names)

# marks = [30,50,60,70]
# result = ["pass" if m >=40 else "Fail" for m in marks]
# print(result)

# # marks = [45, 78, 30, 90]

# # result = ["Pass" if m >= 40 else "Fail" for m in marks]
# # print(result)

# data = ["Python", "", "Java", "", "C++"]
# cleaned_data = [x for x in data if x!= ""]
# print(cleaned_data)

# matrix = [
#     [1, 2],
#     [3, 4],
#     [5, 6]
# ]

# flat = [num for row in matrix for num in row]
# # print(flat)
# logs = ["ERROR", "INFO", "ERROR", "WARNING"]

# error_logs = [log for log in logs if log == "ERROR"]
# print(error_logs)

# logs = ["ERROR","RUNNING","ERROR","WARNING"]
# error_logs = [log for log in logs if log == "ERROR"]
# print(error_logs)

# list1 = [1,2,3]
# list2 = [4,5,6]

# for items in list1:
#     list1.append(list2)
# print(list1)
# Combined_list = list1 + list2
# print(Combined_list)

# Employess_list1 = ["Saurabh","Tarun","Hemu"]
# Employess_list2 = ["Vicky","Rahul"]
# Employess_list1.extend(Employess_list2)
# print(Employess_list1)

# from itertools import chain

# list1 = [1,2,3]
# list2 = [4,5,6]

# # result = list(chain(list1,list2))
# # print(result)

# summation = [a + b for a,b in zip(list1,list2)]
# print(summation)

# jan = [2000, 1500, 3000]
# feb = [2200, 1600, 2800]
# # jan.extend(feb)
# # print(jan)
# # print(sum(jan))
# summation = [a+b for a,b in zip(jan,feb)]
# print(summation)

# nums = [1,2,3]
# result = nums * 3
# print(result)


# names = ["A", "B"] * 2
# print(names)

# a = [1, 2]
# b = [3, 4]

# a.append(b)
# print(a)

# jan = [2000, 1500, 3000]
# feb = [2200, 1600, 2800]
# jan.extend(feb)
# print(jan)

# data = ["A", "B", "A", "C", "A"]
# cleaned = [x for x in data if x! = "A"]
# print(cleaned)

# data = ["A", "B", "A", "C", "A"]

# Data = list(filter(lambda x: x != "A", data))
# print(Data)

# orders = ["Completed", "Cancelled", "Pending", "Cancelled"]
# orders = [o for o in orders if o != "Cancelled"]
# print(orders)

# nums = [1,2,3,44,554,24,67]
# nums.sort(reverse=True)
# print(nums)

# marks = (10,20,30)
# print(type(marks))

# t = ([1, 2], 3)
# t[0].append(4)
# print(t)

# a = 10
# print(id(a))
# b = 10
# print(id(b))

# list1 = [10, 20]
# list2 = list1

# print(id(list1))
# print(id(list2))

# my_set = {10,20,30}
# print(type(my_set))
# mm = { }

# emails = ["a@gmail.com", "b@gmail.com", "a@gmail.com", "c@gmail.com"]
# unique_elements = set(emails)
# print(unique_elements)

# s = {1, 2}
# s.update([3, 4, 5])
# print(s)

# s = {1, 2, 3}
# s.pop()
# print(s)

# a = {1,2,3}
# b = {4,5,6}
# c = a | b
# print(c)

# a = {1, 2}
# b = {1, 2, 3}
# print(a.issubset(b))
# print(b.issuperset(a))

# sets = {1,2,3}
# fs = frozenset(sets)
# print(type(fs))

# python = {"A", "B", "C", "D"}
# java = {"C", "D", "E"}
# common = python & java
# print(common)

# required = {"Python", "SQL"}
# candidate = {"Python", "SQL", "AWS"}
# print(required.issubset(candidate))

# order = {"pen", "book"}
# stock = {"pen", "book", "pencil", "eraser"}
# if order.issubset(stock):
#     print("You can place order")
# else:
#     print("sorry you cannot place")

# a = [1, 2, 3]
# b = [3, 4, 5]
# print(set(a) | set(b))

# name1 = "python"
# name2 = "java"

# # print(set(name1) - set(name2))
# s = set()
# s.add(10)
# s.add(20)
# print(s)

# premium_users = {"A", "B", "C", "D"}
# trial_users = {"C", "D", "E"}
# paid_users = premium_users - trial_users
# print(paid_users)

# A = {1, 2, 3, 4, 5}
# B = {2, 3}
# C = {4}
# print(A - B - C)

# permissions = {
#     frozenset(["read", "write"]): "Editor",
#     frozenset(["read"]): "Viewer"
# }

# print(permissions[frozenset(["read", "write"])])

# student_details = {
#     "Name":"Saurabh",
#     "Age":22,
#     "Course":"MscIT"
# }
# print(type(student_details))
# print(student_details["Name"])
# print(student_details.get("Location"))
# b = set(student_details.keys())
# print(b)
# print(type(b))

# print(student_details.keys())
# print(student_details.get("Name"))

# student_details.update({"Age":23,
#                        "Course":"MBA"})
# print(student_details)

# student_details2 = student_details.copy()
# print(student_details2)

# for k , v in student_details.items():
#     print(k,v)

# sqaures = {x : x*x for x in range(1,6)}
# print(sqaures)

# Students =  {
#     "24306A1065":{"Name":"Saurabh","Age":23,"Course":"MSCIT"},
#     "24306A1050":{"Name":"Rahul","Age":22,"Course":"MSCIT"},
# }
# Roll_no = input("Enter student Roll number to get: ")
# Students_details = input("Enter student details to get: ")
# print(Students[Roll_no][Students_details])

# users = {
#     "admin":"admin123",
#     "user1":"uspass123"
# }

# username = input("Enter username: ")
# if username in users:
#     print(f"User exists with key {users[username]}")
# else:
#     print(f"User does not exist")

# d = {"a":1}
# d["a"] = 100
# print(d)

# import copy
# original_list = [[1,2],[3,4]]
# Shallow_list = copy.copy(original_list)
# Deep_list = copy.deepcopy(original_list)
# Deep_list[0][0] = 9
# # print(original_list,Shallow_list)
# Shallow_list[0][0] = 7
# # print(original_list)/
# print(original_list)
# print(Deep_list)

# sentence = "python is easy and python is powerful"
# words = sentence.split()

# freq = {}

# for word in words:
#     freq[word] = freq.get(word, 0) + 1

# print(freq)

# sentence = "python is easy and python is powerful"
# words = sentence.split()
# freq = {}
# for word in words:
#     freq[word] = freq.get(word,0) + 1
# print(freq)


# student = {
#     "name": "Saurabh",
#     "age": 22,
#     "course": "MSc IT"
# }
# if "marks" not in student:
#     student["marks"] = 1

# print(student)
# if "age" in student:
#     print("Found")
# print(student.get("age"))
# # print(22 in student)
# for value in student.values():
#     if value == 22:
#         print("Found")

# users = {
#     "admin": "admin123",
#     "user1": "pass456"
# }

# username = input("Enter username: ")
# if username in users:
#     print("User found")
# else:
#     print("Not found")

# data = {"user": {"name": "Saurabh"}}
# print("user" in data)
# print("name" in data["user"])


# Groceries = {
#     "Milk":20,
# #     "Bread":30
# }

# Added_groceries = {
#     "Bun":50,
#     "Butter":30
# }

# Groceries.update(Added_groceries)
# print(Groceries)


# student = {
#     "name": "Saurabh",
#     "age": 22,
#     "course": "MSc IT",
#     (1,1) : "Sjain"
# }

# print(student)

# a = [1, 2, 3]
# b = a
# b.append(4)
# print(a)

# a = [1, 2, [3, 4]]
# b = a[:]

# b[2].append(5)
# print(a)

# emp = {
#     "name": "Saurabh",
#     "skills": ["Python", "SQL"]
# }

# emp2 = emp.copy()
# emp2["skills"].remove("SQL")

# print(emp)

# student = ["Saurabh",22,True]
# for i in student:
#     print(i)

# for i in range(6):
#     print(i)

# balance = 20000
# Withdraw_amount = int(input("Enter amount to withdraw: "))
# if Withdraw_amount <= balance:
#     print(f"{Withdraw_amount} withdrawn successfully")
# else:
#     print(f"{Withdraw_amount} is higher than {balance} so transaction failed")

# salary = 60000
# bonus = 5000 if salary >= 50000 else 2000
# print(bonus)

# print("Yes" if [] else "No")

# students = {
#     "name":"Saurav",
#     "age":20,
#     "Salary":30000
# }

# for value in students.values():
#     print(value)

# for i in students.items():
#     print(i[1])

# student = [10,20,30,40]
# for stud in range(len(student)):
#     s = stud + 1
#     print(f"The s roll number for student {s} is {student[stud]} ")

# scores = [10,25,46,5,6,78,45,4,6,0]
# highest = scores[0]
# for score in scores:
#     if highest < score:
#         highest = score

# print(f"Highest score is {highest}")

# scores = [10,25,46,5,6,78,45,4,6,0]
# highest = scores[0]
# for score in scores:
#     if highest < score:
#         highest = score
# print(f"Highest score is {highest}")

# i = 1
# while i <= 5:
#     print(i)
#     i += 1

# correct_password = "admin123"
# attempts = 3
# while attempts > 0:
#     password = input("Enter your password: ")

#     if password == correct_password:
#         print("Login successful")
#         break
#     attempts-=1
#     print(f"Incorrect password number of attempts left {attempts} ")

# if attempts == 0:
#     print("You ran out of attempts , account Locked!")
    
# data = [10,20,30,40]
# index = 0
# while index < len(data):
#     print(data[index])
#     index += 1

# while True:
#     num = int(input("Enter any number(o to exit):  "))
#     if num == 0:
#         break
#     print(f"you entered {num}")

# i = 0
# while i < 5:
#     i += 1
#     if i == 3:
#         continue
#     print(i)


# number = int(input("Enter -1 to stop: "))

# while number != -1:
#     print("You entered:", number)
#     number = int(input("Enter -1 to stop: "))

# import random
# print(random.random())4
# print(random.randint(1,7))
# rn = []
# for i in range(1,51):
#     rn.append(i)

# print(rn)

# rn  = [(random.sample(1,51,5))]
# print(rn)
# print(max(rn))
# rn = []
# for i in random.randrange(1,51):
#     rn.append(i)
# print(rn)


# import random
# numbers = [random.randrange(1,51) for i in range(5)]
# print(numbers)
# print(max(numbers))

# for i in range(1,60):
#     for j in range(1,1+i):
#         print("*",end="")
#     print()

# def greet():
#     Welcome = input("Enter your name: ")
#     print(f"Hello {Welcome}")
#     return Welcome

# # print(greet())
# greet()
# name = input("Enter your name: ")
# def greet(input):
    
# names = "Saurav","Tarun"

# def greet(name):
#         print(f"Welcome {name} good morning")
#         print("have a nice day")
# for name in names:
#     greet(name)

# names = ["Saurabh","Tarun"]
# def greet(name):
#     print(f"welcome {name} good morning")
#     print("Have a nice day")
# for name in names:
#     greet(name)

# names = ["Saurabh","Tarun"]
# def greet(name):
#     print(f"")

# names = ["Saurabh","Tarun"]
# def greet(name):
#     print(f"welcome {name} good morning")
#     print("Have a nice day")
# for name in names:
#     if name[0].startswith("S"):
#         greet(name)
#         print()
#         break
# else:
#     print("No name starts with S")

# number = int(input("Enter number: "))
# def func(number):
#     if number % 2 == 0:
#         print(f"{number} is even")
#     else:
#         print(f"{number} is odd")

# # func(number)
# a = int(input("Enter first number: "))
# b = int(input("Ener seconf number: "))
# def add(a,b):
#     result = a + b
#     print(f"Result: {result}")

# add(a,b)
# def add(a,b):
#     return a + b 

# result = add(4,5)
# print(result)

# def calculate_total(amount,tax):
#     return amount + (amount*tax)
# calculate_total = calculate_total(100,5)
# print(calculate_total)

# def check(num):
#     if num > 0:
#         return "Positive"
#     return "Negative or Zero"
# print(check(5))


# def Arithmetic(num1,num2):
#     add = num1 + num2
#     sub = num1 - num2
#     multi = num1*num2
#     return add,sub,multi

# val1 = int(input("Enter value 1: "))
# val2 = int(input("Enter value 2: "))
# res1,res2,res3 = Arithmetic(val1,val2)
# print(f"The addition of {val1} and {val2} is {res1}")
# print(f"The subtraction of {val1} and {val2} is {res2}")
# print(f"The multiplication of {val1} and {val2} is {res3}")\

# def greet(name,age):
#     print(f"Name {name}")
#     print(f"Age {age}")

# greet("saurabh",22)
# greet(age=22,name="Saurabh")

# def add(*numbers):
#     print(type(numbers))
#     return(sum(numbers))

# Total = add(10,20,30,40)
# print(Total)

# def calculate_total(*prices):
#     total = 0
#     for price in prices:
#         total += price
#     return total
        
# print(calculate_total(10,20,30))

# def student_details(**details):
#     print(details)

# student_details(Name="Saurabh",Age=22,Course="Mscit")
# print(type(student_details))

# def user_data(**data):
#     for key,value in data.items():
#         print(f"{key} : {value}")

# user_data(Name = "Saurabh",Age = 22)

# def demo(a, b, c=10, *args, **kwargs):
#     print(a, b, c)
#     print(args)
#     print(kwargs)

# demo(5,6,4,56,56,name = "Saurabh")

# def test(a, *args, **kwargs):
#     print(a)
#     print(args)
#     print(kwargs)

# test(10, 20, 30, x=100)

# def length_checker(*args):
#     print(len(args))

# list = ["Saurav","idjas",20,40,50]
# length_checker(list) 

# def calculate_percentage(sid,sname,*marks):
#     if len(marks) == 0:
#         print(f"Student with sid {sid} and name {sname} did not appear for any exam")
#     else:
#         percentage = sum(marks)/len(marks)
#         print(f"The percentage of student is {percentage}%")


# calculate_percentage(21,"Saurabh",90,90,90,90,90)
# calculate_percentage(20,"Saurabh")


# def calcualtion(sid,sname,*extra,**marks):
#     if len(marks) == 0:
#         print(f"Student did not appear for any exam")
#     else:
#         percentage = sum(marks.values()) / len(marks)
#         print(f"Student wiht {sid} and {sname} got {percentage}%")
#         print(f"Student with {sid} does do {extra}")


# calcualtion(20,"Tarun","Footplay","Swimming",Sub1 = 90,sub2 = 90)


# def add(a,b):
#     "This is function use to  return sum of two numbers"
#     return a + b

# print(add(4,5))
# # print(add.__doc__)
# doc = add.__doc__
# print(doc)


# def fact(num):
#     factorial = 1
#     while num > 1:
#         factorial *= num
#         num -= 1
#     return factorial
    
# n= int(input("Enter number to get its factorial: "))
# print(fact(n))

# def fact(num):
#     if num == 1:
#         return 1
#     else:
#         factorial = num * fact(num-1)
#         return factorial
    
# n = int(input("Enter number: "))
# print(fact(n))


# def fact(num):
#     if num <= 1:
#         return 1
#     else:
#         factorial = num * fact(num-1)
#         return factorial
    
# n = int(input("Enter number: "))
# print(fact(n))
# def test(n):
#     return test(n-1)

# print(test(5))

# def numbers(num):
#     if num == 1:
#         return 1
#     else:
#         numb = 1 + num

# def print_numbers(n):
#     if n == 0:
#         return
#     print(n)
#     print_numbers(n - 1)

# n = int(input("Enter a number: "))
# print_numbers(n)


# def print_nmbers_list(n):
#     if n == 0:
#         return
#     print(n)
#     print_nmbers_list(n-1)
    

# n = int(input("Enter number: "))
# print_nmbers_list(n)


# n = int(input("Enter number: "))

# for i in range(n,0,-1):
#     print(i)


# def numbers(num):
#     if num == 0:
#         return
#     else:
#         print(num)
#         numbers(num-1)

# n = int(input("Enter number: "))
# numbers(n)


# # Sum of First N Natural Numbers
# def sum(num):
#     if num == 0:
#         return 0
#     else:
#         return (num) + sum(num-1)
        

# N = int(input("Enter number: "))
# Total = sum(N)
# print(Total)

# n = int(input("Enter a number: "))
# total = 0

# for i in range(1, n + 1):
#     total += i

# print(f"Sum of numbers from 1 to {n} is {total}")

# n = int(input("Enter number: "))
# Total = 0
# for i in range(1,n+1):
#     Total += i

# n = int(input("Enter number: "))
# n = abs(n)
# count = 0
# if n == 0:
#     count = 1
# else:
#     while n > 0:
#         count += 1
#         n //= 10

# print(f"Digits {count}")

# A = input("Enter string: ")
# A = A.sort(reversed)
# print(A)


# s = input("Enter a string: ")

# rev = ""
# for ch in s:
#     rev = ch + rev

# print("Reversed string =", rev)

# String = input("Enter string: ")
# Reversed_string = ""
# for ch in String:
#     Reversed_string = ch + Reversed_string

# print(f"Reversed string {Reversed_string}")


# OGS = input("Enter string: ")
# Rev = ""
# for ch in OGS:
#     Rev = ch + Rev

# print(Rev)


# x = 10
# def functions():
#     print(f"Inside function {x}")

# functions()
# print(f"Outside function {x}")

# Name = input("Enter your name: ")
# def greet():
#     print(f"Hello {Name}")

# Balance = int(input("Enter amount to balance:"))
# def Amount_remaining():
#     print(f"Your current balance is {Balance}")

# def calling_functions(func):
#     func()

# calling_functions(greet)

# def add(a,b):
#     return a + b

# def subtract(a,b):
#     return a - b

# def calculator(operation,x,y):
#     return operation(x,y)


# print(calculator(add,5,5))
# print(calculator(subtract,10,5))


# def add(number):
#     return number + 1

# def square(number):
#     return number ** 2

# Num = int(input("Enter number: "))
# Result_1 = add(Num)
# Result_2 = square(Result_1)

# print(f"The sqaure of number {Num} + 1 is : {Result_2}")


# def add(a,b):
# #     return a + b

# # print(add(5,10))

# add = lambda a , b : a + b
# # print(add(10,10))
# x = int(input("Enter number: "))
# Even_odd = lambda x: "Even" if x % 2 == 0 else "Odd"
# print(Even_odd(x))



# students = [
#     {"name": "Saurabh", "marks": 85},
#     {"name": "Rahul", "marks": 95},
#     {"name": "Aman", "marks": 75}
# ]

# sorted_students = sorted(students, key=lambda x: x["name"])
# print(sorted_students)

# Students = [
#     {"Name" : "Saurabh","Marks":85},
#     {"Name" : "Tarun", "Marks":95},
#     {"Name":"Rahul","Marks":99}
# ]

# sorted_students = sorted(Students,key=lambda x:(x["Name"],x["Marks"]))
# print(sorted_students)

# numbers = [1,2,3,4,5]
# # sqared = list(map(lambda x:x*2,numbers))
# # print(sqared)
# Even = list(filter(lambda x: x % 2 == 0 ,numbers))
# print(Even)

# def calculate_function(function,value):
#     return function(value)

# Result = calculate_function(lambda x: x + 10,5)
# print(Result)


# print(list(map(lambda x: x**2, [1,2,3])))

# Numbers = [1,2,3,4,5]
# def even(x):
#     return x % 2 == 0
# # Even = list(filter(lambda x: x%2 != 0 , Numbers))
# Even = list(filter(even, Numbers))
# print(Even)

# users = [
#     {"name": "Saurabh", "active": True},
#     {"name": "Rahul", "active": False},
#     {"name": "Aman", "active": True}
# ]

# active_users = list(filter(lambda user: not user["active"],users))
# print(active_users)

# Prices = [100,200,300]
# Total_with_GST = list(map(lambda price:price * 1.18,Prices))
# print(Total_with_GST)

# a = [1,2,3]
# b = [10,20]
# addition = list(map(lambda x,y:x+y,a,b))
# print(addition)

# import math_operations
# print(math_operations.add(10,5))
# print(math_operations.square(5))