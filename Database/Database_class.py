import sqlite3


class Database:

	def __init__(self):
		self.connection = None

	def create_connection(self, databasename):
		try:
			self.connection = sqlite3.connect(databasename)
			if self.connection is not None:
				return self.connection
			else:
				raise ConnectionError
		except ConnectionError as e:
			print(e)

	def create_tables(self):
		cursor = self.connection.cursor()
		cursor.execute(
			"CREATE TABLE IF NOT EXISTS students(id integer PRIMARY KEY,name text NOT NULL,fathername text NOT NULL,mothername text NOT NULL,rollno text NOT NULL UNIQUE)")
		self.connection.commit()
