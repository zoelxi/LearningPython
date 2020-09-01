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

class ShotPutFrame(Frame):
    '''frame for a game of Shot Put'''

    def __init__(self,master,name):
        '''ShotPutFrame(master,name) -> ShotPutFrame
        creates a new Shot Put frame
        name is name of player'''
        Frame.__init__(self,master)
        self.grid()
        Label(self,text=name,font=('Arial',18)).grid(columnspan=2,sticky=W) # label for player's name
        # set up attempt num, score, and high score
        self.attemptScoreLabel = Label(self,text='Attempt: #1 Score: 0',font=('Arial',18))
        self.attemptScoreLabel.grid(row=0,column=2,columnspan=4)
        self.highScoreLabel = Label(self,text='High Score: 0',font=('Arial',18))
        self.highScoreLabel.grid(row=0,column=6,columnspan=2,sticky=E)
        # initialize game data
        self.score = 0
        self.highScore = 0
        self.attempt = 0
        self.numDie = 0
        # set up dice
        self.dice = []
        for n in range(8):
            self.dice.append(GUIDie(self,colorList=['red']+5*['black']))
            self.dice[n].grid(row=1,column=n)
        # set up buttons
        self.rollButton = Button(self,text='Roll',command=self.roll)
        self.rollButton.grid(row=2)
        self.stopButton = Button(self,text='Stop',state=DISABLED,command=self.stop)
        self.stopButton.grid(row=3)

    def roll(self):
        '''ShotPutFrame.roll()
        handler method for roll button click'''
        # roll die and add score to score for attempt
        self.dice[self.numDie].roll()
        self.score += self.dice[self.numDie].get_top()
        self.attemptScoreLabel['text'] = 'Attempt: #'+str(self.attempt+1)+' Score: '+str(self.score)
        # turn on stop button if this was first roll of attempt
        if self.stopButton['state'] == DISABLED:
            self.stopButton['state'] = ACTIVE
        # end attempt in foul if player rolls 1 
        if self.dice[self.numDie].get_top() == 1:
            self.score = 0
            self.rollButton['state'] = DISABLED
            self.stopButton['text'] = 'FOUL'
            self.attemptScoreLabel['text'] = 'FOULED ATTEMPT'
        # end attempt if 8 dice have been rolled without a foul
        elif self.numDie == 7:
            self.rollButton['state'] = DISABLED
        # otherwise continue to next die
        else:
            self.numDie += 1
            self.rollButton.grid(row=2,column=self.numDie)
            self.stopButton.grid(row=3,column=self.numDie)

    def stop(self):
        '''ShotPutFrame.stop()
        handler method for stop button click'''
        # update high score if attempt score greater than high score
        if self.score > self.highScore:
            self.highScore = self.score
            self.highScoreLabel['text'] = 'High Score: '+ str(self.score)
        self.attempt += 1
        # reset game for next attempt if fewer than 3 attempts had been made
        if self.attempt < 3:
            for n in range(8):
                pipList = self.dice[n].find_all()
                for pip in pipList:
                    self.dice[n].delete(pip)
            self.numDie = 0
            self.score = 0
            self.attemptScoreLabel['text'] = 'Attempt: #'+str(self.attempt+1)+' Score: '+str(self.score)
            self.rollButton.grid(row=2,column=0)
            self.stopButton.grid(row=3,column=0)
            self.stopButton['text'] = 'Stop'
            self.rollButton['state'] = ACTIVE
            self.stopButton['state'] = DISABLED
        # otherwise end game
        else:
            self.rollButton.grid_remove()
            self.stopButton.grid_remove()
            self.attemptScoreLabel['text'] = 'Game over'

# play the game
name = input('Enter your name: ')
root = Tk()
root.title('Shot Put')
game = ShotPutFrame(root,name)
game.mainloop()                             
