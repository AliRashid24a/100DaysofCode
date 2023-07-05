#create a hangman game

import random

def game_start():
    from hangman_art import logo
    print(logo)
    with open("Day 7/listofwords.txt", "r") as f:
        wordbank = f.read().splitlines()
    temp = random.randint(0,len(wordbank)-1)
    random_word = wordbank[temp]
    game_loop(random_word)

def game_loop(word):
    game_fin = False
    lives = 6
    letter_count = len(word)
    word_display = ["_"] * len(word)
    while game_fin is False:
        if lives == 0:
            print(f"ur ded the word was {word}")
            break
        if letter_count == 0:
            print("You win!")
            break
        guess = str(input("Guess a letter!\n"))
        for i in range((len(word))):
            if word[i] == guess.lower():
                if word_display[i] == guess:
                    print(f"You have already guessed {guess}, try another letter.")
                else:
                    word_display[i] = guess
                    letter_count += -1
                    print(f"You guessed {guess}, that's in the word!")
        if guess.lower() in word:
            pass
        else:
            lives += -1
            print(f"You guessed {guess}, that's not in the word. You lose a life. You have {lives} lives left")
        print(word_display)
        from hangman_art import stages
        print(stages[lives])

game_start()