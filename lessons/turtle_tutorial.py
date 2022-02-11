"""Turtle practice!"""
from turtle import Turtle, colormode, done
colormode(255)
leo: Turtle = Turtle()

leo.color(99, 204, 250)
leo.penup()
leo.goto(45, 60)
leo.pendown()
leo.begin_fill()
i: int = 0
while i < 3:
    leo.forward(300)
    leo.right(120)
    i = i + 1
leo.end_fill()
done()