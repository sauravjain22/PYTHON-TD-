'''Task 1: Read a File and Handle Errors 
Problem Statement:  Write a Python program that:
1.   Opens and reads a text file named sample.txt.
2.   Prints its content line by line.
3.   Handles errors gracefully if the file does not exist.
'''

try:
    name = input("Enter name of file: ")
    with open(name,"r") as file:
        line1 = file.readline().strip()
        line2 = file.readline().strip()
        print("Reading file content")
        print(f"Line 1: {line1}")
        print(f"Line 2: {line2}")

except FileNotFoundError as fnf:
    print(f"Error : The file '{name}' was not found")

print()




 
'''Problem Statement: Write a Python program that:
1.   Takes user input and writes it to a file named output.txt.
2.   Appends additional data to the same file.
3.   Reads and displays the final content of the file.


'''
text = input("Enter text to write to the file named Output.txt: ")
with open("Output.txt","w") as Op:
    Op.write(text)
    print(f"Data successfullt written to the Output.txt")
Additional_text = input("Enter additional text to append: ")
with open("Output.txt","a") as Op:
    Op.write("\n" + Additional_text)
    print(f"Data sucessfully append")
print()

print(f"Final content of Output.txt")

print()

with open("Output.txt","r") as Op:
    data = Op.read()
    print(data)