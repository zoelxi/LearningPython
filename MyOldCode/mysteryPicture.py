import turtle

turtle.setup(800,600) # Change the width of the drawing to 800px and the height to 600px.
wn = turtle.Screen()
sammy = turtle.Turtle()

inFile = open('mystery.txt','r')
for line in inFile:
    line = line.strip('\n')
    if line == 'UP':
        sammy.penup()
    elif line == 'DOWN':
        sammy.pendown()
    else:
        coordList = line.split()
        sammy.goto(int(coordList[0]),int(coordList[1]))

wn.mainloop()



