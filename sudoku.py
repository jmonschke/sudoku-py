from lib.validate import Row, Square
from models.gameboard import Sudoku

def main():
	board = Sudoku()
	validateRow = Row()

	map(validateRow.validate, board.board)
	print board.board
	print "jeff"


if __name__ == '__main__':
    main()