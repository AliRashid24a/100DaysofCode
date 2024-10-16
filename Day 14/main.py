from art import logo,vs
from game_data import data
from random import randint

class Game():
    def __init__(self):
        self.logo = logo
        self.data = data
        self.score = 0

    def select_random_person(self) -> list[str,str,str,int]:
        random_num = randint(0,len(self.data))
        return [self.data[random_num]["name"], self.data[random_num]["description"], self.data[random_num]["country"], self.data[random_num]["follower_count"]]
    
    def generate_matchup(self,matchup) -> str:
        msg = f"{matchup[0]}, {matchup[1]}, {matchup[2]}"
        return msg
    
    def compare_followers(self,choice,count_A,count_B) -> bool:
        if choice.upper() == 'A':
            if count_A > count_B:
                self.score += 1
                return True
            else:
                return False
        else:
            if count_B > count_A:
                self.score += 1
                return True
            else:
                return False
    
    def game_loop(self):
        print(logo)
        match_a = self.select_random_person()
        match_b = self.select_random_person()
        if match_a[0] == match_b[0]:
            match_b = self.select_random_person()
        print(f"Compare A: {self.generate_matchup(match_a)}")
        print(vs)
        print(f"Compare B: {self.generate_matchup(match_b)}")
        choice = str(input("Who has more followers? Type 'A' or 'B': "))
        isCorrect = self.compare_followers(choice,match_a[3],match_b[3])
        while isCorrect:
            print(f"You're right! Current score: {self.score}.")
            # display the correct match
            if match_a[3] > match_b[3]:
                match_a = match_b
            match_b = self.select_random_person()
            print(f"Compare A: {self.generate_matchup(match_a)}")
            print(vs)
            print(f"Compare B: {self.generate_matchup(match_b)}")
            choice = str(input("Who has more followers? Type 'A' or 'B': "))
            isCorrect = self.compare_followers(choice,match_a[3],match_b[3])
        else:
            print(f"You're wrong 😢😢😭 Your final score is: {self.score}.")
            return

g = Game()
g.game_loop()
