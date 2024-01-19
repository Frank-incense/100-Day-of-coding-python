import random

def deal(card):
    return random.choice(card)

def game(players):
    total = 0
    for player in players:
        total += player

    return total
