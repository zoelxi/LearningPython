def random_walk(t,steps):
    for i in range(steps):
        t.forward(random.randrange(51))
        t.right(random.randrange(360))

import random
import turtle
wn = turtle.Screen()
chloe = turtle.Turtle()
wn.bgcolor("lightgreen")
chloe.shape("turtle")
chloe.color("magenta")
chloe.speed(10)

random_walk(chloe,100)

wn.mainloop()



              
    
