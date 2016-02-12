import sys
import json
from operator import methodcaller
import datetime

class JSONEncodable(object):
    def json(self):
        return vars(self)

class book(JSONEncodable):
			"""docstring for books"""
			def __init__(self,isbn,title,authors,edition,publisher,bookid):
				super(book, self).__init__()
				self.isbn = isbn.upper()
				self.title = title.upper()
				self.authors = authors
				self.edition = edition
				self.publisher = publisher.upper()
				self.bookid = bookid
			def __iter__(self):
				return iter(self._values)

def load_file_book():
	w_list = []
	try:
		with open('book.json', 'r') as f:
			w_list = json.load(f)
	except IOError:
		#File not opened
		print "IOError Generated"
	except EOFError:
		#File End Reached
		print "End Of file Reached"
	return w_list

def write_file_book(w_list):
	try:
		with open('book.json','wb') as f:
			json.dump(w_list,f,default=methodcaller("json"))
	except IOError:
		print "IOError Generated"

def add_book(booklist):
	isbn = raw_input("Enter ISBN: ")
	title = raw_input("Enter Title Of the Book: ")
	publisher = raw_input("Enter book publisher: ")	
	authors = []
	author_count = raw_input("Enter No of Authors of Book: ")
	for i in range(0,int(author_count)):
		tempauthor = raw_input("Enter Author:")
		authors.append(tempauthor.upper())
	edition = raw_input("Enter Edition of Book: " )
	count = 0 
	for w in booklist:
		if w['isbn'] == isbn.upper():
			count = count + 1 ;
	bookid = isbn + str(count) 
	tempbook = book(isbn,title,authors,edition,publisher,bookid)
	booklist.append(tempbook.__dict__)
	return booklist

def get_bookids(title,booklist):
	bookIds = []
	for i in booklist:
		if(i['title']==title.upper()):
			bookIds.append(i['bookid'])
	return bookIds 
	

def num_copies(title,booklist):
	count = 0
	for i in booklist:
		if(i['title']==title.upper()):
			count = count + 1
	return count 