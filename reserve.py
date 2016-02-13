import sys
import json
import datetime
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
	res_write_file(reservations)
	return reservations

def issue_bookhelp(RollNo,Title,reservations,booklist):
	count = 0
	for i in reservations:
		if(i['RollNo'] == RollNo.upper() and i['status'] == True):
			count = count + 1

	if(count > 5):
		print "Sorry ! A student can only issue 5 books at a time."
		return -1
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
				newreserve = reserve(i,RollNo,datetime.datetime.now())
				issued = True
				break

		if(issued == False):
			print "Book not available"
			return -1
	return newreserve

def cal(dor,doi):
	diff = int((dor-doi).total_seconds()) 
	diff = diff/86400
	diff = diff - 14 
	if(diff>0):
		return diff
	return 0

def return_book(reservations):
	RollNo = raw_input("Enter your RollNo: ")
	bookId = raw_input("Enter your bookId: ")
	for i in reservations:
		if(i['RollNo']==RollNo and i['bookId']==bookId):
			if(i['status']==True):
				i['status']=False
				fine = cal(datetime.datetime.now(),i['DOI'])
				print "Fine levied is " + str(fine)
				return i 
				break
	return -1


