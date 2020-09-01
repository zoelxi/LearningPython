from tkinter import *

class CheckersSquare(Canvas):

    def __init__(self,master,r,c):
        self.color = 'dark green'
        if r%2==c%2:
            self.color = 'blanched almond'
        Canvas.__init__(self,master,width=54,height=54,bg=self.color,highlightbackground=self.color)
        self.grid(row=r,column=c)
        self.coord = (r,c)
        self.bind('<Button>',master.click)

    def get_coords(self):
        return self.coord

    def get_color(self):
        return self.color

    def remove_checker(self):
        ovalList = self.find_all()
        for oval in ovalList:
            self.delete(oval)

    def make_color(self,color):
        self.remove_checker()
        self.create_oval(10,10,50,50,fill=color)

    def make_king(self):
        self.create_text(30,42,fill='black',font=('Arial',50),text='*')
        
class CheckersBoard:

    def __init__(self):
        self.board = {}
        for row in range(8):
            for column in range(8):
                coords = (row,column)
                if coords[0]<3 and coords[0]%2 != coords[1]%2:
                    self.board[coords] = 0
                elif coords[0]>4 and coords[0]%2 != coords[1]%2:
                    self.board[coords] = 1
                else:
                    self.board[coords] = -1
        self.currentPlayer = 0
        self.direction = [1,-1]
        self.valid = False
        self.mustJump = False
        self.lastCoords = None
        self.endgame = -1
        
    def get_checker(self,coords):
        return self.board[coords]

    def get_player(self):
        return self.currentPlayer

    def get_endgame(self):
        return self.endgame

    def next_player(self):
        self.lastCoords = None
        self.currentPlayer = 1-self.currentPlayer

    def get_player_coords(self):
        return [coords for coords in self.board if self.board[coords] == self.currentPlayer]

    def get_jump_coords(self,origCoords,direction):
        if 0 <= origCoords[0]+2*direction <= 7:
            if origCoords[1]+2 <= 7 and origCoords[1]-2 >= 0:
                return [(origCoords[0]+2*direction,origCoords[1]+2),(origCoords[0]+2*direction,origCoords[1]-2)]
            elif origCoords[1]+2 <= 7:
                return [(origCoords[0]+2*direction,origCoords[1]+2)]
            elif origCoords[1]-2 >= 0:
                return [(origCoords[0]+2*direction,origCoords[1]-2)]
            else:
                return []
        else:
            return []

    def q_jump(self,origCoords,direction):
        for jCoords in self.get_jump_coords(origCoords,direction):
            if self.can_jump(origCoords,jCoords,direction):
                return True
        return False

    def can_move(self,origCoords,moveCoords,direction):
        player = self.piece2player(self.board[origCoords])
        if player == self.currentPlayer and self.board[moveCoords] == -1\
        and moveCoords[0] == origCoords[0]+direction\
        and (moveCoords[1] == origCoords[1]+1 or moveCoords[1] == origCoords[1]-1):
            return True
        else:
            return False

    def piece2player(self,piece):
        if piece==2:
            return 0
        if piece==3:
            return 1
        return piece         

    def can_jump(self,origCoords,moveCoords,direction):
        player = self.piece2player(self.board[origCoords])
        if moveCoords[1] < origCoords[1]:
            if 0 <= origCoords[0]+direction <= 7 and origCoords[1]-1 >= 0:
                if player == self.currentPlayer and self.board[moveCoords] == -1\
                and self.piece2player(self.board[(origCoords[0]+direction,origCoords[1]-1)]) == 1-player\
                and moveCoords[0] == origCoords[0]+2*direction\
                and (moveCoords[1] == origCoords[1]+2 or moveCoords[1] == origCoords[1]-2):
                    return True
            else:
                return False
        elif moveCoords[1] > origCoords[1]:
            if 0 <= origCoords[0]+direction <= 7 and origCoords[1]+1 <= 7:
                if player == self.currentPlayer and self.board[moveCoords] == -1\
                and self.piece2player(self.board[(origCoords[0]+direction,origCoords[1]+1)]) == 1-player\
                and moveCoords[0] == origCoords[0]+2*direction\
                and (moveCoords[1] == origCoords[1]+2 or moveCoords[1] == origCoords[1]-2):
                    return True
            else:
                return False

    def move(self,origCoords,moveCoords,direction):
        canMove = self.can_move(origCoords,moveCoords,direction)
        canJump = self.can_jump(origCoords,moveCoords,direction)
        if canMove or canJump:
            if canJump:
                if moveCoords[1] < origCoords[1]:
                    self.board[(origCoords[0]+direction,origCoords[1]-1)] = -1
                elif moveCoords[1] > origCoords[1]:
                    self.board[(origCoords[0]+direction,origCoords[1]+1)] = -1
                self.mustJump = False
            self.valid = True
            piece = self.board[origCoords]
            self.board[origCoords] = -1
            self.board[moveCoords] = piece
            if moveCoords[0] == 7 and self.currentPlayer == 0:
                self.board[moveCoords] = 2
            elif moveCoords[0] == 0 and self.currentPlayer == 1:
                self.board[moveCoords] = 3
            if canJump:
                if self.q_jump(moveCoords,direction):
                    self.lastCoords = moveCoords
                else:
                    self.next_player()
            else:
                self.next_player()
        else:
            self.valid = False

    def get_legal_moves(self):
        moves = 0
        direction1 = [self.direction[self.currentPlayer]]
        direction2 = self.direction[1-self.currentPlayer]
        if len(self.get_player_coords()) == 0:
            return moves
        else:
            for coords in self.get_player_coords():
                pCoords = coords
                if self.board[pCoords] in [2,3]:
                    direction1.append(direction2)
                for row in range(8):
                    for column in range(8):
                        mCoords = (row,column)
                        for direction in direction1:
                            if self.can_move(pCoords,mCoords,direction) or self.can_jump(pCoords,mCoords,direction):
                                moves += 1
            return moves

    def check_endgame(self):
        if self.get_legal_moves() == 0:
            self.endgame = 1-self.currentPlayer

