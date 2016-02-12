import student
import book 
import reserve
print "Welcome to Library Management System :\n"

while(True):
	print "Enter an input:"
	print "1.Add a student:"
	print "2.Remove a student:"
	print "3.Issue a book:"
	print "4.Add a new book:"
	print "7.Exit"
	user_input = input()
	if user_input==1:
		student.add_student() 
	elif user_input==2:
		student.del_student()
	elif user_input==3:
		reserve.issue_book()
	elif user_input==4:
		book.add_book()
	elif user_input==7:
		break
	

