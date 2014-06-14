from tic import *

def parseLine(line):
    pos = line[1:].find('"')+1
    board= Board.unserialize(line[1:pos])
    line = map(int, line[pos+2:].split(',')[:-1]) #[cell,player,outcome]
    move = Cell(line[0], 0)
    outcome = line[2]
    player = line[1]
    return {'board': board, 'move':move, 'outcome':outcome, 'player':player}

def chooseMove(moves):
    '''uses weighted probabilities to choose move'''
    for move in moves:
        moves[move] = moves[move][0]/sum(moves[move])
    return max(moves, key=lambda x: moves[x])

def readMem(board):
    empties = board.empties
    over = board.over
    
    moves = {cell: [1., 1.] for cell in empties} #[wins, losses]
    
    memory = open("memory.csv")
    
    for line in memory:
        line = parseLine(line)
        if board.is_isomorphic(~line['board']):
            line['board'] = ~line['board']
            line['outcome'] = -line['outcome']
        #print board
        #print line['board']
        #print repr(line['move'])
        if line['board'].is_isomorphic(board):
            for isomove in board.isomoves(line['board'],line['move']):
                if isomove in moves:
                    if line['outcome'] == 1:
                        moves[isomove][0] += 1 #wins
                    elif line['outcome'] == -1:
                        moves[isomove][1] += 1 #losses
                    elif len(board.empties)%2==1:
                        moves[isomove][0] = 0.75

    memory.close()
    return moves
