import random

class Board:
    def __init__(self, cells):
        self.cells = cells
        #self.isoboards = [board, rotate_board(board), rotate_board(board,2), rotate_board(board,3), reflect_board(board,'v'), reflect_board(board,'h'), reflect_board(board,'l'), reflect_board(board,'r')]
    def __eq__(self,other):
        return type(other) == type(self) and (self.cells == other.cells or self.cells == [~cell for cell in other.cells])
    
    def __ne__(self,other):
        return not self == other

    def is_isomorphic(self, other):
        return type(other) == type(self) and other in self.isoboards

    def __str__(self):
        """returns the string that should be printed when you print a board 
        """
        out = ''
        for n in [1,0,-1]:
             out += "|".join([board[point] for point in sorted(board.keys()) if point[1] == n])
        return out

    def __hash__(self):
        return tuple(
        
    def rotate(self,n=1):
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
        return Board( [cell.rotate(n) for cell in self.cells] )

    def reflect(self,d):
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
        return Board( [cell.reflect(d) for cell in self.cells] )

        def randomMove(board):
            """outputs a random unoccupied position given a board
            >>> randomMove(board1)
            [0, -1]
            """
            return random.choice([cell for cell in cells if not cell.filled])

        
class Cell:
    def __init__(self, x, y, filled=False, mine=False):
        self.coords = (x,y)
        self.filled = filled
        self.mine = filled and mine
    
    def __hash__(self):
        return (self.x, self.y, 

    def rotate(self, n=1):
        """given the coordiantes of a cell, it returns the coordinates of the cell after a n rotations of 90 degrees clockwise"""
        (x,y) = self.pos
        for x in range(n):
                cell = (y, -1*x)
        return Cell(x,y, self.filled, self.mine)

    def reflect(self,d):
        (x,y) = self.cell
        if d == 'v': #vertical
            (x,y) = (-1*x,y)
        elif d == 'h': #horizontal
            (x,y) = (x, -1*y)
        elif d =='l': #top-left to bottom-right
            (x,y) = (-1*y, -1*x)
        elif d == 'r': #top-right to bottom-left
            (x,y) = (y, x)
        return Cell(x, y, self.filled, self.mine)



a_board = {(-1,1): '1', (0,1): '2', (1,1): '3', (-1,0):'4', (0,0): '5', (1,0): '6', (-1,-1): '7', (0,-1): '8', (1,-1): '9'}

import random

board1 = {(-1,1):"x",(0,1):"o",(1,1):"x",(-1,0):"x",(0,0):"x",(1,0):"o",(-1,-1):"o",(0,-1):" ",(1,-1):"o"}
board2 = {(-1,1):"x",(0,1):"o",(1,1):" ",(-1,0):" ",(0,0):" ",(1,0):" ",(-1,-1):" ",(0,-1):" ",(1,-1):" "}   
board3 = {(-1,1):" ",(0,1):"o",(1,1):"x",(-1,0):" ",(0,0):" ",(1,0):" ",(-1,-1):" ",(0,-1):" ",(1,-1):" "}

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
