import turtle
from turtle import Turtle, Screen
import random
import colorgram

turtle.colormode(255)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color_tuple = (r, g, b)
    return color_tuple


timmy = Turtle()
timmy.shape("arrow")
timmy.speed("fastest")



def draw_spirograph(size_of_gap):
    heading = 0
    for _ in range(int(360 / size_of_gap)):
        timmy.color(random_color())
        timmy.circle(100)

        timmy.setheading(heading)
        heading += size_of_gap

draw_spirograph(1)


screen = Screen()
screen.exitonclick()