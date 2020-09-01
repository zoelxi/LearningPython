def draw_square(t,size):
    for i in range(4):
        t.forward(size)
        t.right(90)

def increasing_squares(t,size):
    for i in range(9):
        draw_square(t,size+size*i)
        t.penup()
        t.right(180)
        t.forward(10)
        t.right(90)
        t.forward(10)
        t.right(90)
        t.pendown()

import turtle
wn = turtle.Screen()
chloe = turtle.Turtle()
increasing_squares(chloe,20)
wn.mainloop()
