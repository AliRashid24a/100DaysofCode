from turtle import Screen, Turtle
import random as rd
from race_brain import ready_race

screen = Screen()
screen.setup(500,400)

# setup race
turtles = ready_race(6)

# get user choice
race_on = False
user_bet = screen.textinput('Make your bet','Which turtle will win the race? Enter a color: ')

if user_bet:
    race_on = True

while race_on:
    for turtle in turtles:
        if turtle.xcor() > 230:
            race_on = False
            winner = turtle.pencolor()
            if winner == user_bet:
                print(f"You've won! The {winner} turtle is the fastest!")
        random_distance = rd.randint(0,10)
        turtle.forward(random_distance)

screen.exitonclick()