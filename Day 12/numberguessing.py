import random as rd

class Game:
    def __init__(self) -> None:
        self.guess_number = -1
        self.difficulty = ""
        self.numAttempts = 0
    
    def set_difficulty(self,difficulty):
        self.difficulty = difficulty
        if self.difficulty.lower() == 'easy':
            self.numAttempts = 10
        else:
            self.numAttempts = 5

    def set_guessnumber(self, guess):
        self.guess_number = guess

    def check_guess(self, guess):
        self.guesses.append(guess)
        self.numAttempts += -1
        if guess == self.guess_number:
            print(f'Congratulations, {self.guess_number} was right!')
            return True
        elif guess > self.guess_number:
            print('Too high.')
        else:
            print('Too low.')
        return False
    
    def play_again(self):
        again = str(input("Would you like to play again. Type 'Yes' or 'No': " ))
        if again.lower() in ['yes', 'y']:
            self.game_loop()
        else:
            print("Thanks for playing! I love you 😀😀😀")

    def game_loop(self):
        guesses = []
        isGuess = False
        self.set_guessnumber(rd.randint(1,100))
        print("Weclome to the Number Guessing Game!")
        dif = str(input("Choose a difficulty. Type 'easy' or 'hard': "))
        self.set_difficulty(dif)
        while self.numAttempts != 0 and isGuess == False:
            print(f'You have {self.numAttempts} attempts to guess the number')
            if len(guesses) != 0:
                print(f'These are your guesses {guesses}')
            guess = int(input("Make a guess: "))
            isGuess = self.check_guess(guess)
        if self.numAttempts == 0 and isGuess == False:
            print(f'The correct number was {self.guess_number}!')
        self.play_again()

NumberGuessing = Game()
NumberGuessing.game_loop()



