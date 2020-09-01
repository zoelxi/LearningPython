def draw_histogram(t,dataList):
    n = 0
    k = 0
    for i in range(11):
        for j in range(len(dataList)):
            if k == dataList[j]:
                n += 1
        t.write("  " + str(k))
        t.forward(20)
        t.left(90)
        t.forward(20*n)
        t.left(90)
        t.forward(20)
        t.left(90)
        t.forward(20*n)
        t.left(90)
        t.penup()
        t.forward(40)
        t.pendown()
        k += 1
        n = 0

import turtle
turtle.setup(600,300) 
wn = turtle.Screen()
bob = turtle.Turtle()
dataList = [6,8,0,7,7,9,2,9,10,4,8,7,6,9,1,4,6,7,5,7,2,10,4,5,5,6,8]
bob.penup()
bob.back(200)
bob.pendown()
draw_histogram(bob,dataList)
wn.mainloop()
