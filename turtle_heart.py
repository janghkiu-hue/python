#turtle_heart.py
import turtle
turtle.bgcolor("black")
turtle.pensize(5)

def curve():
    for i in range(200):
        turtle.right(1)
        turtle.forward(1)


turtle.speed(0)
turtle.color("red" , "blue")

turtle.begin_fill()
turtle.left(140)
turtle.forward(111)
curve()

turtle.left(120)
curve()
turtle.forward(111)
turtle.end_fill()
turtle.hideturtle()
