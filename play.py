#!/usr/bin/python
print "Content-Type: text/html\n"
print ""
from tic_lib import *

import random
#import sys
import cgi
import cgitb
cgitb.enable()
fs = cgi.FieldStorage()

def parseLine(line):
    pos = line[1:].find('"')+1
    board= Board.unserialize(line[1:pos])
    line = map(int, line[pos+2:].split(',')[:-1]) #[cell,player,outcome]
    move = Cell(line[0], 0)
    outcome = line[2]
    return {'board': board, 'move':move, 'outcome':outcome}

def chooseMove():
    '''uses weighted probabilities to choose move'''
    weighted_moves = []
    for move in moves:
        if type(moves[move]) is list: moves[move] = (moves[move][0]-moves[move][1])/(moves[move][0]+moves[move][1])
        record = moves[move]
    return max(moves, key=moves.get)

board = Board.unserialize(fs['board'].value) # given board as string
#board = Board.unserialize(sys.argv[1])
empties = board.empties()
over = board.over()

if not over[0]:
    moves = {cell: [1.,1.] for cell in empties} 
    for move in moves:
        for lane in board.lane(move):
            if len([cell for cell in lane if cell.filled() and cell.mine()]) >= 2: moves[move] = 1.1
            elif len([cell for cell in lane if cell.filled() and cell.theirs()]) >= 2: moves[move] = 1
    memory = open("memory.csv")

    for line in memory:
        line = parseLine(line)
        if (~line['board']).fuzzy_isomorphic(board):
            line['board'] = ~line['board']
            line['outcome'] = -1 * line['outcome']
        if line['board'].fuzzy_isomorphic(board):
            move = board.matchMove(line['board'],line['move'])
            if move in moves and type(moves[move]) is list:
                if line['outcome'] > 1: moves[move][0] += line['outcome']
                elif line['outcome'] < 1: moves[move][1] -= line['outcome']
                else: moves[move][0] += 0.5

    memory.close()                          
                
    move = chooseMove()

    board.move(move.with_state(1))
    over_now = board.over()
    if over_now[0]:
        print str(over_now[1]) + "\n" + over_now[2]
    else: print move.num
    
else: print str(over[1]) + "\n" + over[2]
