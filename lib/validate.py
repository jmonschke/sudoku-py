
class Row(object):
	def __init__(self, board):
		self.__board = board

	def validate(self, row):
		print row

class Column(object):
	def __init__(self, board):
		self.__board = board

	def validate(self, column):
		print column

class Square(object):
	def __init__(self, board):
		self.__board = board

	def validate(self, square):
		print square
