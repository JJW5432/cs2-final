import random

class Cell:
    def __init__(self, x, y, state=0, string=''):
        self.coords = (x,y)
        self.x, self.y = x, y
        self.state = state
        self.string = string
    
    def filled(self):
        return self.state != 0
    
    def __hash__(self):
        return hash( (self.coords, self.filled()) )
    
    def __eq__(self, other): #matters if it's mine or yours
        '''
        >>> Cell(1,1,1) == Cell(1,1,-1)
        False
        '''
        if type(self) != type(other): return False
        return (self.x, self.y, self.state) == (other.x, other.y, other.state)

    def __lt__(self,other):
        if self.y > other.y: return True
        elif self.y == other.y:
            return self.x < other.x
        else: return False

    def __gt__(self,other):
        return not (self<other or self==other)

    def __ne__(self, other):
        return not self == other
     
    def __str__(self):
        if len(self.string) > 0:
            return self.string
        else:
            return [' ', 'x', 'o'][self.state]
    
    def __repr__(self):
        return "<Cell (" + str(self.x) + "," + str(self.y) + ") " + str(self.state) + ">"

    def __invert__(self):
        if self.string == 'x': string = 'o'
        elif self.string == 'o': string = 'x'
        else: string = self.string
        return Cell(self.coords[0], self.y, self.state*-1, string)

    def empty(self):
        return self.state == 0
    
    def mine(self):
        return self.state == 1

    def theirs(self):
        return self.state == -1

    def rotate(self, n=1):
        """given the coordiantes of a cell, it returns the coordinates of the cell after a n rotations of 90 degrees clockwise"""
        (x,y) = self.coords
        for i in range(n):
                (x,y) = (y, -1*x)
        return Cell(x,y, self.state,self.string)

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
        return Cell(x, y, self.state, self.string)

class Board(object):
    def __init__(self, cells=[]):
        self.cells = sorted([Cell(-1,1),Cell(0,1),Cell(1,1),Cell(-1,0),Cell(0,0),Cell(1,0),Cell(-1,-1),Cell(0,-1),Cell(1,-1)])
        for x in cells:
            self.cell = x

    @classmethod
    def from_dict(cls,d):
        states = {'x': 1, 'o':-1, ' ':0, '': 0}
        return Board( [Cell(coord[0], coord[1], (states[d[coord]] if d[coord] in states else 0), d[coord]) for coord in d.keys()] )

    @classmethod
    def from_string(cls,string):
        b = string.split(",")
        B = []
        for i in range(0,27,3):
            B += [Cell(int(b[i]),int(b[i+1]),int(b[i+2]))]
        return Board(B)

    def isoboards(self):
        return {self: lambda x: x, self.rotate(): lambda x: x.rotate(), self.rotate(2): lambda x: x.rotate(2), self.rotate(3): lambda x: x.rotate(3), self.reflect('v'): lambda x: x.reflect('v'), self.reflect('h'): lambda x: x.reflect('h'), self.reflect('l'): lambda x: x.reflect('l'), self.reflect('r'): lambda x: x.reflect('r')}
    
    def __hash__(self):
        return hash( tuple([hash(cell) for cell in self.cells]) )
    
    def __eq__(self,other):
        if type(self) != type(other): return False
        return type(other) == type(self) and self.cells == other.cells
    
    def __ne__(self,other):
        return not self == other

    def __invert__(self):
        return Board(map(lambda x: ~x, self.cells))

    def is_isomorphic(self, other):
        '''
        >>> Board.is_isomorphic(Board.from_dict({(-1,1):"x",(0,1):"o",(1,1):" ",(-1,0):" ",(0,0):" ",(1,0):" ",(-1,-1):" ",(0,-1):" ",(1,-1):" "}), ~Board.from_dict({(-1,1):" ",(0,1):"o",(1,1):"x",(-1,0):" ",(0,0):" ",(1,0):" ",(-1,-1):" ",(0,-1):" ",(1,-1):" "}))
        True
        '''
        return type(other) == type(self) and (other in self.isoboards() or ~other in self.isoboards())

    def __str__(self):
        """returns the string that should be printed when you print a board """
        out = ''
        for n in [1,0,-1]:
             out += "|".join([str(cell) for cell in self.cells if cell.y == n])
             out +="\n"
        return out.strip('\n')
        
    def rotate(self,n=1):
        """rotates a given board clockwise 90 degrees n times"""
        return Board( [cell.rotate(n) for cell in self.cells] )

    def reflect(self,d):
        """reflects board accross vertical ('v'), horizontal ('h'), top-left to bottom-right diagonal ('l'), or top-right to bottom-left diagonal ('r')"""
        return Board( [cell.reflect(d) for cell in self.cells] )

    def randomMove(self):
        """outputs a random unoccupied position given a board"""
        return random.choice([cell for cell in self.cells if not cell.filled()])
        
    def matchMove(self, other, move):
        """finds equivalent move in isoboard"""
        if not self.is_isomorphic(other):
            return False
        else: return self.isoboards()[other](move)
    
    def serialize(self):
        out = ''
        for cell in self.cells:
            out += str(cell.state) + ','
        return out[:-1]

    @classmethod
    def unserialize(cls,s):
        coords = [(-1,1),(0,1),(1,1),(-1,0),(0,0),(1,0),(-1,-1),(0,-1),(1,-1)]
        s=map(int, s.split(','))
        cells = []
        for x in range(len(s)):
            cells.append(Cell(coords[x][0],coords[x][1],s[x]))
        return Board(cells)
    
    def over(self):
        cells = self.cells
        lanes = []
        lanes.append([cell for cell in cells if cell.x == -1])
        lanes.append([cell for cell in cells if cell.x == 0])
        lanes.append([cell for cell in cells if cell.x == 1])
        lanes.append([cell for cell in cells if cell.y == -1])
        lanes.append([cell for cell in cells if cell.y == 0])
        lanes.append([cell for cell in cells if cell.y == 1])
        lanes.append([cell for cell in cells if cell.x == cell.y])
        lanes.append([cell for cell in cells if cell.x == -cell.y])
        for lane in lanes:
            states = [cell.state for cell in lane]
            if max(states) == -1: return -1
            elif min(states) == 1: return 1
        if len([cell for cell in cells if cell.empty()]) == 0: return 'tie'
        else: return False #not over

    def cell(self,x,y):
        return [cell for cell in self.cells if cell.x == x and cell.y == y][0]
        
    def __setattr__(self, name, value):
        if name == 'move' and isinstance(value,Cell):
            for cell in self.cells:
                if cell.x == value.x and cell.y == value.y:
                    self.cells.remove(cell)
                    self.cells.append(value)
                    self.cells.sort()
                    break
                    
        else: super(Board, self).__setattr__(name, value)
