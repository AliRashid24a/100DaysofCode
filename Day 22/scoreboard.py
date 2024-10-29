from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(-230,250)
        self.color('white')
        self.level = 0
        self.update_level()
    
    def update_level(self):
        self.pendown()
        self.clear()
        self.write(f"Level: {self.level}",align='center',font=('Comic Sans',15,'normal'))
        self.level += 1

    def game_over(self):
        self.goto(0,0)
        self.clear()
        self.write(f"GAME OVER.",align='center',font=('Comic Sans',20,'normal'))



