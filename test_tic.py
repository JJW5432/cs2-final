from tic_lib import *

def deep_strip(s):
        return '\n'.join([l.strip() for l in s.split('\n')]).strip()

class TestCell:
        def test_basic(self):
                x, y = random.randrange(-1,2), random.randrange(-1,2)
                cell = Cell((x,y),1)
                assert cell.coords == (x,y)
                assert str(cell) == 'x'
                assert cell != Cell((x,y),-1)
                assert cell != Cell((x,y+1),1)
                assert (~cell).state == -1
                assert cell.filled
                assert cell.num_to_coords(4) == (-1,0)
                assert Cell(1) < Cell(5)
                assert sorted([Cell(4),Cell(2),Cell(7)]) == [Cell(2),Cell(4),Cell(7)]
                assert Cell(1,0).with_state(-1).state == -1

        def test_rotate(self):
                cell = Cell((-1,1))
                assert cell.rotate( ) == Cell((1,1))
                assert cell.rotate(2) == Cell((1,-1))
                assert cell.rotate(3) == Cell((-1,-1))
                assert cell.rotate(4) == cell
    
        def test_reflect(self):
                cell = Cell((-1,1))
                assert cell.reflect('v') == Cell((1,1))
                assert cell.reflect('h') == Cell((-1,-1))
                assert cell.reflect('l') == cell
                assert cell.reflect('r') == Cell((1, -1))
        
class TestBoard:
        def test_basic(self):
                global board1, board2, board3
                board1  = Board.unserialize('1,-1,1,1,1,-1,-1,0,-1')
                board2  = Board(Cell(1,1), Cell(2,-1)) 
                board3  = Board(Cell(2,-1), Cell(3,1))
                assert str(board1) == deep_strip("""
                x|o|x
                x|x|o
                o| |o
                """)
                assert board2[1] == board2[-1,1]
                assert board2[1] == Cell(1,1)
                board2[5] = 1
                assert board2[5] == Cell((0,0),1)
                assert [cell for cell in board3] == [Cell(1),Cell(2,-1), Cell(3,1),Cell(4),Cell(5),Cell(6),Cell(7),Cell(8),Cell(9)]
                assert board1.mine() == [Cell(1,1), Cell(3,1), Cell(4,1), Cell(5,1)]
                assert board1.theirs() == [Cell(2,-1), Cell(6,-1), Cell(7,-1), Cell(9,-1)]
        
        def test_over(self):
                assert board1.empties() == [Cell(8)]
                assert not board1.over()[0]
                board1[8] = -1
                assert board1.over()[0]
                assert board1.over()[1] == 'user'
                assert board1.over()[2] == '7,8,9'
                board1[8] = 0

        def test_lanes(self):
                assert board1.lanes()[0] == [Cell(1,1),Cell(4,1),Cell(7,-1)]
                assert board1.row(board1[5]) == [Cell(4,1),Cell(5,1),Cell(6,-1)]
                assert board1.column(board1[5]) == [Cell(2,-1),Cell(5,1),Cell(8,0)]
                assert board1.diagonal(board1[1]) == [Cell(1,1),Cell(5,1),Cell(9,-1)]

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
    
        def test_rotate(self):
        
                assert str(board1.rotate(2)) == deep_strip("""
                o| |o
                o|x|x
                x|o|x
                """)
        
                assert board1.rotate(4) == board1
                assert board1.rotate(2).is_isomorphic(board1)

        def test_reflect(self):
                assert str(board1.reflect('v')) == deep_strip("""
                x|o|x
                o|x|x
                o| |o
                """)
                
                assert str(board1.reflect('h')) == deep_strip("""
                o| |o
                x|x|o
                x|o|x
                """)
                
                assert deep_strip(str(board1.reflect('l'))) == deep_strip("""
                x|x|o
                o|x| 
                x|o|o
                """)

                assert deep_strip(str(board1.reflect('r'))) == deep_strip("""
                o|o|x
                |x|o
                o|x|x
                """)
                assert board1.reflect('l').is_isomorphic(board1)
                assert board1.serialize() == '1,-1,1,1,1,-1,-1,0,-1'

        def test_randomMove(self):
                assert not board1.randomMove().filled

        def test_matchMove(self):
                board3[5]=1
                assert board2.matchMove(board3,Cell((1,1))) == Cell((-1,1))
                assert board2.matchMove(board1,Cell((1,1))) == False
                assert board2.matchMove(board2,Cell((1,1))) == Cell((1, 1))
