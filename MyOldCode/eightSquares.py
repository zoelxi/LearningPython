import turtle
wn = turtle.Screen ()
hongweiBigPig = turtle.Turtle ()
                    
for i in range(8):
    for j in range(4):
        hongweiBigPig.forward(-50)
        hongweiBigPig.left(90)
    hongweiBigPig.penup()
    hongweiBigPig.forward(50)
    hongweiBigPig.pendown()

wn.mainloop()
