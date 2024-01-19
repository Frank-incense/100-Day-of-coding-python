import os
from art import logo

print(logo)
players = []

print("Welcome to the secret auction program.")

def highest_bidder(plays):
    max = 0
    highest = {}
    for player in plays:
        if player["bid"] > max:
            max = player["bid"]
            highest = player
        print(player)

    print(f"The winner is {highest['name']} with a bid of ${highest['bid']}.")

end = False
while not end:
    name = input("What is your name?: ")
    bid = int(input("What's your bid?: $")) 
    game = input("Are there any other bidders? Type 'yes' or 'no'.\n")
    players.append({"name": name, "bid": bid})
    os.system('clear')
    if game == 'no':
        end = True

highest_bidder(plays=players)