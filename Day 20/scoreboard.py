from turtle import Screen,Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.pencolor('white')
        self.hideturtle()
        self.score = -1
        self.highscore = 0
        self.update_score()
        self.reset()
        self.get_highscore()
        
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
        with open('Day 20\data.txt','w') as file:
            file.write(f"{self.score}")
    
    def get_highscore(self):
        try:
            with open('Day 20\data.txt',"r") as file:
                self.highscore = int(file.read())
        except:
            with open('Day 20\data.txt','w') as file:
                file.write("0")
        
    def reset(self):
        if self.score > self.highscore:
            self.update_highscore()
        self.setposition(0,250)
        self.clear()
        self.score = -1
        self.update_score()
