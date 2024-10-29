from turtle import Screen,Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.pencolor('white')
        self.hideturtle()
        self.score = -1
        self.highscore = 0
        self.reset()
        self.get_highscore()
        self.update_score()
        
    def update_score(self):
        self.score += 1
        self.clear()
        self.write(f'Score: {self.score}. High Score: {self.highscore}',False,align="center",font=("arial",14,'bold'))
    
    def gameOver(self):
        self.clear()
        self.goto(0,0)
        self.write(f'Game Over. Your final score is: {self.score}',False,align="center",font=("arial",24,'bold'))
    
    def update_highscore(self):
        self.highscore = self.score
        with open('data.txt',"w") as file:
            file.write(f"{self.score}")
    
    def get_highscore(self):
        with open('data.txt',"r") as file:
            res = file.read()
            self.highscore = int(res)

    def reset(self):
        if self.score > self.highscore:
            self.update_highscore()
        self.setposition(0,250)
        self.clear()
        self.score = -1
        self.update_score()
