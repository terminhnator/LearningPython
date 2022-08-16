import turtle
from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


def move_forwards():
    tim.forward(10)

screen.listen()
screen.onkey(key="space", fun=move_forwards) #don't need the parentheses at the end of move_forwards because we don't do that when we pass a function into another function
screen.exitonclick()