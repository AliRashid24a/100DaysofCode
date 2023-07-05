# Make a game in which the player playes rock paper scissors. The opponent will be a simple randomized choice

#put start_game() in while loop and make a counter for each win and loss
import random

class Game():
    def __init__(self,player_score=0, bot_score=0):
        self.player_score = player_score
        self.bot_score = bot_score

    def random_choice(self):
        choices = ["rock", "paper", "scissors"]
        randomint = random.randrange(0, 3)
        choice = choices[randomint]
        return choice

    def game_loop(self, player_choice, score, bot_score):
        player_choice = str(input(f"Rock, Paper, Scissors. Your score is {self.player_score} - {self.bot_score}"))
        bot_choice = self.random_choice()
        print(f"You chose {player_choice.lower()} and your opponent chose {bot_choice}")
        if player_choice.lower() == bot_choice:
            print("It's a tie! Choose again!")
        elif player_choice.lower() == "paper":
            if bot_choice == "rock":
                self.player_score += 1
                print("Congrats! You win!")
            else:
                self.bot_score+= 1
                print("You lost!")
        elif player_choice.lower() == "scissors":
            if bot_choice == "rock":
                self.bot_score += 1
                print("You lose!")
            else:
                self.player_score += 1
                print("Congrats! You win!")
        elif player_choice.lower() == "rock":
            if bot_choice == "scissors":
                self.player_score += 1
                print("Congrats! You win!")
            else:
                self.bot_score += 1
                print("You lose!")

    def game_start(self):
        player_choice = ""
        while player_choice.lower() != "exit":
            self.game_loop(player_choice, self.player_score, self.bot_score)

Game1 = Game()
Game1.game_start()