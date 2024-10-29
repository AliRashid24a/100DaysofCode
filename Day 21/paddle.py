from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, start_x):
        super().__init__()
        self.setheading(90)
        self.shape('square')
        self.color('pink')
        self.shapesize(stretch_wid=1,stretch_len=5)
        self.penup()
        self.goto(start_x,0)
        self.score = 0
    
    def upPress(self):
        self.forward(20)
    
    def downPress(self):
        self.backward(20)
