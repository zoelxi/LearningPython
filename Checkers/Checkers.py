######
#
# Zoe's implementation of Checkers
#
######

N = 8 # board dimensions
RED = 0
WHITE = 1

class Coord:
# functional class because it does not update the attributes
    def __init__(self,r,c):
        self.r = r # row number
        self.c = c # column number

    def row(self):
        return self.r

    def column(self):
        return self.c

    def legal_q(self):
        if 0 <= self.r < N and 0 <= self.c < N:
            return True
   
    def dir_left(self,dir):
        return Coord(self.r+dir,self.c-1)

    def dir_right(self,dir):
        return Coord(self.r+dir,self.c+1)

    def dir2_left(self,dir):
        return Coord(self.r+2*dir,self.c-2)

    def dir2_right(self,dir):
        return Coord(self.r+2*dir,self.c+2)

# end of class [Coord]

class Checker:

    def __init__(self,color):
        self.color = color
        self.king = False

    def king_q(self):
        return self.king

    def color(self):
        return self.color

# end of class [Checker]

class Board:

    def __init__(self):
        self.board = {}

    def set_at(self,coord,checker):
        r = coord.row()
        c = coord.column()
        self.board[(r,c)] = checker
        return

    def swap(self,coord,checker):
        tmp = self.get0_at(coord)
        self.set_at(coord,checker)
        return tmp

    def get0_at(self,coord):
        r = coord.row()
        c = coord.column()
        return self.board[(r,c)]

    def get1_at(self,coord):
        tmp = self.board[(r,c)]
        self.board[(r,c)] = None
        return tmp

    def get_between(self,coord1,coord2):
        tmp1 = (coord1[0]+coord2[0])/2
        tmp2 = (coord1[1]+coord2[1])/2
        return (tmp1,tmp2)

    def move_to(self,coord1,coord2):
    # moves piece from coord1 to coord2
        checker = self.get1_at(coord1)
        assert(checker is not None)
        assert(self.swap(coord2,checker) is None)
        return

    def jump_to(self,coord1,coord2):
        checker = self.get1_at(coord1)
        skip = self.get1_at(self.get_between(coord1,coord2))
        assert(checker is not None)
        assert(skip is not None)
        assert(checker.get_color() != skip.get_color())
        assert(self.swap(coord2,checker) is None)
        return

    def l_move_q(self,coord,dir):
        return self.get0_at(coord.dir_left(dir)) is None

    def r_move_q(self,coord,dir):
        return self.get0_at(coord.dir_right(dir)) is None

    def lr_move_q(self,coord,dir):
        return self.l_move_q(coord,dir) or self.r_move_q(coord,dir)

    def l_jump_q(self,coord,dir):
        return self.get0_at(coord.dir_left(dir)) is not None and self.get0_at(coord.dir_left(dir)).get_color() != self.get0_at(coord).get_color and self.get0_at(coord.dir2_left(dir)) is None

    def r_jump_q(self,coord,dir):
        return self.get0_at(coord.dir_right(dir)) is not None and self.get0_at(coord.dir_right(dir)).get_color() != self.get0_at(coord).get_color and self.get0_at(coord.dir2_right(dir)) is None

    def lr_jump_q(self,coord,dir):
        return self.l_jump_q(coord,dir) or self.r_jump_q(coord,dir)

# end of class [Board]


###### end of [Checkers.py] ######
