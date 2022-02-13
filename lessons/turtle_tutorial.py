"""Turtle practice!"""
from turtle import Turtle, colormode, done
colormode(255)
leo: Turtle = Turtle()

leo.speed(50)
leo.hideturtle()
leo.color(99, 204, 250)
leo.penup()
leo.goto(45, 60)
leo.pendown()
leo.begin_fill()
i: int = 0
while i < 3:
    leo.forward(300)
    leo.left(120)
    i = i + 1
leo.end_fill()

bob: Turtle = Turtle()

bob.pencolor("black")
bob.penup()
bob.goto(45, 60)
bob.pendown()
i: int = 0
side_length: float = 300
while i < 3:
    bob.forward(side_length)
    bob.left(120)
    i = i + 1
i: int = 0
while i < 9:
    side_length = side_length * 0.97
    bob.forward(side_length)
    bob.left(122)
    i = i + 1
done()

