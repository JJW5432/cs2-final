#!/usr/bin/python
print "Content-Type: text/html\n"
print ""
from tic_lib import *

#import random

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
    player = line[3]
    return {'board': board, 'move':move, 'outcome':outcome, 'player':player}

def chooseMove(moves):
    '''uses weighted probabilities to choose move'''
    for move in moves:
        moves[move] = moves[move][0]/sum(moves[move]])
    return max(moves, key=lambda x: moves[x])

board = Board.unserialize(fs['board'].value) # given board as string
#board = Board.unserialize('-1,0,0,0,0,0,0,0,0')

def readMem(board):
    empties = board.empties
    over = board.over
    
    moves = {cell: [1., 1.] for cell in empties} #[wins, losses]
    
    memory = open("memory.csv")
    
    for line in memory:
        line = parseLine(line)
        line['outcome'] *= line['player'] #handle other guy
        if line['board'].is_isomorphic(board):
            move = board.matchMove(line['board'], line['move'])
            if line['outcome'] == 1:
                moves[move][0] += 1 #wins
            elif line['outcome'] == -1:
                moves[move][1] += 1 #losses

    memory.close()
    return moves

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
