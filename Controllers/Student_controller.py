from tabulate import tabulate
from Models import Student_database


class Student_controller:
	def __init__(self, connection):
		self.student_database = Student_database.Student_database(connection=connection)

	def add_student(self):
		student_name = input("Enter Student Name : ")
		roll_no = input("Enter Student Roll No : ")
		father_name = input("Enter Father Name : ")
		mother_name = input("Enter Mother Name : ")
		check = self.student_database.check_student(rollno=roll_no)
		if check is True:
			print("Student With This Roll No already Exists.")
		elif check is False:
			self.student_database.add_student(student_name, father_name, mother_name, roll_no)

	def list_students(self):
		data = self.student_database.list_students()
		if data:
			print(tabulate(data, headers=["id", "Name", "FatherName", "MotherName", "RollNo"]))
		else:
			print("No Students Record Found")

	def search_student_name(self):
		student_name = input("Enter Student Name to Search : ")
		data = self.student_database.search_student_name(student_name)
		if data:
			print(tabulate(data, headers=["id", "Name", "FatherName", "MotherName", "RollNo"]))
		else:
			print("No student with this name found")

	def search_student_rollno(self):
		student_rollno = input("Enter Student Roll to Search : ")
		data = self.student_database.search_student_rollno(studentrollno=student_rollno)
		if data:
			print(f"Student Id : {data[0]}")
			print(f"Student Name : {data[1]}")
			print(f"Student Father Name : {data[2]}")
			print(f"Student Mother Name : {data[3]}")
			print(f"Student Roll No : {data[4]}")
		else:
			print("No student with this roll no found")

	def delete_student(self):
		student_rollno = input("Enter Student Roll No to Delete : ")
		check_student = self.student_database.check_student(student_rollno)
		if check_student is True:
			self.student_database.delete_student(student_rollno)
			print(f"Student {student_rollno} was deleted succesfully")
		elif check_student is False:
			print("No Student with this Roll No Exists")

	def update_student(self):
		student_rollno = input("Enter Student Roll you want to Update : ")
		check_student = self.student_database.check_student(student_rollno)
		if check_student is True:
			student_name = input("Update Student Name : ")
			father_name = input("Update Student Father Name : ")
			mother_name = input("Update Student Mother Name :")
			self.student_database.update_student(student_name=student_name, father_name=father_name,
			                                     mother_name=mother_name, roll_no=student_rollno)
			print(f"Student {student_rollno} was updated succesfully")
		elif check_student is False:
			print("No Student with This Roll No Found")
