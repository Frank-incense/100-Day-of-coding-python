from art import vs, logo
from gameData import data
import random, os

# Get random insta details
def get_ista():
    return random.choice(data)

# Format a sentence
def format(option):
    name = option["name"]
    country = option["country"]
    description = option["description"]
    return f"{name}, a {description}, from {country}"
# Check if response is correct
def check(account_a, account_b):
    if account_a["follower_count"] > account_b["follower_count"]:
        return True
    else:
        False

# Initialise the variables
score = 0
end = False
option_a = get_ista()
option_b = get_ista()
while option_b == option_a:
    option_b = get_ista()

while not end:
    print(logo)
    print(f"Compare a: {format(option_a)}")
    print(vs)
    print(f"Compare b: {format(option_b)}")

    choice = input("Who has more followers? Type 'A' or 'B': ").upper()

    os.system('clear')
    if choice == "A" and check(option_a, option_b):
        score += 1
        print(f"You're right. Current score is {score}")
        option_b = get_ista()
    elif choice == "B" and check(option_b, option_a):
        score += 1
        print(f"You're right. Current score is {score}")
        option_a = option_b
        option_b = get_ista()
    else:
        end = True
        print(f"The end. Your score is {score}")