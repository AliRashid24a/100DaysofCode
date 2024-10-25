from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

# game loop
def startGame():
    isGameOn = True
    while isGameOn:
        screen.update()
        time.sleep(0.05)
        # the snake moves by making the last node to follow the node ahead of it
        snake.moveSnake()

        # Detect collision with food
        if snake.head.distance(food) < 20:
            scoreboard.update_score()
            food.refresh()
            snake.extend()
            snake.changeColors()

        if snake.head.xcor() > 300 or snake.head.xcor() < -300 or \
        snake.head.ycor() > 300 or snake.head.ycor() < -300:
            isGameOn = False
        
        if snake.checkForCollisions() == False:
            isGameOn = False
    
    scoreboard.gameOver()
    food.clear()
    

# handle inputs to move the snake
screen.listen()
screen.onkeypress(snake.up,"Up")
screen.onkeypress(snake.down,"Down")
screen.onkeypress(snake.left,"Left")
screen.onkeypress(snake.right,"Right")
screen.onkeypress(startGame,"space")

    
        
        
    

















screen.exitonclick()