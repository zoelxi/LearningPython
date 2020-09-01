import turtle

def teleport_and_draw(x,y):
    carol.goto(x,y)

def teleport_and_no_draw(x,y):
    carol.penup()
    carol.goto(x,y)
    carol.pendown()
    
wn = turtle.Screen()
carol = turtle.Turtle()

wn.onclick(teleport_and_draw,1)    
wn.onclick(teleport_and_no_draw,2) 

wn.listen()
wn.mainloop()
