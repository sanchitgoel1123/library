import sys
import json
import reserve 
from operator import methodcaller


class JSONEncodable(object):
    def json(self):
        return vars(self)

class teacher(JSONEncodable):
			"""docstring for teacher"""
			def __init__(self, name, tid, phoneno):
				super(teacher, self).__init__()
				self.name = name
				self.tid = tid
				self.phoneno = phoneno
			def __iter__(self):
				return iter(self._values)
def load_file_teacher():
	w_list = []
	try:
		with open('teacher.json', 'r') as f:
			w_list = json.load(f)
	except IOError:
		#File not opened
		print "IOError Generated"
	except EOFError:
		#File End Reached
		print "End Of file Reached"
	return w_list

def write_file_teacher(w_list):
	try:
		with open('teacher.json','wb') as f:
			json.dump(w_list,f,default=methodcaller("json"))
	except IOError:
		print "IOError Generated"

def add_teacher(teacherlist):
	flag = True
	name = raw_input("Enter Name: ")
	tid = raw_input("Enter teacher Id: ")
	phoneno = raw_input("Enter Phoneno: ")
	tempteacher = teacher(name.upper(), tid ,phoneno)
	#traverse list of dictionaries of teacher
	for w in teacherlist:
		if  w['tid'] == tempteacher.tid :
			print "Teacher already exists in the database "
			flag = False
			break
	#append Student to List if no same rollno found
	if flag == True:
		return tempteacher
	return -1 

