from Models import books_database


class books_controller:
	def __init__(self, connection):
		self.books_database = books_database.books_database(connection=connection)
