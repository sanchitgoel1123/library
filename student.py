import sys
import json
import reserve 
from operator import methodcaller


class JSONEncodable(object):
    def json(self):
        return vars(self)

class student(JSONEncodable):
			"""docstring for student"""
			def __init__(self, name, rollno, branch, semester, phoneno):
				super(student, self).__init__()
				self.name = name
				self.rollno = rollno
				self.branch = branch
				self.semester = semester
				self.phoneno = phoneno
			def __iter__(self):
				return iter(self._values)
def load_file_student():
	w_list = []
	try:
		with open('student.json', 'r') as f:
			w_list = json.load(f)
	except IOError:
		#File not opened
		print "IOError Generated"
	except EOFError:
		#File End Reached
		print "End Of file Reached"
	return w_list

def write_file_student(w_list):
	try:
		with open('student.json','wb') as f:
			json.dump(w_list,f,default=methodcaller("json"))
	except IOError:
		print "IOError Generated"

def add_student(studentlist):
	flag = True
	name = raw_input("Enter Name: ")
	rollno = raw_input("Enter RollNo: ")
	branch = raw_input("Enter Branch: ")
	semester = raw_input("Enter Semester: ")
	while (int(semester) > 8 or int(semester) < 1):
		print "Incorrect Semester.Enter Again"
		print semester
		semester = raw_input("Enter Semester: ")
	phoneno = raw_input("Enter Phoneno: ")
	tempstudent = student(name.upper(), rollno.upper(), branch.upper(), semester, phoneno)
	#traverse list of dictionaries of student
	for w in studentlist:
		if  w['rollno'] == tempstudent.rollno :
			print "Student already exist "
			flag = False
			break
	#append Student to List if no same rollno found
	if flag == True:
		return tempstudent
	return -1 

def del_student(reservations):
	rollno = raw_input("Enter RollNo of Student you wish to remove from Record: ")
	flag = 0
	for i in reservations:
		if(i['RollNo']==rollno and i['status']==True):
			print "First return the books/fine. Contact Librarian"
			flag = 1
	return flag
