import pandas as pd
from turtle import Turtle, Screen

writer = Turtle()

def write_guess(state,x,y):
    writer.penup()
    writer.hideturtle()
    writer.goto(x,y)
    writer.write(f'{state}')

# get data
df = pd.read_csv('Day 24\\US Census Game\\50_states.csv')
states = df['state'].to_list()
image = 'Day 24\\US Census Game\\blank_states_img.gif'

screen = Screen()
screen.bgpic(image)
score = 0
isGameOn = True
guessed_states = []
while isGameOn:
    user_guess = screen.textinput(f'{score}/{len(states)} States' ,'Enter state here: ')
    if user_guess in states:
        guessed_states.append(user_guess)
        """
        state_df = df[df['state'] == user_guess]
        state = state_df['state'].to_list()[0]
        x = int(state_df['x'].to_list()[0])
        y = int(state_df['y'].to_list()[0])
        """
        score += 1
        state_df = df[df.state == user_guess]
        write_guess(state_df.state.item(),state_df.x.item(),state_df.y.item())
    elif user_guess == 'stop':
        missing_states = [state for state in states if state not in guessed_states]
        states_to_learn = pd.DataFrame(missing_states)
        states_to_learn.to_csv('Day 24\\US Census Game\\states_to_learn.csv')
        isGameOn = False
    elif score == 50:
        print('You win!')
        isGameOn = False

