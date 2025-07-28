#imports
import random


#Helper Functions

#deal() distributes two cards to the dealer and the player
    #Takes an input of bet
    #Distributes Cards to player and dealer
    #returns the total count of points of each side
def deal():
    card = [11,2,3,4,5,6,7,8,9,10,10,10,10]
    card = random.choice(card)
    return card
#hit()
    #ask for another card to add onto your hand

#stand()
    #keep hand and wait for dealer's answer
#calculate_score()
def calculate_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

#compare_hands()
    #compare total hand score of player and dealer
    #return winner
def compare_hands(player_score, dealer_score):
    if player_score == dealer_score:
        return "Draw"
    elif dealer_score == 0:
        return "Lose, Opponent has blackjack"
    elif player_score == 0:
        return "You win with a blackjack"
    elif player_score > 21:
        return "You went over. Bust! You lose!"
    elif dealer_score > 21:
        return "Opponent went over and got busted! You win!"
    elif player_score > dealer_score:
        return "You win"
    else:
        return "You lose"


#Main Game Function
def play_game():
    player_score = -1
    dealer_score = -1
    player_cards = [deal(), deal()]
    dealer_cards = [deal(), deal()]
    is_game_over = False

    while not is_game_over:
        player_score = calculate_score(player_cards)
        dealer_score = calculate_score(dealer_cards)
        print(f"Your cards: {player_cards}, current score: {player_score}")
        print(f"Computer's first card: {dealer_cards[0]}")

        if player_score == 0 or dealer_score == 0 or player_score > 21:
            is_game_over = True
        else:
            user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ")
            if user_should_deal == "y":
                player_cards.append(deal())
            else:
                is_game_over = True

    while dealer_score != 0 and dealer_score < 17:
        dealer_cards.append(deal())
        dealer_score = calculate_score(dealer_cards)

    print(f"\nYour final hand: {player_cards}, final score: {player_score}")
    print(f"Dealer's final hand: {dealer_cards}, final score: {dealer_score}")
    print(compare_hands(player_score, dealer_score))

#Game Entry Call Point

while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
    print("\n" * 20)
    play_game()




