from Ui import student_screen
from Ui import books_screen


def mainmenu(controller_objects):
	userinput = input("Press\n"
	                  "'S' to open Student Section\n"
	                  "'T' to open Teacher Section\n"
	                  "'B' to open Books Section\n"
	                  "'Q' to exit the program\n"
	                  " : ")
	while userinput != 'Q':
		if userinput == 'S':
			student_screen.Student(controller_objects[0])
		elif userinput == 'T':
			pass
		elif userinput == 'B':
			books_screen.Books(bookscontroller=controller_objects[1])
		else:
			print("Wrong Command")
		userinput = input("Press\n"
		                  "'S' to open Student Section\n"
		                  "'T' to open Teacher Section\n"
		                  "'B' to open Books Section\n"
		                  "'Q' to exit the program\n"
		                  " : ")
