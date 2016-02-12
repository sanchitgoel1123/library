import student
import book 
import reserve
print "Welcome to Library Management System :\n"

studentlist = []
booklist = []
reservelist = []
studentlist = student.load_file_student()
booklist = book.load_file_book()
reservelist = reserve.res_load_file()

while(True):
	print "Enter an input:"
	print "1.Add a student:"
	print "2.Remove a student:"
	print "3.Issue a book:"
	print "4.Add a new book:"
	print "5.Display all lists"
	print "7.Exit"
	user_input = input()
	if user_input==1:
		studentlist = student.add_student(studentlist) 
	elif user_input==2:
		studentlist = student.del_student(studentlist)
	elif user_input==3:
		reservelist = reserve.issue_book(reservelist,booklist)
	elif user_input==4:
		booklist = book.add_book(booklist)
	elif user_input==5:
		print studentlist
		print booklist
		print reservelist
	elif user_input==7:
		student.write_file_student(studentlist)
		book.write_file_book(booklist)
		reserve.res_write_file(reservelist)
		break
	

