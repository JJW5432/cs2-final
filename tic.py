import random

class Board:
    def __init__(self, cells):
        self.cells = cells
        self.isoboards = {self: lambda x: x, self.rotate(): lambda x: x.rotate(), self.rotate(2): lambda x: x.rotate(2), self.rotate(3): lambda x: x.rotate(3), self.reflect('v'): lambda x: x.reflect('v'), self.reflect('h'): lambda x: x.reflect('h'), self.reflect('l'): lambda x: x.reflect('l'), self.reflect('r'): lambda x: x.reflect('r')}
    
    def __hash__(self):
        return hash( tuple([hash(cell) for cell in self.cells]) )
    
    def __eq__(self,other):
        return type(other) == type(self) and self.cells == other.cells
    
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
        
        def matchMove(self, other, move):
            """finds equivalent move in isoboard
            isoboards() function returns list of isoboards as following:
            >>> matchMoveIsoboard((1,1),board2,board3)
            (-1, 1)
            >>> matchMoveIsoboard((1,1),board2,board1)
            'not isomorphic'
            >>> matchMoveIsoboard((1,1),board2,board2)
            (1, 1)
            """
            if self != other:
                return False
            return self.isoboards[other](cell)

        
class Cell:
    def __init__(self, x, y, state=0, string=''):
        self.coords = (x,y)
        self.x, self.y = x, y
        self.state = state
    
    def __hash__(self):
        return hash( (self.coords, self.filled()) )
    
    def __eq__(self, other): #doesn't matter if it's mine or yours
        return (self.x, self.y, self.filled()) == (other.x, other.y, other.filled())

    def __ne__(self, other):
        return not self == other
     
    def __str__(self):
        if len(self.string) > 0:
            return self.string
        else:
            return ['x', ' ', 'o'][self.state]
    
    def __repr__(self):
        return "<Cell at (" + str(x) + "," + str(y) + "), state: " + str(self.state) + ">"

    def __invert__(self):
        return Cell(self.coords[0], self.y, self.state*-1)

    def filled(self):
        return self.state != 0

    def empty(self):
        return self.state == 0
    
    def mine(self):
        return state == 1

    def theirs(self):
        return state == -1

    def rotate(self, n=1):
        """given the coordiantes of a cell, it returns the coordinates of the cell after a n rotations of 90 degrees clockwise"""
        (x,y) = self.coords
        for x in range(n):
                cell = (y, -1*x)
        return Cell(x,y, self.state)

    def reflect(self,d):
        (x,y) = self.coords
        if d == 'v': #vertical
            (x,y) = (-1*x,y)
        elif d == 'h': #horizontal
            (x,y) = (x, -1*y)
        elif d =='l': #top-left to bottom-right
            (x,y) = (-1*y, -1*x)
        elif d == 'r': #top-right to bottom-left
            (x,y) = (y, x)
        return Cell(x, y, self.state)



a_board = {(-1,1): '1', (0,1): '2', (1,1): '3', (-1,0):'4', (0,0): '5', (1,0): '6', (-1,-1): '7', (0,-1): '8', (1,-1): '9'}
a_board = Board([Cell(x[0], x[1], 0, a_board[x]) for x in a_board.keys()])

board1 = {(-1,1):"x",(0,1):"o",(1,1):"x",(-1,0):"x",(0,0):"x",(1,0):"o",(-1,-1):"o",(0,-1):" ",(1,-1):"o"}
board2 = {(-1,1):"x",(0,1):"o",(1,1):" ",(-1,0):" ",(0,0):" ",(1,0):" ",(-1,-1):" ",(0,-1):" ",(1,-1):" "}   
board3 = {(-1,1):" ",(0,1):"o",(1,1):"x",(-1,0):" ",(0,0):" ",(1,0):" ",(-1,-1):" ",(0,-1):" ",(1,-1):" "}

if __name__ == "__main__":
    import doctest
    doctest.testmod()
