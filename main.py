from Database import Database_class
from Controllers import Student_controller
import os


def init():
	databaseobject = Database_class.Database()
	connection = databaseobject.create_connection(databasename="database.db")
	databaseobject.create_tables()
	studentcontroller = Student_controller.Student_controller(connection=connection)
	return [studentcontroller]


def Search_Student(studentcontroller):
	userinput = input("Press\n"
	                  "'SN' to Search by Student Name\n"
	                  "'SR' to Search by Student Roll No\n"
	                  "'Q' to return to Mainmenu\n"
	                  " : ")
	while userinput != 'Q':
		if userinput == 'SN':
			studentcontroller.search_student_name()
		elif userinput == "SR":
			studentcontroller.search_student_rollno()
		userinput = input("Press\n"
		                  "'SN' to Search by Student Name\n"
		                  "'SR' to Search by Student Roll No\n"
		                  "'Q' to return to Mainmenu\n"
		                  " : ")


def Student(studentcontroller):
	clear = lambda: os.system('cls')
	userinput = input("Press\n"
	                  "'A' to Add a Student\n"
	                  "'L' to List all Students\n"
	                  "'S' to Search a Student\n"
	                  "'D' to Delete a Student\n"
	                  "'U' to Update a Student\n"
	                  "'Q' to return to Mainmenu\n"
	                  " : ")
	while userinput != 'Q':
		if userinput == 'A':
			studentcontroller.add_student()
		elif userinput == "L":
			studentcontroller.list_students()
		elif userinput == "S":
			Search_Student(studentcontroller)
		elif userinput == 'D':
			studentcontroller.delete_student()
		elif userinput == "U":
			studentcontroller.update_student()
		else:
			print("Wrong Command")
		userinput = input("Press\n"
		                  "'A' to Add a Student\n"
		                  "'L' to List all Students\n"
		                  "'S' to Search a Student\n"
		                  "'D' to Delete a Student\n"
		                  "'U' to Update a Student\n"
		                  "'Q' to return to Mainmenu\n"
		                  " : ")


def mainmenu(controller_objects):
	userinput = input("Press\n"
	                  "'S' to open Student Section\n"
	                  "'T' to open Teacher Section\n"
	                  "'B' to open Books Section\n"
	                  "'Q' to exit the program\n"
	                  " : ")
	while userinput != 'Q':
		if userinput == 'S':
			Student(controller_objects[0])
		elif userinput == 'T':
			pass
		elif userinput == 'B':
			pass
		else:
			print("Wrong Command")
		userinput = input("Press\n"
		                  "'S' to open Student Section\n"
		                  "'T' to open Teacher Section\n"
		                  "'B' to open Books Section\n"
		                  "'Q' to exit the program\n"
		                  " : ")


def main():
	controller_objects = init()
	mainmenu(controller_objects)


main()
