from turtle import Turtle
import random as rd

class Snake(Turtle):
    def __init__(self):
        super().__init__()
        self.segments = []
        self.createSnake(3)
        self.head = self.segments[0]

    def createSnake(self,nSegments):
        x_pos = 0
        for i in range(nSegments):
            new_turtle = Turtle('square')
            new_turtle.penup()
            new_turtle.color('white')
            new_turtle.pensize(20)
            new_turtle.setpos(x_pos,0)
            self.segments.append(new_turtle)
            x_pos -= 20
    
    def moveSnake(self):
            # the snake moves by making the last node to follow the node ahead of it
            for i in range(len(self.segments)-1,0,-1):
                # get coords of node in front
                new_x = self.segments[i - 1].xcor()
                new_y = self.segments[i - 1].ycor()
                # move previous node to last nodes location
                self.segments[i].goto(new_x,new_y)
            # move head so that the snake moves 
            self.head.forward(20)
    
    def extend(self):
        prev_last_node = self.segments[-1]
        self.createSnake(1)
        self.segments[-1].goto(prev_last_node.xcor(),prev_last_node.ycor())
    
    def checkForCollisions(self):
        for i in range(len(self.segments)-1,1,-1):
            if self.head.distance(self.segments[i]) < 2:
                return False
        return True

    def up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)
    
    def down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)

    def left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)

    def right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)
    
    def changeColors(self):
        colors = ['red','orange','yellow','green','blue','purple']
        for i in range(len(self.segments)-1):
            self.segments[i].color(rd.choice(colors))
