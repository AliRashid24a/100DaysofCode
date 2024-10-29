from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time as t


screen = Screen()
screen.setup(800,600)
screen.title("Pong Game")
screen.bgcolor("Black")
screen.tracer(0)

ball = Ball()

l_paddle = Paddle(-340)
r_paddle = Paddle(340)

scoreboard = Scoreboard()

screen.listen()

if r_paddle.ycor() < 280 or (r_paddle.ycor() > -280 and r_paddle.ycor() > 0):
    screen.onkeypress(r_paddle.upPress,"Up")
    screen.onkeypress(r_paddle.downPress,"Down")

if l_paddle.ycor() < 280 or (r_paddle.ycor() > -280 and l_paddle.ycor() > 0):
    screen.onkeypress(l_paddle.upPress,"w")
    screen.onkeypress(l_paddle.downPress,"s")

isGameOn = True
while isGameOn:
    screen.update()

    t.sleep(0.03)
    ball.move()

    #check colliosn with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounceY()
    
    # check colliosn with paddle
    if ball.distance(r_paddle) < 60 and ball.xcor() > 320 or ball.distance(l_paddle) < 60 and ball.xcor() < -320:
        ball.bounceX()

    # paddle misses the ball
    if ball.xcor() < -380:
        scoreboard.updateScoreR()
        ball.reset()
    if ball.xcor() > 380:
        scoreboard.updateScoreL()
        ball.reset()

    







