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
	print "5.Return a book"
	print "6.Display all lists"
	print "7.Exit"
	user_input = input()
	if user_input==1:
		testudent = student.add_student(studentlist) 
		if(testudent==-1):
			pass
		else:
			studentlist.append(testudent.__dict__)
	elif user_input==2:
		deleted = student.del_student(reservelist)
		if(deleted==0):
			#delete krde 
		else:
			pass
	elif user_input==3:
		newreserve = reserve.issue_book(reservelist,booklist)
		if(newreserve==-1):
			pass
		else:
			reservelist.append(newreserve.__dict__)
	elif user_input==4:
		newbook = book.add_book(booklist)
		booklist.append(newbook.__dict__)
	elif user_input==5:
		returned = reserve.return_book(reservelist)
		if(returned==-1):
			print "Enter valid information:"
	elif user_input==6:
		print studentlist
		print booklist
		print reservelist
	elif user_input==7:
		student.write_file_student(studentlist)
		book.write_file_book(booklist)
		reserve.res_write_file(reservelist)
		break
	

