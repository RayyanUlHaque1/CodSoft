# Description of the Code
The code provided is a basic contact management system [contact book] where a user can perform several actions related to contact details (name, age, e-mail, and mobile number). 

# Below is an explanation of the operators, logic, and actions in the code:

# Key Concepts and Operators Used
Dictionary (contacts):

The contacts dictionary is storing contact information. It maps the contact's name (as the key) to a dictionary containing the contact's age, email, and mobile number (as values).

While Loop (while True):The program uses an infinite while loop to continuously display the menu until the user chooses to exit.
This ensures that the program keeps running until the user explicitly decides to quit.
# User Input (input()):

The input() function is used to get user input for performing various operations, such as adding a contact, searching, updating, etc.
Conditionals (if, elif, else):if, elif, and else are used for branching and decision-making in the program. Based on the user's input, the program will perform different actions.
Like : if choose == '1': determines whether to add a contact.
Logical Comparison (==, in):==: Used to check equality.Like, choose == '1' checks if the user selected option 1.in: Used to check if a specific item exists in a collection. Like if name in contacts: checks whether a contact already exists in the dictionary.
Assignment Operator (=):Used for assigning values to variables.Like, contacts[name] = {'age': age, 'email': email, 'mobile': phone_no} assigns the contact details to the dictionary under the key name.
Input Type Conversion (int()):Used to convert input into integers, such as converting the age and phone number into integers for proper data handling.
Example: age = int(input('Enter Contacts Age: ')).
Deletion (del):The del statement is used to remove an item from the dictionary. Like, del contacts[name] deletes a contact from the contacts dictionary.
Looping (for):A for loop is used in the search function to iterate over all contacts in the contacts dictionary.
Example: for name, contact in contacts.items(): allows iterating over each contact's name and details.
Boolean Flag (found):The found variable is used in the search functionality to check whether a contact has been found and avoid printing a "not found" message multiple times.
Example: if S_name.lower() in name.lower(): checks if the search name matches part of the contact name (case-insensitive).
Print Statements:print() is used to display messages and results to the user, such as the contact details or displayed message like "Contact added successfully."
Example: print(f'Contact name ({name}) is added successfully: ').
Exit Condition (break):The break statement is used to exit the while loop and stop the program when the user selects the "Exit".
Example: elif choose == '7': break exits the loop.
# Key Operations and Features
# 1. Add Contact (1):
The user have to enter the contact details (name, age, email, mobile).
If the contact already exists, a message is displayed, otherwise, the contact is added to the contacts dictionary.
# 2. View Contact (2):
The user have to enter the contact name. If the contact exists, it displays the contact details, including name, age, email, and mobile number.
# 3. Delete Contact (3):
The user have to enter the contact name they wish to delete. If the contact exists, it is removed from the contacts dictionary.
# 4. Search Contact (4):
The user have to enter a name to search for. The program checks if any contact's name contains the search string (case-insensitive), and if found, displays the details.
else displayed message contact not found ...
# 5. Update Contact (5):
The user have to enter the contact name they want to update. If the contact exists, they can modify the age, email, and mobile number.
# 6. Total Contacts (6):
The program calculates the number of contacts in the contacts dictionary using len(contacts) and displays the result.
# 7. Exit (7):
The program terminates the loop and ends the program.

