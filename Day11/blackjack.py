############### Blackjack Project #####################

#Difficulty Normal 😎: Use all Hints below to complete the project.
#Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
#Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
#Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.

##################### Hints #####################

#Hint 1: Go to this website and try out the Blackjack game: 
#   https://games.washingtonpost.com/games/blackjack/
#Then try out the completed Blackjack project here: 
#   http://blackjack-final.appbrewery.repl.run

# Steps to play
from art import logo
import helper
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
endOfGame = False

# Dealer deals the set of cards.
player = []
dealer = []

for i in range(2):
        player.append(helper.deal(cards))
        dealer.append(helper.deal(cards))

def play():

    while not endOfGame:
        # The olayer can see one of the dealers Cards
        print(f"Your cards are {player[1]} and {player[0]} the dealer has {dealer[0]}")

        # The player gets to the the count for the visible Cards
        print(f"Your total is {player[0] + player[1]} the dealer has {dealer[0]}")

        # The player gets the choice of hit or stand.
        choice = input("Will you 'hit' or 'stand': ").lower()

        # Hit grants the player a new card 
        # Stand is called when the player thinks they have won
        if choice == "hit":
        #   player loses if card total is greaater than 21
            if helper.game(player) > 21:
                endOfGame = True
                return "Bust"
            else:
                player.append(helper.deal(cards))

        elif choice == "stand": 
        #   DEALER GETS ANOTHER CARD IF TOTAL LESS THAN 15
            if helper.game(dealer) < 15:
                dealer.append(helper.deal(cards))
                if helper.game(dealer) > 21:
                    endOfGame = True
                    return "Player Wins!"
                     
        #   Player loses if their count is less than dealers 
        #   Dealer loses if their count is less than players
        #    