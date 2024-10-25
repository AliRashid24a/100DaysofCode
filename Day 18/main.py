import turtle
import random as rd

turtle.colormode(255)
timmy = turtle.Turtle("turtle")

timmy.speed(4)
timmy.pensize(5)

#Square
#for i in range(4):
  #  timmy.forward(100)
    #timmy.circle(100)
    #timmy.left(120)

def random_color():
    r = rd.randint(0,255)
    g = rd.randint(0,255)
    b = rd.randint(0,255)
    colors = (r,g,b)
    return colors

# draw a ngon
def draw_ngon(sides):
    side_angle = 360/sides
    for i in range(sides):
        timmy.left(side_angle)
        timmy.forward(100)

#random walk
def random_walk(steps):
    directions = [0,90,180,270]
    for i in range(steps):
        timmy.color(random_color())
        direction = rd.choice(directions)
        timmy.setheading(direction)
        timmy.forward(30)

#random_walk(200)

def spirograph(circles,rad):
    timmy.pendown()
    for i in range(circles):
        timmy.color(random_color())
        timmy.circle(rad)
        timmy.left(360/circles)
    timmy.penup()

#spirograph(5)

def spot_painting(grid_size):
    timmy.hideturtle()
    timmy.pensize(15)
    timmy.penup()
    for j in range(grid_size[1]):
        timmy.setposition(-50,j*50)
        for i in range(grid_size[0]):
           # random_walk(10)
            timmy.color(random_color())
            #spirograph(30,50)
            timmy.dot()
            timmy.forward(50)
        
screen = turtle.Screen()
screen.bgcolor('black')
random_walk(200)
#spot_painting([5,5])

screen.exitonclick()
