import random

class Cell(object):
    def __init__(self, n, state=0, string=''):
        if type(n) is tuple:
            self.x, self.y = n
            self.num=Cell.coords_to_num(self.x, self.y)
        else: #n is an cell num
            self.num = n
            self.x, self.y = Cell.num_to_coords(self.num)
        self.coords = (self.x,self.y)
        self.state = state
        
        self.filled = self.state != 0
        self.empty  = self.state == 0
        self.mine   = self.state == 1
        self.theirs = self.state == -1
    
    @classmethod
    def coords_to_num(cls,x,y):
        return x-3*y+5

    @classmethod
    def num_to_coords(cls,n):
        return ((n-1)%3-1, -((n-1)/3)+1)

    def __hash__(self):
        return hash( (self.num, self.state) )
    
    def __eq__(self, other): #matters if it's mine or yours
        return type(self) is type(other) and (self.num, self.state) == (other.num, other.state)

    def __lt__(self,other):
        return self.num < other.num

    def __gt__(self,other):
        return self.num > other.num

    def __ne__(self, other):
        return not self == other
     
    def __str__(self):
        return [' ', 'x', 'o'][self.state]
    
    def __repr__(self):
        return "<Cell " + str(self.num) + ' ' + str(self.state) + ">"

    def __invert__(self):
        return Cell(self.num, self.state*-1)

    def with_state(self,state):
        return Cell(self.num, state)


    def rotate(self, n=1):
        """returns the coordinates of the cell after a n rotations of 90 degrees clockwise"""
        (x,y) = self.coords
        for i in range(n):
                (x,y) = (y, -1*x)
        return Cell((x,y), self.state)

    def reflect(self,d):
        """returns the coordiantes of the cell after a reflection about a specific axis: v=>vertical axis; h=>horizontal axis; l=>top-left to bottom-right axis; r=>top-right to bottom-left axis"""
        (x,y) = self.coords
        if d == 'v': #vertical
            (x,y) = (-1*x,y)
        elif d == 'h': #horizontal
            (x,y) = (x, -1*y)
        elif d =='l': #top-left to bottom-right
            (x,y) = (-1*y, -1*x)
        elif d == 'r': #top-right to bottom-left
            (x,y) = (y, x)
        return Cell((x,y), self.state)

class Board(object):
    transformations = [lambda x: x, lambda x: x.rotate(),  lambda x: x.rotate(2), lambda x: x.rotate(3), lambda x: x.reflect('v'), lambda x: x.reflect('h'), lambda x: x.reflect('l'), lambda x: x.reflect('r')]

    def __init__(self, *cells):
        self.cells = sorted([Cell(x) for x in range(1,10)])
        for cell in cells:
            self.move(cell)
    
    def __hash__(self):
        return hash( tuple([hash(cell) for cell in self.cells]) )
    
    def __eq__(self,other):
        return type(other) is type(self) and self.cells == other.cells
    
    def __ne__(self,other):
        return not self == other

    def __invert__(self):
        return Board(*[~cell for cell in self])

    def __str__(self):
        out = ''
        for n in [1,0,-1]:
             out += "|".join([str(cell) for cell in self if cell.y == n])
             out +="\n"
        return out.strip('\n')
    
    def __repr__(self):
        return "<Board x:" + str(tuple([self.mine])) + ", o:" + str(tuple([self.theirs])) + ">"

    @classmethod
    def from_list(cls,s):
        return Board(*[Cell(x,s[x-1]) for x in range(1,10)])

    @classmethod
    def from_dict(cls,d):
        return Board(*[Cell(x,d[x]) for x in d])

    @classmethod
    def unserialize(cls,s):
        s=map(int, s.split(','))
        return Board(*[Cell(x,s[x-1]) for x in range(1,10)])

    def serialize(self):
        out = ''
        for cell in self:
            out += str(cell.state) + ','
        return out[:-1]
    
    def __getitem__(self, key):
        if type(key) is tuple:
            x,y=key
            if abs(x) > 1 or abs(y) > 1: raise IndexError, 'coordinates mmust be on board'
            return [cell for cell in self if cell.x == x and cell.y == y][0]
        else: 
            try: return [cell for cell in self if cell.num==key][0]
            except: raise ValueError, 'cell number must be in 1-9 inclusive'

    def __setitem__(self, key, value):
        try: self.move(self[key].with_state(value))
        except: raise ValueError, 'must be integer within 1:-1'

    def __iter__(self):
        return iter(self.cells)
        
    def move(self, cell):
        self.cells.remove(self[cell.num])
        self.cells.append(cell)
        self.cells.sort()

    def isotransformations(self,other):
        return [transformation for transformation in Board.transformations if transformation(other)==self]

    def is_isomorphic(self, other):
        return len(self.isotransformations(other)) > 0
        
    def rotate(self,n=1):
        """rotates a given board clockwise 90 degrees n times"""
        return Board(*[cell.rotate(n) for cell in self] )

    def reflect(self,d):
        """reflects board accross vertical ('v'), horizontal ('h'), top-left to bottom-right diagonal ('l'), or top-right to bottom-left diagonal ('r')"""
        return Board(*[cell.reflect(d) for cell in self] )

    def randomMove(self):
        """outputs a random unoccupied position given a board"""
        return random.choice(self.empties)
        
    def isomoves(self, other, move):
        """finds equivalent move in isoboard"""
        return [transformation(move) for transformation in self.isotransformations(other)]
        
    @property
    def lanes(self):
        lanes = []
        lanes.append([cell for cell in self if cell.x == -1])
        lanes.append([cell for cell in self if cell.x == 0])
        lanes.append([cell for cell in self if cell.x == 1])
        lanes.append([cell for cell in self if cell.y == -1])
        lanes.append([cell for cell in self if cell.y == 0])
        lanes.append([cell for cell in self if cell.y == 1])
        lanes.append([cell for cell in self if cell.x == cell.y])
        lanes.append([cell for cell in self if cell.x == -cell.y])
        return lanes

    @property
    def empties(self):
        return [cell for cell in self if cell.empty]

    @property
    def over(self):
        for lane in self.lanes:
            states = [cell.state for cell in lane]
            if states.count(1)>=3 or states.count(-1)>=3: return lane
        if len([cell for cell in self if cell.empty]) == 0: return True
        else:
            return False

    def row(self, cell):
        return sorted([ncell for ncell in self if ncell.y == cell.y])

    def column(self,cell):
        return sorted([ncell for ncell in self if ncell.x == cell.x])

    def diagonal(self,cell):
        if cell.num in [2,4,5,6,8]: raise ValueError
        if cell.x == cell.y: return [ncell for ncell in self if ncell.x == ncell.y]
        elif cell.x == -cell.y: return [ncell for ncell in self if ncell.x == -ncell.y]
        else: return False
    
    @property
    def mine(self):
        return [cell for cell in self if cell.mine]
        
    @property
    def theirs(self):
        return [cell for cell in self if cell.theirs]
