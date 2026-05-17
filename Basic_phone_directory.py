class Contact:

    phone_directory = []

    def __init__(self,name,Phone_number):
        self.name = name
        self.Phone_number = Phone_number
        Contact.phone_directory.append(self)

    def show_contact(self):
        return f"Name : {self.name}, Phone number : {self.Phone_number}"
    
    @classmethod
    def show_all_contact(cls):
        if len(cls.phone_directory) == 0:
            print(f"No contact found")
        else:
            for contact in cls.phone_directory:
                print(contact.show_contact())

    @staticmethod
    def Validate_number(number):
        if len(number) >= 8 and number.isdigit():
            return True
        else:
            return False

    @classmethod
    def search_contact(cls,search_name):
        # Name = input("Enter name: ")
        # Name == search_name
        for contact in cls.phone_directory:
            if contact.name.lower() == search_name.lower():
                return f"The contact number for {search_name} is {contact.Phone_number}"
            
        return f"No contact found for name {search_name}"

    @classmethod
    def Add_contacts(cls):
        n_contacts = int(input("Enter number of contacts you want to add: "))
        for i in range(n_contacts):
            name = input("Enter name: ")
            Phone_number = input("Enter phone number: ")
            if Contact.Validate_number(Phone_number):
                Contact(name,Phone_number)

c1 = Contact("Saurabh",9403338964)
c2 = Contact("Tarun",8275461815)
c3 = Contact("Vicky",9892351936)
c4 = Contact("Sheref",9874565477)

while True:
    print("Welcome to phone directory app,choose your options below")
    print("\n1 to Add Contact")
    print("2 to Show all Contacts")
    print("3 to Search Contact")
    print("4 to Exit")

    option = int(input("Choose option: "))

    if option == 1:

        Contact.Add_contacts()

    elif option == 2:

        Contact.show_all_contact()

    elif option == 3:

        search_name = input("Enter name to search: ")

        print(Contact.search_contact(search_name))

    elif option == 4:

        print("Program Closed")
        break

    else:

        print("Invalid Option")      


"""
    This program is a:

Phone Directory System

It can:

store contacts
show contacts
search contacts
add new contacts

And you built it using:

OOP concepts
1. CLASS CREATION
class Contact:

This creates blueprint/template for contact objects.

Every contact object will contain:

name
phone number

And related behaviors.

2. CLASS VARIABLE
phone_directory = []

This is:

class variable

Meaning:

shared by ALL objects
only one copy exists

Think of it as:

main shared contact book
IMPORTANT

All contacts get stored here.

Example later:

[c1, c2, c3, c4]
3. CONSTRUCTOR (__init__)
def __init__(self,name,Phone_number):

Runs automatically when object is created.

Example:

c1 = Contact("Saurabh",9403338964)
INTERNAL FLOW

Python roughly does:

1. create empty object
2. self = c1
3. name = "Saurabh"
4. Phone_number = 9403338964
5. run __init__()
4. INSTANCE VARIABLES
self.name = name
self.Phone_number = Phone_number

These belong to:

individual objects

Example:

c1.name → "Saurabh"
c2.name → "Tarun"

Each object stores separate values.

5. MOST IMPORTANT LINE
Contact.phone_directory.append(self)

This stores:

current object itself

inside shared directory.

EXAMPLE

When:

c1 = Contact(...)

runs:

self = c1

So:

Contact.phone_directory.append(c1)

happens internally.

AFTER ALL OBJECTS

Directory becomes:

[c1, c2, c3, c4]
IMPORTANT UNDERSTANDING

You are storing:

OBJECTS

not strings.

Very important OOP concept.

6. INSTANCE METHOD
def show_contact(self):

This works with:

one specific object
EXAMPLE
c1.show_contact()

Internally:

Contact.show_contact(c1)

So:

self = c1
RETURNS
Name : Saurabh, Phone number : 9403338964
7. CLASS METHOD
@classmethod
def show_all_contact(cls):

This method works with:

shared class data

not one object.

That’s why class method is correct choice.

cls REFERS TO
Contact

class itself.

THIS CHECK
if len(cls.phone_directory) == 0:

Checks whether directory is empty.

LOOP
for contact in cls.phone_directory:

Each:

contact

becomes:

c1
c2
c3
c4

one-by-one.

THIS LINE
print(contact.show_contact())

calls instance method for each object.

8. STATIC METHOD
@staticmethod
def Validate_number(number):

This method:

does NOT use self
does NOT use cls

So static method is correct.

PURPOSE

Checks whether:

number length ≥ 8
all characters are digits
RETURNS
True

or

False
9. SEARCH METHOD
@classmethod
def search_contact(cls,search_name):

This searches shared directory.

Again:

class method is correct

because it works with entire contact book.

SEARCH FLOW
for contact in cls.phone_directory:

checks every object.

THIS CONDITION
if contact.name.lower() == search_name.lower():

makes search:

case-insensitive

Very good touch.

Example:

SAURABH
saurabh
Saurabh

all work.

RETURNS
The contact number for Saurabh is 9403338964
10. ADD CONTACT METHOD
@classmethod
def Add_contacts(cls):

Used for adding new contacts dynamically.

FLOW

Gets:

number of contacts
name
phone number

Then validates phone number.

THIS LINE
Contact(name,Phone_number)

creates NEW object.

And because constructor contains:

append(self)

new object automatically enters directory.

Very important design understanding.

11. PREDEFINED OBJECTS
c1 = Contact(...)
c2 = Contact(...)

These are initial contacts already stored in system.

12. MAIN PROGRAM LOOP
while True:

Creates:

infinite menu loop

Program keeps running until user exits.

MENU SYSTEM
1 Add
2 Show
3 Search
4 Exit

Classic menu-driven application design.

OPTION HANDLING
if option == 1
elif option == 2

Controls which feature executes.

PROGRAM FLOW SUMMARY
User chooses option
        ↓
Related class method runs
        ↓
Methods manipulate shared phone_directory
        ↓
Objects store actual contact data
OOP CONCEPTS USED
Concept	Where Used
Class	Contact
Objects	c1, c2, c3, c4
Instance Variables	self.name
Class Variable	phone_directory
Instance Method	show_contact()
Class Method	show_all_contact()
Static Method	Validate_number()
Constructor	__init__()
self	current object
cls	current class

"""