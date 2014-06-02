a_board = {(-1,1): '1', (0,1): '2', (1,1): '3', (-1,0):'4', (0,0): '5', (1,0): '6', (-1,-1): '7', (0,-1): '8', (1,-1): '9'}
def display(board,sep=''):
    """displays a textual representation of a board (for dev purposes)
    >>> display(a_board)
    1|2|3
    4|5|6
    7|8|9
    """
    for n in [1,0,-1]:
        print "|".join([board[point] for point in sorted(board.keys()) if point[1] == n])
    if len(sep) > 0: print sep

def rotate(cell, n=1):
        """given the coordiantes of a cell, it returns the coordinates of the cell after a n rotations of 90 degrees clockwise"""
        for x in range(n):
                cell = (cell[1], -1*cell[0])
        return cell

def rotate_board(board,n=1):
    """rotates a given board clockwise 90 degrees n times
    >>> display(rotate_board(a_board))
    7|4|1
    8|5|2
    9|6|3
    >>> display(rotate_board(a_board,2))
    9|8|7
    6|5|4
    3|2|1
    >>> rotate_board(a_board,4)==a_board
    True
    """
    backup = board.copy()
    board = {rotate(point,n): backup[point] for point in backup.keys()}
    return board

def reflect(cell,d):
    if d == 'v': #vertical
        return (-1*cell[0],cell[1])
    elif d == 'h': #horizontal
        return (cell[0], -1*cell[1])
    elif d =='l': #top-left to bottom-right
        return (-1*cell[1], -1*cell[0])
    elif d == 'r': #top-right to bottom-left
        return (cell[1], cell[0])


def reflect_board(board,d):
    """reflects board accross vertical ('v'), horizontal ('h'), top-left to bottom-right diagonal ('l'), or top-right to bottom-left diagonal ('r')
    >>> display(reflect_board(a_board,'v'))
    3|2|1
    6|5|4
    9|8|7
    >>> display(reflect_board(a_board,'h'))
    7|8|9
    4|5|6
    1|2|3
    >>> display(reflect_board(a_board,'l'))
    1|4|7
    2|5|8
    3|6|9
    >>> display(reflect_board(a_board,'r'))
    9|6|3
    8|5|2
    7|4|1
    """
    backup = board.copy()
    board = {reflect(point,d): backup[point] for point in backup.keys()}
    return board

def isoboards(board):
    """returns a list of all equivelant boards"""
    return [board, rotate_board(board), rotate_board(board,2), rotate_board(board,3), reflect_board(board,'v'), reflect_board(board,'h'), reflect_board(board,'l'), reflect_board(board,'r')]

def is_isomorphic(board1, board2):
    return board1 in isoboards(board2)

import random

board1 = {(-1,1):"x",(0,1):"o",(1,1):"x",(-1,0):"x",(0,0):"x",(1,0):"o",(-1,-1):"o",(0,-1):" ",(1,-1):"o"}
board2 = {(-1,1):"x",(0,1):"o",(1,1):" ",(-1,0):" ",(0,0):" ",(1,0):" ",(-1,-1):" ",(0,-1):" ",(1,-1):" "}   
board3 = {(-1,1):" ",(0,1):"o",(1,1):"x",(-1,0):" ",(0,0):" ",(1,0):" ",(-1,-1):" ",(0,-1):" ",(1,-1):" "}

def randomMove(board):
    """outputs a random unoccupied position given a board
    >>> randomMove(board1)
    [0, -1]
    """
    listBlank = [] # stores list of positions that are unoccupied
    for cell in board.keys():
        if board[cell] == " ":
            listBlank += cell
    choose = random.randrange(0,len(listBlank),2)
    move = listBlank[choose:choose+2]
    return move

def matchMoveIsoboard(move,board,isoboard):
    """finds equivalent move in isoboard
    isoboards() function returns list of isoboards as following:
    0 - original
    1 - rotated 90
    2 - rotated 180
    3 - rotated 270
    4 - flipped on vertical
    5 - flipped on horizontal
    6 - flipped on top-left to bottom-right
    7 - flipped on top-right to bottom-left
    >>> matchMoveIsoboard((1,1),board2,board3)
    (-1, 1)
    >>> matchMoveIsoboard((1,1),board2,board1)
    'not isomorphic'
    >>> matchMoveIsoboard((1,1),board2,board2)
    (1, 1)
    """
    try:
        transformation = isoboards(board).index(isoboard)
    except:
        return "not isomorphic"
    if transformation == 1:
        return rotate(move,1)
    elif transformation == 2:
        return rotate(move,2)
    elif transformation == 3:
        return rotate(move,3)
    elif transformation == 4:
        return reflect(move,'v')
    elif transformation == 5:
        return reflect(move,'h')
    elif transformation == 6:
        return reflect(move,'l')
    elif transformation == 7:
        return reflect(move,'r')
    else:
        return move

if __name__ == "__main__":
    import doctest
    doctest.testmod()