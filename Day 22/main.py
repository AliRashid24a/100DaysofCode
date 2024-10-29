from turtle import Screen
from player import Player
from car import Car
from scoreboard import Scoreboard
import time as t
import random as rd

screen = Screen()
screen.setup(600,600)
screen.bgcolor('black')
screen.tracer(0)

player = Player()
scoreboard = Scoreboard()
screen.listen()
screen.onkeypress(player.move_forward,"Up")
global cars
cars = []
def generate_obstacles(num):
    global cars
    ypos = -200
    rangepos = 560 // num
    for i in range(num):
        acar = Car(rd.randint(20,1000),rd.randint(ypos,ypos + rangepos))
        cars.append(acar)
        ypos += 50
    return cars

cars = generate_obstacles(20)
car_speed = 10

GameOn = True
while GameOn:
    screen.update()
    t.sleep(0.1)

    for i in range(len(cars)-1):
        cars[i].move_forward(car_speed)
        if cars[i].xcor() < -280:
            cars[i].reset_position()
        if cars[i].distance(player) < 20:
            scoreboard.game_over()
            GameOn = False

    # player makes it to the end
    if player.ycor() > 280:
        player.reset_position()
        new_cars = generate_obstacles(3)
        cars.append(new_cars)
        car_speed *= 1.1 + (scoreboard.level / 5)
        scoreboard.update_level()

screen.exitonclick()
    



