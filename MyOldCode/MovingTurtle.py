import turtle
import random

def move_forward():
    tRed.forward(random.randrange(1,51))
    tBlue.forward(random.randrange(1,51))
    tGreen.forward(random.randrange(1,51))

def turn_left():
    tRed.left(15)
    tBlue.left(30)
    tGreen.left(40)

def turn_right():
    tRed.right(15)
    tBlue.right(30)
    tGreen.right(40)
        
wn = turtle.Screen()
tRed = turtle.Turtle()
tRed.color('red')
tBlue = turtle.Turtle()
tBlue.color('blue')
tGreen = turtle.Turtle()
tGreen.color('green')

wn.onkey(move_forward,'Up')
wn.onkey(turn_left,'Left')
wn.onkey(turn_right,'Right')

wn.listen()
wn.mainloop()
