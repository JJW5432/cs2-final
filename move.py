#!/usr/bin/python
print ""
from tic_lib import *
import cgi
import cgitb
cgitb.enable()

fs = cgi.FieldStorage()

input_board = Board.unserialize(fs['board'].value)#given board as string)

over = Board.over()
if not over:
	move = input_board.randomMove()

	print move.num
else: print over
