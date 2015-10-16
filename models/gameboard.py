
class Sudoku(object):
	def __init__(self):
		self.board = [[i+1 for i in range(9)] for j in range(9)]
		# print self.board