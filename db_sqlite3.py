import sqlite3

conn = sqlite3.connect('bank.db')
cursor  = conn.cursor()

def close_connection():
	cursor.close()
	conn.close()

def create_table():
	cursor.execute('CREATE TABLE IF NOT EXISTS bank_db(id TEXT, last TEXT, first Text, amt REAL)')

def data_entry(ID: str, last: str, first: str, amt: float):
	create_table()
	data = str((ID, last, first, amt))
	string_command = "INSERT INTO bank_db VALUES " + data
	cursor.execute(string_command)
	conn.commit()

def fetch_amt(ID: str):
	string_command = "SELECT amt FROM bank_db WHERE id = " + ID
	for i in cursor.execute(string_command):
		return i[0]

def fetchall():
	create_table()
	return cursor.execute("SELECT * FROM bank_db ORDER BY ID")

def remove_row(ID: str):
	string_command = "DELETE FROM bank_db WHERE id = " + ID
	cursor.execute(string_command)
	conn.commit()

def remove_all_rows():
	try:
		cursor.execute("DROP TABLE bank_db")
	except:
		pass


def add_amt(ID: str, amt: float):
	new_amt  = fetch_amt(ID) + amt
	string_command = """
	UPDATE bank_db
	SET amt = {new_amt}
	WHERE ID = {ID}
	""".format(new_amt = new_amt, ID = ID)
	cursor.execute(string_command)
	conn.commit()

def sub_amt(ID: str, amt: float):
	new_amt = fetch_amt(ID) - amt
	string_command = """
	UPDATE bank_db
	SET amt = {new_amt}
	WHERE ID = {ID}
	""".format(new_amt = new_amt, ID = ID)
	cursor.execute(string_command)
	conn.commit()

def set_amt(ID: str, new_amt: float):
	string_command = """
	UPDATE bank_db
	SET amt = {new_amt}
	WHERE ID = {ID}
	""".format(new_amt = new_amt, ID = ID)
	cursor.execute(string_command)
	conn.commit()

def main():
        conn = sqlite3.connect('bank.db')
        cursor  = conn.cursor()
        create_table()
        data_entry("123456", "t", "j", 100)
        #print("hello")
        #remove_all_rows()
        f = fetch_amt("123456")
        print(f)
        add_amt("123456", 50)
        sub_amt("123456", 25)
        set_amt("123456", 300)
        f = fetch_amt("123456")
        print(f)

if __name__ == '__main__':
	main()
