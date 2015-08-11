import turtle
from random import randint
def grow(trunkLength,height):
    if height == -1:
        return
    randomColor() 
    turtle.forward(trunkLength)
    turtle.left(45)
    grow(trunkLength * .5, height - 1)
    turtle.right(90)
    grow(trunkLength * .5, height - 1)
    turtle.left(45)
    turtle.pu()
    turtle.backward(trunkLength)
    turtle.pd()

def tree(trunkLength,height):
    turtle.speed(1)
    turtle.reset()
    turtle.left(90)
    turtle.pu()
    turtle.backward(200)
    turtle.pd()
    grow(trunkLength,height)

def randomColor():
    x = randint(0,6)
    if x == 0:
        turtle.pencolor("red")
    if x == 1:
        turtle.pencolor("orange")
    if x == 2:
        turtle.pencolor("yellow")
    if x == 3:
        turtle.pencolor("green")
    if x == 4:
        turtle.pencolor("blue")
    if x == 5:
        turtle.pencolor("purple")
    if x == 6:
        turtle.pencolor("brown")
