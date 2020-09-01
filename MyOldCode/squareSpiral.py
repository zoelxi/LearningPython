import turtle
wn = turtle.Screen()
hongweiBigPig = turtle.Turtle()

hongweiBigPig.forward(10)
hongweiBigPig.left(90)
size = 20
for i in range(4):
    for j in range(4):
        hongweiBigPig.forward(size)
        hongweiBigPig.left(90)
        size = size + 10

wn.mainloop()
