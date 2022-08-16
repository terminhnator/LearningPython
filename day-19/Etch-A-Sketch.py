from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


##Move forward function
def move_forwards():
    tim.forward(10)

##Move backwards function
def move_backwards():
    tim.backward(10)

##Counter-clockwise rotation
def turn_left():
    tim.left(10)

##Clockwise rotation
def turn_right():
    tim.right(10)

##Clear drawing
def clear():
    tim.reset()


screen.listen()
screen.onkeyrelease(key="w", fun=move_forwards)
screen.onkeyrelease(key="s", fun=move_backwards)
screen.onkeyrelease(key="a", fun=turn_left)
screen.onkeyrelease(key="d", fun=turn_right)
screen.onkeyrelease(key="c", fun=clear)
screen.exitonclick()