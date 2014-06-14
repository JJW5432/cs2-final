#!/usr/bin/python
from play_lib import *
from datetime import datetime

board = Board()
short_term = []

while True:
    if not board.over:
        moves = readMem(board)
        move = chooseMove(moves)
        short_term.append('"' + board.serialize() + '",' + str(move.num) + ',1,')
        board.move(move.with_state(1))
        board = ~board
    else:
        now = str(datetime.now())
        long_term = open('./memory.csv', 'a')
        tie = type(board.over) is bool
        for i in range(len(short_term)):
            entry = short_term[i]
            outcome = 0 if tie else (-1)**(len(short_term) - i - 1)
            long_term.write(entry + str(outcome) + ',' + now + '\n')
        long_term.close()
        board = Board()
        short_term = []
