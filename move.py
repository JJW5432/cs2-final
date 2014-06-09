import tic_lib
import play

input_board = Board.from_string()#given board as string)

move = chooseMove(input_board)

cell = convertCell(move)

