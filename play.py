#!/usr/bin/python
print "Content-Type: text/html\n"
print ""
from tic_lib import *

import random

import cgi
import cgitb
cgitb.enable()
fs = cgi.FieldStorage()

def parseLine(line):
    pos = line[1:].find('"')+1
    board= Board.unserialize(line[1:pos])
    line = map(int, line[pos+2:].split(',')) #[cell,player,outcome]
    move = Cell(line[0], 0)
    outcome = line[2]
    return {'board': board, 'move':move, 'outcome':outcome}

def chooseMove():
    '''uses weighted probabilities to choose move'''
    weighted_moves = []
    for move in moves:
        record = moves[move]
        ratio = int(round(record[0]/sum(record),3)*1000)
        weighted_moves.extend([move]*ratio)
    return random.choice(weighted_moves)

board = Board.unserialize(fs['board'].value) # given board as string
empties = board.empties()
over = board.over()

if not over[0]:
    moves = {cell: [1., 1.] for cell in empties} #[wins, losses]

    memory = open("memory.csv")

    for line in memory:
        line = parseLine(line)
        if line['board'].is_isomorphic(board):
            move = board.matchMove(line['board'], line['move'])
            if line['outcome'] == 1:
                moves[move][0] += 1 #wins
            elif line['outcome'] == -1:
                moves[move][1] += 1 #losses

    memory.close()                          
                
    move = chooseMove()

    print move.num

else: print str(over[1]) + "\n" + over[2]
