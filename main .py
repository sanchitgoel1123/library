import student
import sys
import book 
import reserve
import shutil


studentlist = []
booklist = []
reservelist = []
teacherlist = []
studentlist = student.load_file_student()
teacherlist = teacher.load_file_teacher()
booklist = book.load_file_book()
reservelist = reserve.res_load_file()

while(True):
	#sys.stderr.write("\x1b[2J\x1b[H")
	print "==========================Welcome to Library Management System :=================================\n"
	print "\tEnter an input:\n"
	print "\t1.Add a student:"
	print "\t2.Remove a student:"
	print "\t3.Issue a book:"
	print "\t4.Add a new book:"
	print "\t5.Return a book"
	print "\t6.Display all lists"
	print "\t7.Add a teacher"
	print "\t8.Issue book to teacher"
	print "\t9.Return a book - teacher"
	print "\t10.Create a backup of current data"
	print "\t11.Exit"
	print "\t\t"
	user_input = input()
	if user_input==1:
		testudent = student.add_student(studentlist) 
		if(testudent==-1):
			pass
		else:
			studentlist.append(testudent.__dict__)
	elif user_input==2:
		rollno = raw_input("Enter RollNo of Student you wish to remove from Record: ")
		deleted = student.del_student(reservelist,rollno)
		if(deleted==0):
			#delete krde 
			for i in studentlist:
				if i['rollno'] == rollno.upper():
					studentlist.remove(i) 
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
		testeacher = teacher.add_teacher(teacherlist) 
		if(testeacher==-1):
			pass
		else:
			teacherlist.append(testeacher.__dict__)
	elif user_input==8:
		newreserve = reserve.tissue_book(reservelist,booklist)
		if(newreserve==-1):
			pass
		else:
			reservelist.append(newreserve.__dict__)
	elif user_input==9:
		returned = reserve.treturn_book(reservelist)
		if(returned==-1):
			print "Enter valid information:"
	elif user_input==10:
		student.write_file_student(studentlist)
		book.write_file_book(booklist)
		reserve.res_write_file(reservelist)
		teacher.write_file_teacher(teacherlist)
		shutil.copy2('teacher.json','backupteacher.json')
		shutil.copy2('student.json','backupstudent.json')
		shutil.copy2('book.json','backupbook.json')
		shutil.copy2('res.json','backupres.json')
	elif user_input==11:
		student.write_file_student(studentlist)
		book.write_file_book(booklist)
		reserve.res_write_file(reservelist)
		break
	

