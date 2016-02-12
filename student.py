import sys
import json
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
				self.bookissued = 0
				self.totalfine = 0
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

def add_student(w_list):
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
	for w in w_list:
		if  w['rollno'] == tempstudent.rollno :
			print "Student already exist "
			flag = False
			break
	#append Student to List if no same rollno found
	if flag == True:
		w_list.append(tempstudent.__dict__)
	return w_list

def del_student(w_list):
	rollno = raw_input("Enter RollNo of Student you wish to remove from Record: ")
	w_list = load_file_student()
	for w in w_list:
		if w['rollno'] == rollno.upper():
			if w['totalfine'] != 0 or w['bookissued'] < 5:
				print "Cannot Delete Student,Outstanding Issues,Contact Librarian"
			else :
				w_list.remove(w)
	return w_list