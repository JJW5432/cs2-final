#!/usr/bin/python
print ""

from tic_lib import *

import cgi
import cgitb
cgitb.enable()
fs = cgi.FieldStorage()

board = Board.from_string(fs['board'].value) # given board as string
empties = board.empties()
moves = {cell: [0., 0.] for cell in empties} #[wins, losses]

fileMemory = open("memory.csv")
memory = fileMemory.read()
fileMemory.close()

for line in memory:
    line = parseLine(line)
    if line['board'].is_isomorphic(board):
        move = board.matchMove(line['board'], line['move'])
        if line['outcome'] == 1:
            moves[move][0] += 1
        elif line['outcomes'] == -1:
            moves[move][1] += 1

#each item in memory: [board, cell_num, outcome]

def int_to_coords(n):
    ys = [1, 1, 1, 0, 0, 0, -1, -1, -1]
    xs = [-1, 0, 1, -1, 0, 1, -1, 0, 1]
    y = ys[n-1]
    x = xs[n-1]
    return [x,y]

def parseLine(line):
    pos = line[1:].find('"')
    board= board.from_string(line[1:pos])
    line = map(int, line[pos+1:].split(',')) #[cell,player,outcome]
    coords = int_to_coords(line[0])
    move = Cell(coords[0], coords[1], 1)
    outcome = line[2]
    return {'board': board, 'move':move, 'outcome':outcome}
    
def rankMoves(moves):
    '''orders moves into list based on win percentage'''
    ranked = []
    for cell in moves: # for a possible move in dictionary
        ratio = move[0] / (move[1] + move[0]) # ratio of wins to total games
        i = 0
        while i < len(ranked) and ratio < ranked[i][1]:
            i += 1
        ranked = ranked[:i] + [[cell,ratio]]+ ranked[i:]
    return ranked                                  
           
def chooseMove():
    '''uses weighted probabilities to choose move'''
    for move in rankMoves(moves):
        if random.random() < move[1]:
            return move[1]
    return Board.randomMove(board)

move = chooseMove()
cell_to_num = lambda x,y: x-3*y+5

print cell_to_num(*move.coords)
