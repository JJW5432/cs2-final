#!/usr/bin/python
print ""
from tic_lib import *
import cgi
import cgitb
cgitb.enable()

fs = cgi.FieldStorage()

input_board = Board.from_string(fs['board'].value)#given board as string)

move = input_board.randomMove()

cell_to_num = lambda x,y: x-3*y+5

print cell_to_num(*move.coords)
