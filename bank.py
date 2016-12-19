
import random, db_sqlite3, messages

def generate_id():
	id = ""
	for i in range(6):
		id += str(random.randint(0,9))
	return id

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

def delete_client():
	pass

def list_all_clients():
	pass


def main():
	pass

print("Hellooo")
print(add_client())

if __name__ == '__main__':
	main()