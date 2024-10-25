from turtle import Screen,Turtle

class Scoreboard(Turtle):
    def __init__(self, shape = "classic", undobuffersize = 1000, visible = True):
        super().__init__(shape, undobuffersize, visible)
        self.pencolor('white')
        self.hideturtle()
        self.penup()
        self.setposition(0,250)
        self.score = -1
        self.pendown()
        self.update_score()

    def update_score(self):
        self.score += 1
        self.clear()
        self.write(f'Score: {self.score}',False,align="center",font=("arial",14,'bold'))
    
    def gameOver(self):
        self.clear()
        self.home()
        self.write(f'Game Over. Your final score is: {self.score}',False,align="center",font=("arial",24,'bold'))
