from tic_lib import *

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

def updateMemory():
    '''updates ranking of moves in memory'''
    for board in memory:
        memory[board] = rankMoves(memory[board])

def chooseMove(b):
    '''uses weighted probabilities to choose move'''
    for board in memory:
        if Board.is_isomorphic(board,b):
            for move in memory[board]:
                if random.random() < move[3]:
                    return Board.matchMove(board,b,move[0])
            return Board.randomMove(b)
        else:
            return Board.randomMove(b)

def updateGame(game,outome):
    '''updates memory with game moves and outcomes'''
    if outcome == "w":
        o = 1
    else:
        o = 2
    for position in game:
        newPosition = True
        for board in memory:
            if Board.is_isomorphic(position,board):
                play = Board.matchMove(position,board,game[position])
                newPlay = True
                for move in memory[board]:
                    if move[0] == play:
                        move[o] += 1.0
                        newPlay = False
                if newPlay == True:
                    memory[board] += [play,0.0,0.0,0.0]
                    memory[board][-1][o] += 1.0
                newPosition = False
        if newPosition == True:
            memory[position] = [[game[position],0.0,0.0,0.0]]
            memory[board][0][o] += 1.0
    
a_board = Board.from_dict({(-1,1): '1', (0,1): '2', (1,1): '3', (-1,0):'4', (0,0): '5', (1,0): '6', (-1,-1): '7', (0,-1): '8', (1,-1): '9'})
board1 = Board.from_dict({(-1,1):"x",(0,1):"o",(1,1):"x",(-1,0):"x",(0,0):"x",(1,0):"o",(-1,-1):"o",(0,-1):" ",(1,-1):"o"})
board2 = Board.from_dict({(-1,1):"x",(0,1):"o",(1,1):" ",(-1,0):" ",(0,0):" ",(1,0):" ",(-1,-1):" ",(0,-1):" ",(1,-1):" "})  
board3 = Board.from_dict({(-1,1):" ",(0,1):"o",(1,1):"x",(-1,0):" ",(0,0):" ",(1,0):" ",(-1,-1):" ",(0,-1):" ",(1,-1):" "})

memory = {board1:[[Cell(0,-1),2.0,0.0,1.0]],board2:[[Cell(-1,0),1.0,1.0,1.0],[Cell(0,0),1.0,4.0,.2],[Cell(1,1),5.0,3.0,0.1]]}

