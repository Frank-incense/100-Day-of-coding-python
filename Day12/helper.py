import random

def guess():
    return random.randint(1,100)

def check(play, guess):
    if play != guess:
        return False
    else: 
        return True