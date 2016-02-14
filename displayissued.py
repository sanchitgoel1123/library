import book
import reserve



class DisplayIssued(object):
	"""docstring for DisplayIssued"""
	def __init__(self, bookid,DOI):
		super(DisplayIssued, self).__init__()
		self.bookid = bookid
		self.DOI = DOI


def get_reservedid(reservelist,rollno):
	Issued = []
	for i in reservelist:
		if i['RollNo'] == rollno.upper() and i['status'] == True:
			newbookreserve = DisplayIssued(i['bookId'],i['DOI'])
			Issued.append(newbookreserve.__dict__) 		
	return Issued