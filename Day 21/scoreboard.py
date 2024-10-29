WIN_CONDITION = 5
from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("white")
        self.l_score = 0
        self.r_score = 0
        self.updateScoreboard()
    
    def updateScoreboard(self):
        self.clear()
        self.goto(-100,200)
        self.write(self.l_score,align="center",font=("Comic Sans",40,"normal"))
        self.goto(100,200)
        self.write(self.r_score,align="center",font=("Comic Sans",40,"normal"))

    def updateScoreL(self):
        if self.r_score == WIN_CONDITION:
            self.winner('Left')
        else:
            self.l_score += 1
            self.updateScoreboard()
        
    def updateScoreR(self):
        if self.r_score == WIN_CONDITION:
            self.winner('Right')
        else:
            self.r_score += 1
            self.updateScoreboard()
      
    def winner(self, player):
        self.goto(0,0)
        self.write(f"The {player} player has won!",align="center",font=("Comic Sans",40,"normal"))


        