"""A Beautiful Day in Nature."""
__author__ = "730320310"

from turtle import Turtle, colormode, done
colormode(255)


def trunk(lucy: Turtle, x: float, y: float, height: float) -> None: 
    """Draw a rectangle to make tree trunks."""
    lucy.penup()
    lucy.goto(x, y)
    lucy.pendown()
    # 5. Marker color
    lucy.color(131, 61, 14)
    #  4. fill color 
    lucy.begin_fill()
    lucy.speed(500)
    # draw 1st side
    lucy.forward(50)
    lucy.left(90)
    # draw 2nd side
    lucy.forward(height)
    lucy.left(90)
    # draw 3rd side
    lucy.forward(50)
    lucy.left(90)
    # draw 4th side 
    lucy.forward(height)
    lucy.left(90)
    lucy.end_fill()


def leaves(lila: Turtle, x: float, y: float, width: float) -> None:
    """Draw a square to make a patch of leaves."""
    lila.penup()
    lila.goto(x, y)
    lila.pendown()
    lila.color("green")
    lila.begin_fill()
    lila.speed(500)
    # drawing the body of the square with a loop
    # 3. loop usage
    i: int = 0
    while i < 4:
        lila.forward(width)
        lila.left(90)
        i = i + 1
    lila.end_fill()
    lila.hideturtle()


def sky(henry: Turtle, x: float, y: float, width: float) -> None:
    """Draw the sky with a big blue square."""
    henry.penup()
    henry.goto(x, y)
    henry.pendown()
    henry.color(176, 229, 255)
    henry.begin_fill()
    henry.speed(500)
    i: int = 0
    while i < 4:
        henry.forward(width)
        henry.left(90)
        i = i + 1
    henry.end_fill()


def sun(holden: Turtle, x: float, y: float) -> None:
    """Draw the sun with a circle."""
    # 8. Try something fun!
    holden.penup()
    holden.goto(x, y)
    holden.pendown()
    holden.color(249, 241, 65)
    holden.begin_fill()
    holden.speed(500)
    holden.circle(75, None, None)
    holden.end_fill()


def main() -> None:
    """The entrypoint of my scene."""
    # 1. Main
    t: Turtle = Turtle()
    # drawing the sky
    sky(t, -375, -375, 800)
    # drawing tree trunks
    # 2. Draw something twice
    trunk(t, -350, -325, 300)
    trunk(t, -200, -325, 250)
    trunk(t, 250, -325, 300)
    trunk(t, 100, -325, 250)
    # drawing leaves 
    leaves(t, -400, -25, 200)
    leaves(t, -235, -100, 125)
    leaves(t, 200, -25, 200)
    leaves(t, 75, -100, 125)
    # drawing the sun
    sun(t, 100, 150)
    done()


if __name__ == "__main__":
    main()