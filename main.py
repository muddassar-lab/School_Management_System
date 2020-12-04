from Database import Database_class
from Controllers import Student_controller
from Ui import main_screen


def init():
	databaseobject = Database_class.Database()
	connection = databaseobject.create_connection(databasename="database.db")
	databaseobject.create_tables()
	studentcontroller = Student_controller.Student_controller(connection=connection)
	return [studentcontroller]


def main():
	controller_objects = init()
	main_screen.mainmenu(controller_objects)


main()
