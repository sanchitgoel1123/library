



def printstudents(studentlist):
	for i in studentlist:
		print "\tName:   \t"+i['name']
		print "\tRollNo: \t"+i['rollno']
		print "\tSem:    \t"+i['semester']
		print "\tBranch: \t"+i['branch']
		print "\tPhoneNo:\t"+i['phoneno']
		print "\n"
def printbooks(booklist):
	for i in booklist:
		print "\tName:   \t"+i['title']
		print "\tISBN:   \t"+i['isbn']
		print "\tPub:    \t"+i['publisher']
		print "\tBookId: \t"+i['bookid']
		s = ""
		for j in i['authors']:
			s = s + j
			s = s + "  -  "
		print "\tAuthors:\t"+s
		print "\n"