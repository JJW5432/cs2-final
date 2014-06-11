from tic_lib import *

import cgi
fs = cgi.FieldStorage()

board = Board.from_string(fs['board'].value)
empties = board.empties()
moves = {cell: [0., 0., 0.] for cell in empties} #[wins, losses]

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
    outcome =line[2]
    return {'board': board, 'move':move, 'outcome':outcome}
    
                                   
            
                                   


def findMemory(b):
    '''gets list of moves and outcomes in isomorphic situations
    returns a list of possible moves [Cell, wins, losses, win/total, player] for all moves in memory
    '''
    L = [] #list of possible moves [Cell, wins, losses, win/total, player]
    for move in memory: # list in memory
        if Board.is_isomorphic(move[0],b): # tests if given board is same as board in memory
            play = Board.matchMove(move[0],b,move[1]) # equivalent move in isomorphic board
            newPlay = True # tests if new move needs to be added
            for m in L:
                if m[0] == play: #if cells are equal
                    if move[3] == 1: #if I won
                        m[1] += 1.0 #increase wins by 1
                    elif move[3] == -1: #else if I lost
                        m[2] += 1.0 #increase losses by 1
                    newPlay = False 
            if newPlay == True: #no mathching moves in L
                L += [[move[1],0.0,0.0,0.0,move[2]]] #add new blank move
                if move[3] == 1: #if I won...
                    m[1] += 1.0
                elif move[3] == -1: #if I lost...
                    m[2] += 1.0
    return L

def rankMoves(moves):
    '''orders moves based on win percentage'''
    ranked = []
    for move in moves:
        move[3] = move[1] / (move[1] + move[2])
    for move in moves:
        i = 0
        while i < len(ranked) and move[3] < ranked[i][3]:
            i += 1
        ranked = ranked[:i] + [move] + ranked[i:]
    return ranked

def chooseMove(b):
    '''uses weighted probabilities to choose move'''
    for move in rankMoves(findMemory(b)):
        if random.random() < move[3]:
            return move[3]
    return Board.randomMove(b)
