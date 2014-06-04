from tic import *

a_board = Board.from_dict({(-1,1): '1', (0,1): '2', (1,1): '3', (-1,0):'4', (0,0): '5', (1,0): '6', (-1,-1): '7', (0,-1): '8', (1,-1): '9'})
board1 = Board.from_dict({(-1,1):"x",(0,1):"o",(1,1):"x",(-1,0):"x",(0,0):"x",(1,0):"o",(-1,-1):"o",(0,-1):" ",(1,-1):"o"})
board2 = Board.from_dict({(-1,1):"x",(0,1):"o",(1,1):" ",(-1,0):" ",(0,0):" ",(1,0):" ",(-1,-1):" ",(0,-1):" ",(1,-1):" "})  
board3 = Board.from_dict({(-1,1):" ",(0,1):"o",(1,1):"x",(-1,0):" ",(0,0):" ",(1,0):" ",(-1,-1):" ",(0,-1):" ",(1,-1):" "})

def deep_strip(s):
        return '\n'.join([l.strip() for l in s.split('\n')]).strip()

class TestCell:
    def test_basic(self):
        x, y = random.randrange(-1,2), random.randrange(-1,2)
        cell = Cell(x,y,1,'o')
        assert cell.coords == (x,y)
        assert str(cell) == 'o'
        assert cell != Cell(x,y,-1)
        assert cell != Cell(x,y+1,1)
        assert (~cell).state == -1
        a_board.isoboards()

    def test_rotate(self):
        cell = Cell(-1,1)
        assert cell.rotate( ) == Cell(1,1)
        assert cell.rotate(2) == Cell(1,-1)
        assert cell.rotate(3) == Cell(-1,-1)
        assert cell.rotate(4) == cell
    
    def test_reflect(self):
        cell = Cell(-1,1)
        assert cell.reflect('v') == Cell(1,1)
        assert cell.reflect('h') == Cell(-1,-1)
        assert cell.reflect('l') == cell
        assert cell.reflect('r') == Cell(1, -1)
        

class TestBoard:
    def test_basic(self):
        assert a_board == Board([Cell(-1, 1, 0, '1'), Cell(0, 1, 0, '2'), Cell(1, 1, 0, '3'), Cell(-1, 0, 0, '4'), Cell(0, 0, 0, '5'), Cell(1, 0, 0, '6'), Cell(-1, -1, 0, '7'), Cell(0, -1, 0, '8'), Cell(1, -1, 0, '9')])
        assert str(a_board) == deep_strip("""
        1|2|3
        4|5|6
        7|8|9
        """)

    def test_invert(self):
        display = str(board3)
        invert = ''
        for char in display:
            if char == 'x': 
                invert += 'o'
            elif char == 'o': 
                invert += 'x'
            else:
                invert += char
        assert invert == str(~board3)
        assert board3.is_isomorphic(~board3)
    
    def test_rotate(self):
        assert str(a_board.rotate()) == deep_strip("""
        7|4|1
        8|5|2
        9|6|3
        """)
        
        assert str(a_board.rotate(2)) == deep_strip("""
        9|8|7
        6|5|4
        3|2|1
        """)
        
        assert a_board.rotate(4) == a_board
        assert a_board.rotate(2).is_isomorphic(a_board)

    def test_reflect(self):
        assert str(a_board.reflect('v')) == deep_strip("""
        3|2|1
        6|5|4
        9|8|7
        """)

        assert str(a_board.reflect('h')) == deep_strip("""
        7|8|9
        4|5|6
        1|2|3
        """)

        assert str(a_board.reflect('l')) == deep_strip("""
        1|4|7
        2|5|8
        3|6|9
        """)

        assert str(a_board.reflect('r')) == deep_strip("""
        9|6|3
        8|5|2
        7|4|1
        """)
        
        assert a_board.reflect('l').is_isomorphic(a_board)

    def test_randomMove(self):
        assert not board1.randomMove().filled()

    def test_matchMove(self):
        assert board2.matchMove(board3,Cell(1,1)) == Cell(-1,1)
        assert board2.matchMove(board1,Cell(1,1)) == False
        assert board2.matchMove(board2,Cell(1,1)) == Cell(1, 1)
