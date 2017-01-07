
import random, db_sqlite3, messages

def generate_id():
	id = ""
	for i in range(6):
		id += str(random.randint(0,9))
	return id

def first_input():
	return input()[0]

def main_menu_input():
	i = first_input()
	if i.isalpha():
		if i.upper() == "A":
			add_client()
		elif i.upper() == "B":
			delete_client()
		elif i.upper() == "C":
			pass
		elif i.upper() == "D":
			list_all_clients()
			return None
		elif i.upper() == "E":
			remove_all_clients()
		elif i.upper() == "Q":
			return False
	else:
		print("Please choose a letter.")

def search_input():
	i = first_input()
	if i.isalpha():
		if i.upper() == "A":
			pass
		elif i.upper() == "B":
			pass
		else:
			print("Please choose an option from the menu.")
	else:
		print("Please enter letters ONLY.")

def search_options_input():
	i = first_input()

def add_client():
	while True:
		first = input("Please enter the FIRST name.")
		if first.isalpha():
			break
		else:
			print("Please enter letters ONLY.")
		break

	while True:
		last = input("Please enter the LAST name.")
		if last.isalpha():
			break
		else:
			print("Please enter letters ONLY.")

	while True:
		try:
			amt = input("Please enter the starting amount of money.")
			float(amt)
			break
		except:
			print("Please enter a number.")

	db_sqlite3.data_entry(str(generate_id()), first, last, amt)

	print("CLIENT ADDED")

def delete_client():
	messages.print_search()
	i = input()
	if i.upper() == "A":
		db_sqlite3.remove_row(i)
		print("Client deleted.")
	elif i.upper()  == "Q":
		pass

def ask_client_ID():
	return input()


def list_all_clients():
	empty = False
	for row in db_sqlite3.fetchall():
		empty = True
		print(row)
	if empty  == False:
		print("No one in the database.")

def remove_all_clients():
	print("Removing all clients...")
	db_sqlite3.remove_all_rows()
	print("All clients removed.")


def main():
	messages.print_welcome()
	while True:
		messages.print_main_menu()
		if main_menu_input() == False:
			break



	messages.print_farewell()

def main2():
	delete_client("11111")


if __name__ == '__main__':
	main()
