import sys
import json
import time
from operator import methodcaller

import student
import book

class JSONEncodable(object):
    def json(self):
        return vars(self)

class reserve(JSONEncodable):
	""" assume fine begins 2 weeks after the Date of issue"""
	def __init__(self,bookId,RollNo,DOI):
		self.bookId = bookId 
		self.RollNo = RollNo
		self.DOI = DOI
		self.status = True  # true implies book has not been returned . false implies book is with library
	def __iter__(self):
				return iter(self._values)

def res_load_file():
	w_list = []
	try:
		with open('res.json', 'r') as f:
			w_list = json.load(f)
	except IOError:
		#File not opened
		print "IOError Generated load"
	except EOFError:
		#File End Reached
		print "End Of file Reached"
	return w_list

def res_write_file(w_list):
	try:
		with open('res.json','wb') as f:
			json.dump(w_list,f,default=methodcaller("json"))
	except IOError:
		print "IOError Generated write" 

def issue_book(reservations,booklist):
	RollNo = raw_input("Enter your RollNo: ")
	Title = raw_input("Enter title of book you want to issue: ")
	reservations = issue_bookhelp(RollNo,Title,reservations,booklist)
	return reservations

def issue_bookhelp(RollNo,Title,reservations,booklist):
	count = 0
	for i in reservations:
		if(i['RollNo'] == RollNo.upper() and i['status'] == True):
			count = count + 1

	if(count > 5):
		print "Sorry ! A student can only issue 5 books at a time."
	else:
		bookids = []
		issued = False
		bookids = book.get_bookids(Title,booklist)
		for i in bookids:
			currid = i
			flag = True 
			for j in reservations:
				if(j['status'] == True):
					flag = False 

			if(flag == True):
				newreserve = reserve(i,RollNo,time.strftime("%x"))
				reservations.append(newreserve.__dict__) 
				issued = True
				break

		if(issued == True):
			print "Book not available"
	return reservations

def return_book(RollNo,bookId):
	pass 


