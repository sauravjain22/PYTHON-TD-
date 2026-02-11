'''
Task 1: Check if a Number is Even or Odd
Problem Statement:  Write a Python program that:
1. 	Takes an integer input from the user.
2. 	Checks whether the number is even or odd using an if-else statement.
3. 	Displays the result accordingly.
'''

number = int(input("Enter number: "))
if number % 2 == 0:
    print(f"{number} is an even number")

else:
    print(f"{number} is an odd number")

'''
Task 2: Sum of Integers from 1 to 50 Using a Loop
 
Problem Statement: Write a Python program that:
1.   Uses a for loop to iterate over numbers from 1 to 50.
2.   Calculates the sum of all integers in this range.
3.   Displays the final sum.

'''
summation = 0
for i in range(1,51):
    summation += i
    
print(f"Sum of all numbers {summation}")