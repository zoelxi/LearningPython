# Python Class 2256
# Lesson 7 Problem 5 Part (b)
# Author: zxi (179194)

import turtle

class SuperAwesomeTurtle(turtle.Turtle):
    '''a super awesome turtle!'''

    def __init__(self):
        '''SuperAwesomeTurtle() -> SuperAwesomeTurtle
        creates a SuperAwesomeTurtle that responds to keypress events'''
        turtle.Turtle.__init__(self) 
        self.unit = 0 # begin not moving
        # create listeners for Up-Arrow, Down-Arrow, Left-Arrow, Right-Arrow, 's', and 'q' keypresses
        self.getscreen().onkey(self.inc_unit,'Up') 
        self.getscreen().onkey(self.dec_unit,'Down')
        self.getscreen().onkey(self.turn_left,'Left')
        self.getscreen().onkey(self.turn_right,'Right')
        self.getscreen().onkey(self.stop,'s')
        self.getscreen().onkey(self.quit,'q')
        self.go()

    def go(self):
        '''SuperAwesomeTurtle.go()
        moves turtle forward a number of units every 40 milliseconds'''
        self.forward(self.unit)
        self.getscreen().ontimer(self.go,40) # set 40 millisecond timer

    def inc_unit(self):
        '''SuperAwesomeTurtle.inc_unit()
        increases number of units turtle moves every 40 milliseconds by 1'''
        self.unit += 1

    def dec_unit(self):
        '''SuperAwesomeTurtle.dec_unit()
        decreases number of units turtle moves every 40 milliseconds by 1'''
        self.unit -= 1

    def turn_left(self):
        '''SuperAwesomeTurtle.turn_left()
        turns turtle 90 degrees to the left'''
        self.left(90)

    def turn_right(self):
        '''SuperAwesomeTurtle.turn_right()
        turns turtle 90 degrees to the right'''
        self.right(90)

    def stop(self):
        '''SuperAwesomeTurtle.stop()
        makes turtle come to full stop'''
        self.unit = 0

    def quit(self):
        '''SuperAwesomeTurtle.quit()
        closes window and ends program'''
        self.getscreen().bye()      

wn = turtle.Screen()
pete = SuperAwesomeTurtle()
wn.listen()
wn.mainloop()
