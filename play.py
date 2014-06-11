from tic_lib import *

fileMemory = open("memory.csv")
memory = fileMemory.read()
fileMemory.close()

memory = memory.split("\n")
i = 0
for move in memory:
    board = Board.from_string(move.split("'")[1])
    memory[i] = [board] + move.split("'")[2].split(",")[1:]
    i += 1

def findMemory(b):
    '''gets list of moves and outcomes in isomorphic situations'''
    L = [] 
    for move in memory: # list in memory
        if Board.is_isomorphic(move[0],b): # tests if given board is same as board in memory
            play = Board.matchMove(move[0],b,move[1]) # equivalent move in isomorphic board
            newPlay = True # tests if new move needs to be added
            for m in L:
                if m[0] == play:
                    if move[3] == 1:
                        m[1] += 1.0
                    elif move[3] == -1:
                        m[2] += 1.0
                    newPlay = False
            if newPlay == True:
                L += [[move[1],0.0,0.0,0.0,move[2]]]
                if move[3] == 1:
                    m[1] += 1.0
                elif move[3] == -1:
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
