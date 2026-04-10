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


