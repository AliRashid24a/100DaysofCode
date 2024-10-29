from turtle import Turtle

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape('turtle')
        self.color('white')
        self.reset_position()
        self.setheading(90)
    
    def move_forward(self):
        self.forward(20)

    def reset_position(self):
        self.goto(0,-250)
