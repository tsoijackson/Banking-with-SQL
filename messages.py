"""
This will contain all of the general messages utilizes through the menu UI
"""

def print_welcome():
	print("Welcome to the Bank! How may we help you?")

def print_farewell():
	print("Goodbye and have a nice day! Come again soon!")

def print_main_menu():
	message = """----------MAIN MENU----------
A. Add client
B. Delete client
C. Change client information
Q. Quit
"""
	print(message)

def print_client_menu():
	message = """----------CLIENT MENU----------
A. Deposit money
B. Retrieve money
C. Set new amount
Q. Quit
"""
	print(message)

def print_search():
	message  = """----------OPTIONS----------
A. Enter Id (6 digits)
B. Search by last name
"""
	print(message)

def print_search_options():
	message = """----------OPTIONS----------
A. Enter Id (6 digits)
B. New search by last name
C. Add first name to the search
"""
	print(message)

def print_letter_ONLY():
	print("Please enter letters ONLY.")