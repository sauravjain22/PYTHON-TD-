'''Task 1: Perform Basic Mathematical Operations
Problem Statement: Write a Python program that does the following:
1.  Takes two numbers as input from the user.
2.  Performs the basic mathematical operations on these two numbers:
o	Addition
o	Subtraction
o	Multiplication
o	Division
3.  Displays the results of each operation on the screen.
'''

num1 = int(input("Enter first Number: "))
num2 = int(input("Enter Second Number: "))

print("Addition : ",num1 + num2)
print("Subtraction :",num1 - num2)
print("Multiplication :",num1*num2)
print("Division : ",num1/num2)


''' 
Task 2: Create a Personalized Greeting
Problem Statement: Write a Python program that:
1.  Takes a user's first name and last name as input.
2.  Concatenates the first name and last name into a full name.
3.  Prints a personalized greeting message using the full name.
'''

First_name = input("Enter your first name :")
Last_name = input("Enter your last name : ")
Full_name = First_name +" " + Last_name

print(f"Hello {Full_name} Welcome to python programm")