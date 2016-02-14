import student
import sys
import book 
import reserve
import shutil
import teacher
import displayissued
import getpass


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
	print "==========================Welcome to Library Management System=================================\n"
	print "\tEnter an input:\n"
	print "\t1.Add a student:"
	print "\t2.Remove a student:"
	print "\t3.Issue a book:"
	print "\t4.Add a new book:"
	print "\t5.Return a book"
	print "\t6.Display issued books"
	print "\t7.Add a teacher"
	print "\t8.Issue book to teacher"
	print "\t9.Return a book - teacher"
	print "\t10.Search all Books"
	print "\t11.Create a backup of current data"
	print "\t12.Exit"
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
		print teacherlist
		user_type = raw_input("Are You ADMIN or STUDENT? : ")
		if user_type.upper() == "STUDENT":
			rollno = raw_input("Enter your Rollno: ")
			issued = []
			issued = displayissued.get_reservedid(reservelist,rollno)
			print "\n"
			for j in issued:
				for i in booklist:
					if i['bookid'] == j['bookid']:
						print "\tDate of Issue is%s.Remeber a Book is only Valid 14 Days from DOI"%j['DOI']
						print "\tTitle of book is %s \n \tPublisher is %s \n \tEdition is %s\n\tBookID code is %s\t"%(i['title'],i['publisher'],i['edition'],i['bookid'])
						print "\tAuthors are:   ",
						for authors in i['authors']:
							print "%s\n\t\t\t"%authors,
		elif user_type.upper() == "ADMIN":
			password = getpass.getpass()
			if password.upper() == "PASSWORD":
				for i in reservelist:
					if i['status'] == True:
						print "\tIssued on %s,Issued by %s,Bookid issued is %s"%(i['DOI'],i['RollNo'],i['bookId'])
			else:
				print "Incorrect Password"

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
		print "====================Search Book Database==============================================\n\n"
		print "\tSearch Book by?:\n"
		print "\t1.Title"
		print "\t2.ISBN"
		print "\t3.Author"
		print "\t4.Publisher"
		search_input = input()
		if search_input==1:
			flag = 0
			title=raw_input("Enter Title of book to search?:")
			for i in booklist:
				if i['title'] == title.upper():
					flag = 1
					print "\n\n\tTitle of book is %s \n \tPublisher is %s \n \tEdition is %s\n\tBookID code is %s\t"%(i['title'],i['publisher'],i['edition'],i['bookid'])
					print "\tAuthors are:   ",
					for authors in i['authors']:
						print "%s\n\t\t\t"%authors,
					print "\n"
			if flag == 0:
				print "\nNo Such Book Found.\n"
		elif search_input==2:
			flag = 0
			isbn=raw_input("Enter ISBN of book to search?:")
			for i in booklist:
				if i['isbn'] == isbn.upper():
					flag = 1
					print "\n\tTitle of book is %s \n \tPublisher is %s \n \tEdition is %s\n\tBookID code is %s\t"%(i['title'],i['publisher'],i['edition'],i['bookid'])
					print "\tAuthors are:   ",
					for authors in i['authors']:
						print "%s\n\t\t\t"%authors,
					print "\n"
			if flag == 0:
				print "\nNo Such Book Found.\n"
		elif search_input==3:
			flag = 0
			search_authors = raw_input("Enter name of author to search for?: ")
			for i in booklist:
				for authors in i['authors']:
					if authors == search_authors.upper():
						flag = 1
						print "\n\tTitle of book is %s \n \tPublisher is %s \n \tEdition is %s\n\tBookID code is %s\t"%(i['title'],i['publisher'],i['edition'],i['bookid'])
						print "\tAuthors are:   ",
						for authors in i['authors']:
							print "%s\n\t\t\t"%authors,
			if flag == 0:
				print "\nNo Such Book Found.\n"		
		elif search_input==4:
			flag = 0
			publisher=raw_input("Enter Publisher of book to search?:")
			for i in booklist:
				if i['publisher'] == publisher.upper():
					flag = 1
					print "\n\n\tTitle of book is %s \n \tPublisher is %s \n \tEdition is %s\n\tBookID code is %s\t"%(i['title'],i['publisher'],i['edition'],i['bookid'])
					print "\tAuthors are:   ",
					for authors in i['authors']:
						print "%s\n\t\t\t"%authors,
					print "\n"
			if flag == 0:
				print "\nNo Such Book Found.\n"

	elif user_input==11:
		student.write_file_student(studentlist)
		book.write_file_book(booklist)
		reserve.res_write_file(reservelist)
		teacher.write_file_teacher(teacherlist)
		shutil.copy2('teacher.json','backupteacher.json')
		shutil.copy2('student.json','backupstudent.json')
		shutil.copy2('book.json','backupbook.json')
		shutil.copy2('res.json','backupres.json')
	elif user_input==12:
		student.write_file_student(studentlist)
		book.write_file_book(booklist)
		reserve.res_write_file(reservelist)
		teacher.write_file_teacher(teacherlist)
		break
	

