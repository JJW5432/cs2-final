import tic_lib
import play
import cgi

fs = cgi.FieldStorage()

input_board = Board.from_string(fs['board'].value)#given board as string)

move = chooseMove(input_board)

cell = convertCell(move)

cell_to_num = lambda x,y: x-3*y+5

print cell_to_num(*cell.coords)
