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
    line = map(int, line[pos+2:].split(',')[:-1]) #[cell,player,outcome]
    move = Cell(line[0], 0)
    outcome = line[2]
    return {'board': board, 'move':move, 'outcome':outcome}

def chooseMove():
    '''uses weighted probabilities to choose move'''
    weighted_moves = []
    for move in moves:
        record = moves[move]
        if record < 10: record = 10 #so every move has hope
        weighted_moves.extend([move]*record)
    return random.choice(weighted_moves)

board = Board.unserialize(fs['board'].value) # given board as string
#board = Board.unserialize('-1,0,0,0,0,0,0,0,0')
empties = board.empties()
over = board.over()

if not over[0]:
    moves = {cell: 100 for cell in empties} 

    memory = open("memory.csv")

    for line in memory:
        line = parseLine(line)
        if line['board'].fuzzy_isomorphic(board):
            move = board.matchMove(line['board'], line['move'])
            if move in moves: moves[move] += line['outcome']

    memory.close()                          
                
    move = chooseMove()

    board.move(move.with_state(1))
    over_now = board.over()
    if over_now[0]:
        print str(over_now[1]) + "\n" + over_now[2]
    else: print move.num
    
else: print str(over[1]) + "\n" + over[2]
