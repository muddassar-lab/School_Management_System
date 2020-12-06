from Database import Database_class
from Controllers import Student_controller
from Controllers import books_controller
from Ui import main_screen


def init():
	databaseobject = Database_class.Database()
	connection = databaseobject.create_connection(databasename="database.db")
	databaseobject.create_tables()
	studentcontroller = Student_controller.Student_controller(connection=connection)
	bookscontroller = books_controller.books_controller(connection=connection)
	return [studentcontroller, bookscontroller, databaseobject]


# Main Function
def main():
	controller_objects = init()
	main_screen.mainmenu(controller_objects)
	controller_objects[2].close_connection()


main()
