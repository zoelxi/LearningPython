hour = int(input('Enter an hour: '))
minute = int(input('Enter a minute: '))

import turtle
wn = turtle.Screen()
chloe = turtle.Turtle()

for i in range(12):
    chloe.penup()
    chloe.forward(50)
    chloe.stamp()
    chloe.forward(-50)
    chloe.right(30)
    chloe.pendown()

chloe.left(90)
chloe.right(1/2*(hour*60+minute))
chloe.forward(20)
chloe.forward(-20)
chloe.left(1/2*(hour*60+minute))
chloe.right(6*minute)
chloe.forward(35)

chloe.hideturtle()

wn.mainloop()
