from turtle import Turtle

def ready_race(num_turtles:int):
    turtles = []
    colors = ['red','orange','yellow','green','blue','purple']
    ypos = 0
    for i in range(num_turtles):
        temp_turtle = Turtle(shape='turtle')
        temp_turtle.color(colors[i])
        temp_turtle.penup()
        temp_turtle.goto(-240,-100+ypos)
        turtles.append(temp_turtle)
        ypos+= 40
    return turtles