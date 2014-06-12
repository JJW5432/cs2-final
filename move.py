#!/usr/bin/python
print ""

from tic_lib import *
import cgi
import cgitb
cgitb.enable()

fs = cgi.FieldStorage()

<<<<<<< HEAD
input_board = Board.from_string(fs['board'].value)#given board as string
=======
input_board = Board.unserialize(fs['board'].value)#given board as string
<<<<<<< HEAD

over = Board.over()
if not over:
	move = input_board.randomMove()
>>>>>>> 2976aff8d7a3169df75869f92fd88047eee55238

=======

over = Board.over()
if not over:
	move = input_board.randomMove()

>>>>>>> 1e83fcc1d259b26dbdc0a192e224dc7f5ca4ad1f
	print move.num
else: print over