class CheckersGame(Frame):

    def __init__(self,master):
        Frame.__init__(self,master,bg='white')
        self.grid()
        self.colors = ('red','white')
        self.board = CheckersBoard()
        self.clickCoords = []
        self.jumpCoords = []
        self.squares = {}
        for row in range(8):
            for column in range(8):
                rc = (row,column)
                self.squares[rc] = CheckersSquare(self,row,column)
        self.rowconfigure(8,minsize=3)
        self.turnLabel = Label(self,text='Turn:',font=('Arial',18))
        self.turnLabel.grid(row=9,column=1)
        self.messageLabel = Label(self,text='',font=('Arial',18))
        self.messageLabel.grid(row=9,column=4,columnspan=3)
        self.turnSquare = CheckersSquare(self,9,2)
        self.turnSquare['bg'] = 'silver'
        self.turnSquare['highlightbackground'] = 'silver'
        self.turnSquare.make_color('red')
        self.turnSquare.unbind('<Button>')
        self.update_display()

    def update_display(self):
        for row in range(8):
            for column in range(8):
                rc = (row,column)
                checker = self.board.get_checker(rc)
                if checker in [0,1]:
                    self.squares[rc].make_color(self.colors[checker])
                elif checker in [2,3]:
                    self.squares[rc].make_color(self.colors[checker-2])
                    self.squares[rc].make_king()
                else:
                    self.squares[rc].remove_checker()
        newPlayer = self.board.get_player()
        oldPlayer = 1-newPlayer
        self.turnSquare.make_color(self.colors[newPlayer])
        if self.board.valid == True and self.board.mustJump == False:
            self.messageLabel['text'] = ''
        self.clickCoords = []
        self.jumpCoords = []
        endgame = self.board.get_endgame()
        if endgame != -1:
            winner = self.colors[endgame]
            endgameMessage = '{} wins!'.format(winner.title())
            self.messageLabel['text'] = endgameMessage
            for square in self.squares.values():
                square.unbind('<Button>')

    def click(self,event):
        coords = event.widget.get_coords()
        self.clickCoords.append(coords)
        self.squares[self.clickCoords[-1]]['highlightbackground'] = 'black'
        direction1 = [self.board.direction[self.board.get_player()]]
        direction2 = self.board.direction[1-self.board.get_player()]
        if self.board.board[self.clickCoords[0]] in [2,3]:
            direction1.append(direction2)
        if len(self.clickCoords) == 2:
            # if self.board.lastCoords is not None:
                # if self.clickCoords[0] != self.board.lastCoords:
                    # self.messageLabel['text'] = 'Continue the jump!'
                    # self.squares[self.clickCoords[0]]['highlightbackground'] = self.squares[self.clickCoords[0]].get_color()
                    # self.squares[self.clickCoords[1]]['highlightbackground'] = self.squares[self.clickCoords[1]].get_color()
                    # self.clickCoords = []
                    # return
            self.squares[self.clickCoords[0]]['highlightbackground'] = self.squares[self.clickCoords[0]].get_color()
            self.squares[self.clickCoords[1]]['highlightbackground'] = self.squares[self.clickCoords[1]].get_color()
            for pCoord in self.board.get_player_coords():
                for direction in direction1:
                    self.board.mustJump = False
                    for jCoord in self.board.get_jump_coords(pCoord,direction):
                        if self.board.can_jump(pCoord,jCoord,direction):
                            self.jumpCoords.append((pCoord,jCoord))
                            self.messageLabel['text'] = 'You must jump!'
                            self.board.mustJump = True
                    if self.board.mustJump:
                        break
            if not self.board.mustJump or (self.clickCoords[0],self.clickCoords[1]) in self.jumpCoords:
                for direction in direction1:
                    self.board.valid = False
                    self.board.move(self.clickCoords[0],self.clickCoords[1],direction)
                    if self.board.valid:
                        break
                if not self.board.valid:
                    self.messageLabel['text'] = 'Your move is invalid!'
            self.board.check_endgame()
            self.update_display()

def play_checkers():
    root = Tk()
    root.title('Checkers')
    cg = CheckersGame(root)
    cg.mainloop()

play_checkers() 
