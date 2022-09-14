import turtle
turtle.goto(0, 0)

def mU():
    pos = turtle.pos()
    turtle.goto(pos[0], pos[1] + 5)
def mD():
    pos = turtle.pos()
    turtle.goto(pos[0], pos[1] - 5)
def mL():
    pos = turtle.pos()
    turtle.goto(pos[0] - 5, pos[1])
def mR():
    pos = turtle.pos()
    turtle.goto(pos[0] + 5, pos[1])
def pD():
    if turtle.isdown():
        turtle.penup()
    else:
        turtle.pendown()
def cl():
    turtle.clear()



turtle.onkey(mU, "Up")
turtle.onkey(mD, "Down")
turtle.onkey(mR, "Right")
turtle.onkey(mL, "Left")
turtle.onkey(pD, "space")
turtle.onkey(cl, "0")


turtle.listen()
turtle.mainloop()
