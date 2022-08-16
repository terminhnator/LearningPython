# import colorgram
#
# colors = colorgram.extract('image.jpg', 20)
#
# rgb_colors = []
#
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     color_tuple = (r, g , b)
#     rgb_colors.append(color_tuple)

# print(rgb_colors)
import turtle

color_list = [(236, 35, 108), (221, 232, 237), (145, 28, 64), (239, 75, 35), (6, 148, 93), (232, 238, 234), (231, 168, 40), (184, 158, 46), (44, 191, 233), (27, 127, 195), (126, 193, 74), (253, 223, 0), (85, 28, 93), (173, 36, 97), (246, 219, 44), (44, 172, 112), (215, 130, 165), (215, 56, 27)]

from turtle import Turtle, Screen
import random


tim = Turtle()
tim.penup()
tim.speed("fastest")

turtle.colormode(255)

tim.setpos(-176.78, -176.78)

number_of_dots = 100

for dot_count in range(1, number_of_dots + 1):
    random_color = color_list[random.randint(0,17)]
    tim.dot(20, random_color)
    tim.forward(50)

    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(360)
tim.hideturtle()













screen = Screen()
screen.exitonclick()