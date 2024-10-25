from turtle import Turtle
import random as rd

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.penup()
        self.shapesize(stretch_len=0.75, stretch_wid=0.75)
        self.color('pink')
        self.speed(0)
        self.refresh()

    def refresh(self):
        self.goto(rd.randint(-270,270),rd.randint(-270,270))


