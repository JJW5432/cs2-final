#!/usr/bin/python
from play_lib import *
from datetime import datetime

board = Board()
short_term = []

while True:
    if not board.over:
        moves = readMem(board)
        move = chooseMove(moves)
        short_term.append('"' + board.serialize() + '",' + str(move.num) + ',1,-1,')
        board.move(move.with_state(1))
        board = ~board
    else:
        now = str(datetime.now())
        long_term = open('./memory.csv', 'a')
        for entry in short_term:
            long_term.write(entry + now + '\n')
        long_term.close()
        board = Board()
        short_term = []
