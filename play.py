#!/usr/bin/python
print "Content-Type: text/html\n"
print ""

#import random
from play_lib import *
import cgi
import cgitb
cgitb.enable()
fs = cgi.FieldStorage()

board = Board.unserialize(fs['board'].value) # given board as string
#board = Board.unserialize('-1,0,0,0,0,0,0,0,0')

if not board.over:
    moves = readMem(board)
    move = chooseMove(moves)
        
    board.move(move.with_state(1))

    if board.over:
        if type(board.over) is list: 
            print "computer"
            print ','.join([cell.num for cell in board.over])
        else: #tie
            print "tie"

else: #twas lost before it began
    print "user"
    print ','.join([cell.num for cell in board.over])
