import turtle

def grow(trunkLength,height):
    if height == -1:
        return
    turtle.forward(trunkLength)
    turtle.left(45)
    grow(trunkLength * .5, height - 1)
    turtle.right(90)
    grow(trunkLength * .5, height - 1)
    turtle.left(45)
    turtle.backward(trunkLength)


def tree(trunkLength,height):
    turtle.speed(1)
    turtle.reset()
    turtle.left(90)
    turtle.pu()
    turtle.backward(200)
    turtle.pd()
    grow(trunkLength,height)
