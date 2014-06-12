from tic_lib import *

def lanes(board):
    cells = board.cells
    lanes = {}
    lanes["leftC"] = [cell for cell in cells if cell.x == -1]
    lanes["midC"] = [cell for cell in cells if cell.x == 0]
    lanes["rightC"] = [cell for cell in cells if cell.x == 1]
    lanes["bottomR"] = [cell for cell in cells if cell.y == -1]
    lanes["midR"] = [cell for cell in cells if cell.y == 0]
    lanes["topR"] = [cell for cell in cells if cell.y == 1]
    lanes["posD"] = [cell for cell in cells if cell.x == cell.y]
    lanes["negD"] = [cell for cell in cells if cell.x == -cell.y]
    return lanes

def states(lane):
    states = [cell.state for cell in lane]
    return states

##def make_fork(board):
##    for i in [lanes(board)['posD'],lanes(board)['negD']]:
##        if mine(states(i)[0]) and mine(states(i)[1]):
##            f

def optimal_move(board):
    L = lanes(board)
    for lane in lanes(board):
        # 2 cells in lane filled by comp
        if states(L[lane]).count(1) == 2 and states(L[lane]).count(0) == 1:
            # complete lane
            return [str(cell.num) for cell in L[lane] if cell.state == 0]
        # 2 cells in lane filled by user
        elif states(L[lane]).count(-1) == 2 and states(L[lane]).count(0) == 1:
            # block lane
            return [str(cell.num) for cell in L[lane] if cell.state == 0]
    #! make fork
    #! block opponent fork
    if mine(board[5]) and ( (theirs(board[1] and board[9])) or (theirs(board[3] and board[7])) ):
        return [str(i) for i in range(1,10,2)]
    # mark center if unoccupied
    if empty(board[5]): 
        return ["5"]
    # mark opposite corner from opponent
    for i in [lanes(board)['posD'],lanes(board)['negD']]:
        if theirs(states(i)[0]) and empty(states(i)[2]):
            return [str(states(i)[2].num)]
        elif theirs(states(i)[2]) and empty(states(i)[0]):
            return [str(states(i)[0].num)]
    # mark empty side square
    return [str(i) for i in range(1,10,2) if empty(board[i])]
    

        
    
