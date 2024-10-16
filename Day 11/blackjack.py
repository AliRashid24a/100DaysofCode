import random as rd

global cards
cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]

def game_loop():
    keep_going = True
    while keep_going:
        computer_cards = [rd.choice(cards)]
        player_cards = []
        player_score = 0

        continue_str = str(input("Do you want to play a game of blackjack? Type 'Y' or 'N' "))
        # if no, break the loop
        if continue_str.upper() in ['N','NO']:
            keep_going = False
        # if yes, continue
        player_cards = rd.choices(cards, k=2)
        player_score = calculate_score(player_cards)
        print(f'Your cards: {player_cards}, current score: {player_score}')
        print(f"Computer's first card: {computer_cards}")

        round_going = True
        while round_going:
            continue_game = str(input("Type 'Y' to get another card, type 'N' to pass: "))
            # if N
            if continue_game.upper() in ['N','NO']:
                # stop drawing, compute pc turn
                computer_final = computer_turn(computer_cards)
                computer_score = calculate_score(computer_cards)
                print(f'Your final cards: {player_cards}, final score: {player_score}')
                print(f"Computer's final cards: {computer_final}, final score: {computer_score}")
                if computer_score > 21:
                    print("Bot went over. You won! Yippie!")
                elif computer_score > player_score:
                    print("You lost to a bot xdd.")
                else:
                    print("You won! Poggers")
                round_going = False
            # if Yes
            else:
                player_cards.append(rd.choice(cards))
                player_score = calculate_score(player_cards)

                if player_score > 21:
                    # player loses, compute pc turn
                    print(f'Your cards: {player_cards}, current score: {player_score}')
                    print(f"Computer's final card: {computer_cards}")
                    print("You went over. You lose. Smodge")
                    round_going = False
                else:
                    print(f'Your cards: {player_cards}, current score: {player_score}')
                    print(f"Computer's cards: {computer_cards}")

def calculate_score(cards_list: list[int]) -> int:
    result = 0
    for card in cards_list:
        if card == 11:
            # if 11 will make you go over, it counts as a one
            if result + card > 21:
                result += 1
            # else it counts as an 11
            else:
                result += 11
        else:
            result += card
    return result

def computer_turn(computer_cards: list[int]) -> list[int]:
    while calculate_score(computer_cards) < 17:
        computer_cards.append(rd.choice(cards))
    return computer_cards


game_loop()



