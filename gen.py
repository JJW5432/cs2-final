#!/usr/bin/python

from tic_lib import *

import random
from datetime import datetime

def parseLine(line):
    pos = line[1:].find('"')+1
    #print pos
    board= Board.unserialize(line[1:pos])
    line = map(int, line[pos+2:].split(',')[:-1]) #[cell,player,outcome]
    move = Cell(line[0], 0)
    outcome = line[1]
    return {'board': board, 'move':move, 'outcome':outcome}

def chooseMove():
    '''uses weighted probabilities to choose move'''
    weighted_moves = []
    for move in moves:
        record = moves[move]
        ratio = int(round(record[0]/sum(record),3)*1000)
        weighted_moves.extend([move]*ratio)
    return random.choice(weighted_moves)

board = Board()
short_term = []

while True:
#    print 'starting'
    if not board.over()[0]:
        empties = board.empties()
        moves = {cell: [1., 1.] for cell in empties} #[wins, losses]

        memory = open("memory.csv")

        for line in memory:
            line = parseLine(line)
            print line
            print line['board']
            print board
            if (~line['board']).is_isomorphic(board):
                line['board'], line['outcome'] = ~(line['board']), -line['outcome']
            if line['board'].is_isomorphic(board):
                move = line['board'].matchMove(board, line['move'])
                if line['outcome'] == 1:
                    moves[move][0] += 1 #wins
                elif line['outcome'] == -1:
                    moves[move][1] += 1 #losses

        memory.close()                          
                
        move = chooseMove()
        
        short_term.append('"'+board.serialize()+'",'+str(move.num)+",1,");

        board.move(move.with_state(1))
        print short_term

    if board.over()[0]:
        print 'game'
        winners = {'computer':1, 'user':-1, 'tie':0}
        outcome = str(winners[board.over()[1]])
        long_term = open('memory.csv', 'a')
        now = str(datetime.today())

        for entry in short_term:
            long_term.write(entry+outcome+','+now+'\n')
        long_term.close()

        board = Board()
    else: board = ~board
