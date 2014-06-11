import random

class Cell(object):
    def __init__(self, n, state=0, string=''):
        if type(n) == tuple:
            self.x, self.y = n
            self.num=Cell.coords_to_num(self.x, self.y)
        else:
            self.num = n
            self.x, self.y = Cell.num_to_coords(self.num)
        self.coords = (self.x,self.y)
        self.state = state
        self.string = string
    
    def filled(self):
        return self.state != 0
    
    def __hash__(self):
        return hash( (self.num, self.filled()) )
    
    def __eq__(self, other): #matters if it's mine or yours
        if type(self) != type(other): return False
        return (self.num, self.state) == (other.num, other.state)

    def __lt__(self,other):
        return self.num < other.num

    def __gt__(self,other):
        return self.num > other.num

    def __ne__(self, other):
        return not self == other
     
    def __str__(self):
        if len(self.string) > 0:
            return self.string
        else:
            return [' ', 'x', 'o'][self.state]
    
    def __repr__(self):
        return "<Cell " + str(self.num) + ' ' + str(self.state) + ">"

    def __invert__(self):
        if self.string == 'x': string = 'o'
        elif self.string == 'o': string = 'x'
        else: string = self.string
        return Cell(self.num, self.state*-1, string)

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
        return Cell((x,y), self.state,self.string)

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
        return Cell((x,y), self.state, self.string)

    def with_state(self,state):
        return Cell(self.num, state, self.string)

    @classmethod
    def coords_to_num(cls,x,y):
        return x-3*y+5

    @classmethod
    def num_to_coords(cls,n):
        return ((n-1)%3-1, -((n-1)/3)+1)

class Board(object):
    def __init__(self, cells=[]):
        self.cells = sorted([Cell(x) for x in range(1,10)])
        for cell in cells:
            self.move(cell)

    @classmethod
    def from_list(cls,d):
        states = {'x': 1, 'o':-1, ' ':0, '': 0}
        return Board( [Cell(x+1,(states[d[x]] if d[x] in states else 0), str(d[x])) for x in range(9)] )

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
        return Board([~cell for cell in self.cells])

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
        s=map(int, s.split(','))
        return Board([Cell(x,s[x-1]) for x in range(1,10)])
    
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
            if max(states) == -1:
                winner = 'user'
                the_lane = ','.join([str(cell.num) for cell in lane])
                return [True, winner, the_lane]
            elif min(states) == 1:
                winner = 'computer'
                the_lane = ','.join([str(cell.num) for cell in lane])
                return [True, winner, the_lane]
        if len(self.empties()) == 0:
            return [True, 'tie', '']
        else: return [False]

    def __getitem__(self, key):
        if type(key) is slice:
            x,y=key.start,key.stop
            if abs(x) > 1 or abs(y) > 1: raise IndexError, 'list index out of range'
            return [cell for cell in self.cells if cell.x == x and cell.y == y][0]
        else: return [cell for cell in self.cells if cell.num==key][0]
        
    def move(self, ncell):
        for cell in self.cells:
            if ncell.num == cell.num:
                self.cells.remove(cell)
                self.cells.append(ncell)
                self.cells.sort()
                break

    def empties(self):
        return [cell for cell in self.cells if cell.empty()]
