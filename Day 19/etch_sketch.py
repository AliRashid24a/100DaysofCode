import turtle as t

timmy = t.Turtle()
screen = t.Screen()

def move_forwards():
    timmy.forward(10)

def move_backwards():
    timmy.backward(10)

def rotate_clockwise():
    timmy.right(10)

def rotate_counterclockwise():
    timmy.left(10)

def clear():
    timmy.clear()
    timmy.penup()
    timmy.home()
    timmy.pendown()

screen.listen()
screen.onkey(key='w',fun=move_forwards)
screen.onkey(key='s',fun=move_backwards)
screen.onkey(key='a',fun=rotate_counterclockwise)
screen.onkey(key='d',fun=rotate_clockwise)
screen.onkey(key='c',fun=clear)
screen.exitonclick()
