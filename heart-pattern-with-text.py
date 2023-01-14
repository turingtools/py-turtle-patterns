import turtle
tt = turtle
tt.setup(width=460, height=800)
tt.Screen().bgcolor('black')
pen = tt.Turtle()
pen.pensize(10)
pen.speed(20)
pen.color('pink', 'green')

# Method to draw curve
def curve(): 
    # To draw the curve step by step
    for i in range(200): 
        pen.right(1)
        pen.forward(1)

# Method to draw full Heart
def drawHeartShape(color):  
    pen.fillcolor(color)
    pen.begin_fill()
    pen.left(140)
    pen.forward(113)
    curve() # Left Curve
    pen.left(120)
    curve() # Right Curve
    pen.forward(112)
    pen.end_fill()


def textToShow(text, size, fontFamily, color, xPos, yPos):

    pen.up()
    # x axis & y axis positions
    pen.setpos(xPos, yPos)
    pen.color(color)
    pen.write(
        text, # text to show
        font=(
            fontFamily, # font family
            size # font size
        )
    )

# to draw heart shape
drawHeartShape('red') 

# to show the text
textToShow(
    "  Subsribe \nTuring Tools",
    16,
    "Comic Sans MS",
    "pink",
    -60,
    70
)

pen.ht() # Hiding Turtle (turtle.hideturtle())

tt.exitonclick()
