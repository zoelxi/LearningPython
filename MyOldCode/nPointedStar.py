n = int(input('Enter an odd ositive integer n >= 3: '))

import turtle
wn = turtle.Screen()
chloe = turtle.Turtle()

angle = 180/n

chloe.speed(0)

for i in range(n):
    chloe.forward(300)
    chloe.right(180-angle)

wn.mainloop()
