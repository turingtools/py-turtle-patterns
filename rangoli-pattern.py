import turtle
tt = turtle
tt.Screen()
tt.bgcolor('black')
tt.shape('arrow')
tt.setup(470, 800)
tt.Turtle()
tt.speed("fastest")


def singleColorShapeLoop(
    loop1, 
    loop2, 
    penSize, 
    color, 
    circleRadius = 0, 
    circleSteps = 0
):
    for i in range(loop1):
        for i in range(loop2):
            tt.pu()
            tt.goto(0,0)
            tt.pd()
            tt.color(color)
            tt.pensize(penSize)
            tt.circle(
                circleRadius,
                steps=circleSteps
            )
            tt.right(100)

def multiColorShapeLoop(
    loop1, 
    loop2, 
    penSize, 
    forwordSteps = [], 
    colors = [], 
    includeCircle = False
):
    for i in range(loop1):
        for i in range(loop2):
            tt.pensize(penSize)
            tt.goto(0,0)
            tt.color(colors[0])
            tt.forward(forwordSteps[0])

            if includeCircle: 
                tt.circle(5,steps=4)

            tt.right(60)
            tt.color(colors[1])
            tt.forward(forwordSteps[1])
            tt.right(120)
            tt.right(30)


singleColorShapeLoop(10, 2, 4, 'green', 30, 9)
singleColorShapeLoop(10, 2, 3, 'dark violet', 35, 9)
singleColorShapeLoop(10, 2, 0.5, 'yellow', 38, 9)
singleColorShapeLoop(10, 2, 0.5, 'red', 41, 9)
singleColorShapeLoop(10, 2, 0.5, 'cyan', 50, 9)
singleColorShapeLoop(6, 4, 1, 'plum', 55, 9)
multiColorShapeLoop(10, 2, 1, [100, 60], ["purple", "blue"])
multiColorShapeLoop(10, 2, 1, [120, 60], ["purple", "violet"], True)


tt.done()
