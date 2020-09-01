import turtle

def draw_square(t,size):
    for i in range(4):
        t.forward(size)
        t.right(90)

wn = turtle.Screen()
chloe = turtle.Turtle()
draw_square(chloe,10)
wn.mainloop()
