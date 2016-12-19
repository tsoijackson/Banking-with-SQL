"""
This will contain all of the general messages utilizes through the menu UI
"""

def welcome():
	return "Welcome to the Bank! How may we help you?"

def farewell():
	return "Goodbye and have a nice day! Come again soon!"

def main_menu():
	message = """----------MAIN MENU----------
A. Add client
B. Delete client
C. Change client information
Q. Quit
"""
	return message

def client_menu():
	message = """----------CLIENT MENU----------
A. Deposit money
B. Retrieve money
C. Set new amount
Q. Quit
"""
	return message