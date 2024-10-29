from turtle import Turtle,colormode
import random as rd
colormode(255)

class Car(Turtle):
    def __init__(self,xpos,ypos):
        super().__init__()
        self.penup()
        self.color(self.random_color())
        self.goto(280+xpos, ypos)
        self.shapesize(stretch_len=2)
        self.setheading(180)
        self.shape('square')
        self.defaultX = self.xcor()
        self.defaultY = self.ycor()

    def random_color(self):
        r = rd.randint(0,255)
        g = rd.randint(0,255)
        b = rd.randint(0,255)
        return (r,g,b)
    
    def move_forward(self, movespeed):
        self.forward(movespeed)

    def reset_position(self):
        newX = self.defaultX + rd.randint(0,200) 
        newY = self.defaultY + rd.randint(0,20)
        self.goto(newX,newY)