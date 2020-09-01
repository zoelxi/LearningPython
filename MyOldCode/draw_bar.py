import turtle
wn = turtle.Screen()
wn.bgcolor("lightgreen")
tess = turtle.Turtle()
tess.color("blue")

def draw_bar(t, height):
    """ Get turtle t to draw one bar, of height. """
    t.begin_fill()        # Start of the fill area
    t.left(90)
    t.forward(height)     # Draw up the left side
    t.write("  " + str(height))  # Write the data
    t.right(90)
    t.forward(40)         # Width of bar, along the top
    t.right(90)
    t.forward(height)     # And down again!
    t.left(90)            # Put the turtle facing the way we found it.
    t.end_fill()          # Fill in the bar
    t.forward(10)         # Leave small gap after each bar

xs = [48, 117, 200, 240, 160, 260, 220] # our data
for v in xs:              # Draw a bar for each number in the data
    if v >= 200:
        tess.fillcolor("green")
    else:
        tess.fillcolor("red")
    draw_bar(tess, v)

wn.mainloop()
