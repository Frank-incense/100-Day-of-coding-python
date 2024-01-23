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

print(logo )

# Dealer deals the set of cards.
player = []
dealer = []

for i in range(2):
        player.append(helper.deal(cards))
        dealer.append(helper.deal(cards))

# The olayer can see one of the dealers Cards
print(f"Your cards are {player[1]} and {player[0]} the dealer has {dealer[0]}")

# The player gets to the the count for the visible Cards
print(f"Your total is {helper.game(player)} the dealer has {dealer[0]}")

while not endOfGame:
    choice = input("Will you 'hit' or 'stand': ").lower()
    if choice == "hit":
        player.append(helper.deal(cards))

        print(f"Your cards are {player} and total is {helper.game(player)}")
        print(f"Your cards are {dealer} and total is {helper.game(dealer)}")

        if helper.game(player) > 21:
            endOfGame = True
            print("YOU LOSE") 
        
    else:
        while helper.game(dealer) < helper.game(player) and helper.game(dealer) < 21:
            if helper.game(dealer) < 17:
                dealer.append(cards)
                print(f"Your cards are {player} and total is {helper.game(player)}")
                print(f"Your cards are {dealer} and total is {helper.game(dealer)}")
                
            elif helper.game(player) > helper.game(dealer):
                print("YOU WIN")
                endOfGame = True
                break

            elif helper.game(player) == helper.game(dealer):
                print("YOU TIE")
                endOfGame = True
                break