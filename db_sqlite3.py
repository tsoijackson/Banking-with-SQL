import sqlite3

conn = sqlite3.connect('bank.db')
cursor  = conn.cursor()

def create_table():
	cursor.execute('CREATE TABLE IF NOT EXISTS bank_db(id TEXT, last TEXT, first Text, amt REAL)')


def data_entry(ID: str, last: str, first: str, amt: float):
	data = str((ID, last, first, amt))
	string_command = "INSERT INTO bank_db VALUES " + data
	cursor.execute(string_command)
	conn.commit()
	cursor.close()
	conn.close()

def fetchall():
	return cursor.execute("SELECT * FROM bank_db ORDER BY ID")

def remove_row(ID: str):
	string_command = "DELETE FROM bank_db WHERE id = " + ID
	cursor.execute(string_command)
	conn.commit()

def main():
        conn = sqlite3.connect('bank.db')
        cursor  = conn.cursor()
        create_table()
        data_entry("123456", "t", "j", 100)
        print("hello")

if __name__ == '__main__':
	main()
