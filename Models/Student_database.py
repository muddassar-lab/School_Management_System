class Student_database:
	def __init__(self, connection):
		self.connection = connection

	def add_student(self, name, father_name, mother_name, roll_no):
		cursor = self.connection.cursor()
		cursor.execute(
			f"INSERT INTO students(name,fathername,mothername,rollno) "
			f"VALUES('{name}','{father_name}','{mother_name}','{roll_no}')")
		self.connection.commit()

	def list_students(self):
		cursor = self.connection.cursor()
		cursor.execute("SELECT * FROM students")
		data = cursor.fetchall()
		return data

	def search_student_name(self, studentname):
		cursor = self.connection.cursor()
		cursor.execute("SELECT * FROM students WHERE name=?", (studentname,))
		data = cursor.fetchall()
		return data

	def search_student_rollno(self, studentrollno):
		cursor = self.connection.cursor()
		cursor.execute("SELECT * FROM students WHERE rollno=? ", (studentrollno,))
		data = cursor.fetchone()
		return data

	def delete_student(self, studentrollno):
		cursor = self.connection.cursor()
		cursor.execute("DELETE FROM students WHERE rollno=?", (studentrollno,))
		self.connection.commit()

	def update_student(self, student_name, father_name, mother_name, roll_no):
		cursor = self.connection.cursor()
		cursor.execute("UPDATE students SET name=?,fathername=?,mothername=? WHERE rollno=?",
		               (student_name, father_name, mother_name, roll_no))
		self.connection.commit()

	def check_student(self, rollno):
		cursor = self.connection.cursor()
		cursor.execute("SELECT * FROM students WHERE rollno=?", (rollno,))
		data = cursor.fetchone()
		if data:
			return True
		else:
			return False
