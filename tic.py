a_board = [['1','2', '3'],['4','5','6'],['7', '8', '9']]
def display(board,sep=''):
	"""displays a textual representation of a board (for dev purposes)
	>>> display(a_board)
	1|2|3
	4|5|6
 	7|8|9
	"""
	for row in board:
		print "|".join(row)
	if len(sep) > 0: print sep

def rotate(board,n=1):
	"""rotates a given board clockwise 90 degrees n times
	>>> display(rotate(a_board))
	7|4|1
	8|5|2
	9|6|3
	>>> display(rotate(a_board,2))
	9|8|7
	6|5|4
	3|2|1
	>>> rotate(a_board,4)==a_board
	True
	"""
	for x in range(n):
		board = [[row[n] for row in board][::-1] for n in range(len(board))]
	return board

def reflect(board,d):
	"""reflects board accross vertical ('v'), horizontal ('h'), top-left to bottom-right diagonal ('l'), or top-right to bottom-left diagonal ('r')
	>>> display(reflect(a_board,'v'))
	3|2|1
	6|5|4
	9|8|7
	>>> display(reflect(a_board,'h'))
	7|8|9
	4|5|6
	1|2|3
	>>> display(reflect(a_board,'l'))
	1|4|7
	2|5|8
	3|6|9
	>>> display(reflect(a_board,'r'))
	9|6|3
	8|5|2
	7|4|1
	"""
	if d == 'v': #vertical
		return [row[::-1] for row in board]
	elif d == 'h': #horizontal
		return board[::-1]
	elif d =='l': #top-left to bottom-right
		return [[row[n] for row in board] for n in range(len(board))]
	elif d == 'r': #top-right to bottom-left
		return [[row[-(n+1)] for row in board][::-1] for n in range(len(board))]

def isoboards(board):
	"""returns a list of all equivelant boards"""
	return [board, rotate(board), rotate(board,2), rotate(board,3), reflect(board,'v'), reflect(board,'h'), reflect(board,'l'), reflect(board,'r')]

def isomorphic(board1, board2):
	return board1 in isoboards(board2)

if __name__ == "__main__":
	import doctest
	doctest.testmod()
