from tkinter import *
import random

class GUIDie(Canvas):
    '''6-sided Die class for GUI'''

    def __init__(self,master,valueList=[1,2,3,4,5,6],colorList=['black']*6):
        '''GUIDie(master,[valueList,colorList]) -> GUIDie
        creates a GUI 6-sided die
          valueList is the list of values (1,2,3,4,5,6 by default)
          colorList is the list of colors (all black by default)'''
        # create a 60x60 white canvas with a 5-pixel grooved border
        Canvas.__init__(self,master,width=60,height=60,bg='white',\
                        bd=5,relief=GROOVE)
        # store the valuelist and colorlist
        self.valueList = valueList
        self.colorList = colorList
        # initialize the top value
        self.top = 1

    def get_top(self):
        '''GUIDie.get_top() -> int
        returns the value on the die'''
        return self.valueList[self.top-1]

    def roll(self):
        '''GUIDie.roll()
        rolls the die'''
        self.top = random.randrange(1,7)
        self.draw()

    def draw(self):
        '''GUIDie.draw()
        draws the pips on the die'''
        # clear old pips first
        self.erase()
        # location of which pips should be drawn
        pipList = [[(1,1)],
                   [(0,0),(2,2)],
                   [(0,0),(1,1),(2,2)],
                   [(0,0),(0,2),(2,0),(2,2)],
                   [(0,0),(0,2),(1,1),(2,0),(2,2)],
                   [(0,0),(0,2),(1,0),(1,2),(2,0),(2,2)]]
        for location in pipList[self.top-1]:
            self.draw_pip(location,self.colorList[self.top-1])

    def draw_pip(self,location,color):
        '''GUIDie.draw_pip(location,color)
        draws a pip at (row,col) given by location, with given color'''
        (centerx,centery) = (17+20*location[1],17+20*location[0])  # center
        self.create_oval(centerx-5,centery-5,centerx+5,centery+5,fill=color)

    def erase(self):
        '''GUIDie.erase()
        erases all the pips'''
        pipList = self.find_all()
        for pip in pipList:
            self.delete(pip)


class GUIFreezeableDie(GUIDie):
    '''a GUIDie that can be "frozen" so that it can't be rolled'''

    def __init__(self,master,valueList=[1,2,3,4,5,6],colorList=['black']*6):
        '''GUIFreezeableDie(master,[valueList,colorList]) -> GUIFreezeableDie
        creates a GUI 6-sided freeze-able die
          valueList is the list of values (1,2,3,4,5,6 by default)
          colorList is the list of colors (all black by default)'''
        GUIDie.__init__(self,master,valueList,colorList)
        self.isFrozen = False  # die starts out unfrozen

    def is_frozen(self):
        '''GUIFreezeableDie.is_frozen() -> bool
        returns True if the die is frozen, False otherwise'''
        return self.isFrozen
    
    def toggle_freeze(self):
        '''GUIFreezeableDie.toggle_freeze()
        toggles the frozen status'''
        self.isFrozen = not self.isFrozen
        if self.isFrozen:
            self['bg'] = 'gray'
        else:
            self['bg'] = 'white'

    def roll(self):
        '''GuiFreezeableDie.roll()
        overloads GUIDie.roll() to not allow a roll if frozen'''
        if not self.isFrozen:
            GUIDie.roll(self)

class DiscusFrame(Frame):

    def __init__(self,master,name):
        Frame.__init__(self,master)
        self.grid()
        Label(self,text=name,font=('Arial',18)).grid(columnspan=2,sticky=W) 
        self.attemptScoreLabel = Label(self,text='Attempt: #1 Score: 0',font=('Arial',18))
        self.attemptScoreLabel.grid(row=0,column=2,columnspan=3)
        self.highScoreLabel = Label(self,text='High Score: 0',font=('Arial',18))
        self.highScoreLabel.grid(row=0,column=6)
        self.helpLabel = Label(self,text='Click Roll button to start',font=('Arial',18))
        self.helpLabel.grid(row=3,column=0,columnspan=5)
        self.score = 0
        self.highScore = 0
        self.attempt = 0
        self.evens = 0
        self.frozen = -1
        self.dice = []
        for n in range(5):
            self.dice.append(GUIDie(self,colorList=['red','black','red','black','red','black'))
            self.dice[n].grid(row=1,column=n)
        self.rollButton = Button(self,text='Roll',command=self.roll)
        self.rollButton.grid(row=1,column=6)
        self.freezeButton = Button(self,text='Freeze',state=DISABLED,command=self.freeze)
        self.freeze = []
        for n in range(5):
            self.freezeButton.grid(row=2,column=n)
            self.freeze.append(self.freezeButton)
        self.stopButton = Button(self,text='Stop',state=DISABLED,command=self.stop)
        self.stopButton.grid(row=2,column=6)

    def roll(self):
        if self.frozen != 0:
            for n in range(5):
                self.dice[n].roll()
                if self.dice[n].get_top() % 2 == 0:
                    self.score += self.dice[n].get_top()
                    self.attemptScoreLabel['text'] = 'Attempt : #'+str(self.attempt)+' Score: '+str(score)
                    self.evens += 1
                    self.freeze[n]['state'] = ACTIVE
            self.frozen = 0
            self.helpLabel['text'] = 'Click Stop button to keep'
            if self.evens = 0:
                self.helpLabel['text'] = 'Click FOUL button to continue'
                self.attemptScoreLabel['text'] = 'FOULED ATTEMPT'
                self.rollButton['state'] = DISABLED

    
        
        


        
    
