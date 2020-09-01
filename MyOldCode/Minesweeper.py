from tkinter import *
from tkinter import messagebox
import random

class MinesweeperCell(Label):
    '''represents a Minesweeper cell'''

    def __init__(self,master):
        '''MinesweeperCell(master) -> MinesweeperCell
        creates a new Minesweeper cell'''
        Label.__init__(self,master,height=1,width=2,text='',\
                       relief = 'raised',bg='white',font=('Arial',18))
        self.coord = (-1,-1) # (row,column) coordinate tuple
        self.adjBombs = -1
        self.bomb = False
        self.exposed = False
        self.flagged = False
        # set up listeners
        self.bind('<Button-1>',self.expose)
        self.bind('<Button-2>',self.flag)

    def expose(self,event):
        '''MinesweeperCell.expose(event)
        handler method for left mouse click
        exposes cell'''
        colormap = ['','blue','darkgreen','red','purple','maroon','cyan','black','dim gray'] # colors for different numbers
        if not self.flagged and not self.exposed: # only acts on cells that are not flagged and not exposed
            if not self.bomb:
                self.exposed = True
                self['bg'] = 'silver'
                self['relief'] = 'sunken'
                self.adjBombs = self.master.find_adj_bombs(self.coord) # find number of adjacent bombs
                # display colored number of adjacent bombs if there are any
                if self.adjBombs > 0:
                    self['text'] = self.adjBombs
                    self['fg'] = colormap[self.adjBombs]
                # otherwise auto-expose adjacent cells
                else:
                    self.master.auto_expose(self.coord,'<Button-1>')
                self.master.exposedCount += 1
                # check for win
                if self.master.find_win():
                    messagebox.showinfo('Minesweeper','Congratulations -- you won!',parent=self)
                    self.master.end_game()
            # player loses if exposed cell contains bomb
            else:
                messagebox.showerror('Minesweeper','KABOOM! You lose.',parent=self)
                self.master.display_bombs()
                self.master.end_game()

    def flag(self,event):
        '''MinesweeperCell.flag(event)
        handler method for right mouse click
        flags cell'''
        if not self.exposed: # only acts on cells that are not exposed
            # flags not flagged cells
            if not self.flagged:
                self.flagged = True
                self['text'] = '*'
                self.master.dec_rem_bombs() # decreases bombs remaining count by 1
            # removes flag from flagged cells
            else:
                self.flagged = False
                self['text'] = ''
                self.master.inc_rem_bombs() # increases bombs remaining count by 1

class MinesweeperUnit:
    '''represents a Minesweeper unit (a square of 9 cells)'''

    def __init__(self,unit):
        '''MinesweeperUnit(unit) -> Minesweeper Unit
        creates a new Minesweeper unit with MinesweeperCells in dict unit'''
        self.unit = unit # store dict of MinesweeperCell

    def get_cell_list(self):
        '''MinesweeperUnit.get_cell_list() -> list
        returns list of MinesweeperCells'''
        return list(self.unit.values())

class MinesweeperGrid(Frame):
    '''object for Minesweeper grid'''

    def __init__(self,master,width,height,numBombs):
        '''MinesweeperGrid(master,width,height,numBombs)
        creates a new Minesweeper grid with given numbers of columns, rows, and bombs'''
        # initialize a new Frame
        Frame.__init__(self,master,bg='black') 
        self.grid()
        self.numColumns = width
        self.numRows = height
        self.numBombs = numBombs
        self.remBombsCount = self.numBombs
        self.exposedCount = 0 # create a counter for number of exposed cells
        # create label for number of remaining bombs
        self.bombLabel = Label(self,bg='white',text=str(self.numBombs),font=('Arial',24)) 
        self.bombLabel.grid(row=self.numRows+1,column=0,columnspan=self.numColumns)
        # create cells
        self.cells = {} # set up dict for cells
        for row in range(self.numRows):
            for column in range(self.numColumns):
                coord = (row,column)
                newCell = MinesweeperCell(self)
                newCell.coord = coord
                self.cells[coord] = newCell
                self.cells[coord].grid(row=row,column=column)
        cellList = [cell for cell in self.cells.values()] 
        # randomly assign given number of bombs to cells
        for b in range(self.numBombs):
            cell = random.choice(cellList)
            cell.bomb = True
            cellList.remove(cell)
        # create units
        self.units = {}
        for coord in self.cells:
            unitCells = {} 
            for i in range(-1,2):
                for j in range(-1,2):
                    # add cell to unit dict if coord valid
                    if 0<=coord[0]+i<self.numRows and 0<=coord[1]+j<self.numColumns:
                        unitCells[(coord[0]+i,coord[1]+j)] = self.cells[(coord[0]+i,coord[1]+j)]    
            self.units[coord] = MinesweeperUnit(unitCells) # add unit to dict of units with center cell coord as key
        
    def find_adj_bombs(self,coord):
        '''MinesweeperGrid.find_adj_bombs(coord) -> int
        returns number of bombs adjacent to cell with given coord'''
        adjBombCount = 0
        # count number of adjacent cells with bombs
        for cell in self.units[coord].get_cell_list():
            if cell.bomb:
                adjBombCount += 1
        return adjBombCount

    def auto_expose(self,coord,event):
        '''MinesweeperGrid.auto_expose(coord,event)
        exposes cells adjacent to cell with given coord'''
        for cell in self.units[coord].get_cell_list():
            cell.expose(event)

    def dec_rem_bombs(self):
        '''MinesweeperGrid.dec_rem_bombs()
        decreases remaining bombs count by 1'''
        self.remBombsCount -= 1
        self.bombLabel['text'] = str(self.remBombsCount)

    def inc_rem_bombs(self):
        '''MinesweeperGrid.inc_rem_bombs()
        increases remaining bombs count by 1'''
        self.remBombsCount += 1
        self.bombLabel['text'] = str(self.remBombsCount)

    def display_bombs(self):
        '''MinesweeperGrid.display_bombs()
        displays not flagged bombs'''
        for cell in self.cells.values():
            if cell.bomb and not cell.flagged:
                cell['bg'] = 'red'
                cell['text'] = '*'

    def find_win(self):
        '''MInesweeperGrid.find_win() -> bool
        returns True if all cells without bombs are exposed'''
        if self.exposedCount == self.numRows*self.numColumns-self.numBombs:
            return True

    def end_game(self):
        '''MinesweeperGrid.end_game()
        makes all cells unable to be exposed'''
        for cell in self.cells.values():
            cell.exposed = True
            
def play_minesweeper(width,height,numBombs):
    '''play_minesweeper(width,height,numBombs)
    plays Minesweeper on a width by height board with given number of bombs'''
    root = Tk()
    root.title('Minesweeper')
    mg = MinesweeperGrid(root,width,height,numBombs)
    root.mainloop()

print(play_minesweeper(12,10,15))
                           
        

                            


        
            


