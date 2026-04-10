# Problem Statement: Write a Python program that:
# 1.   Creates a dictionary where student names are keys and their marks are values.
# 2.   Asks the user to input a student's name.
# 3.   Retrieves and displays the corresponding marks.
# 4.   If the student’s name is not found, display an appropriate message.

Stud_marks = {
    "Saurav":80,
    "Tarun":70,
    "Vicky":66,
    "Amish":74,
    "Himanshu":46
} 

name = input("Enter the Student's name: ")

if name in Stud_marks:
    print(f"{name}'s marks are: {Stud_marks[name]}")
else:
    print(f"Student not found.")


'''
Problem Statement: Write a Python program that:
1.   Creates a list of numbers from 1 to 10.
2.   Extracts the first five elements from the list.
3.   Reverses these extracted elements.
4.   Prints both the extracted list and the reversed list
'''

Original_list = [1,2,3,4,5,6,7,8,9,10]
Extracted_list = Original_list[0:5]
Reversed_list = list(reversed(Extracted_list))
print(f"Original list: {Original_list}")
print(f"Extracted first five elements : {Extracted_list}")
print(f"Reversed Extracted elements: {Reversed_list}")

