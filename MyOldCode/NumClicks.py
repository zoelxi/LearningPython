from tkinter import *

class NumClicks(Frame):

    def __init__(self,master):
        Frame.__init__(self,master)
        self.grid()
        self.button = Button(self,text = 'Click me!',command = self.print_numClicks)
        self.button.grid()
        self.messageBox = Label(self,text = '')
        self.messageBox.grid()
        self.numClicks = 0

    def print_numClicks(self):
        self.numClicks += 1
        self.messageBox['text'] = str(self.numClicks) + ' clicks so far'

root = Tk()
ncf = NumClicks(root)
ncf.mainloop()
