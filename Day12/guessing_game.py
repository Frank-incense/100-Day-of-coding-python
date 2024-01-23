import helper

print("Welcome to the Number Guessing Game!")
print("I'm thinking od a number between 1 and 100.")
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
attempt = 0
number =  helper.guess()

if difficulty == 'easy':
    attempt = 10
    while attempt > 0:
        print(f"You have {attempt} attempts remaining to guess the number.")
        player = int(input("Make a guess: "))
        if not helper.check(player, number):
            attempt -= 1
            if player > number:
                print("Too high.")
            else:
                print("Too low.")
        else:
            print(f"You got it! Thw answer was {number}")
            break

else:
    attempt = 5
    while attempt > 0:
        print(f"You have {attempt} attempts remaining to guess the number.")
        player = int(input("Make a guess: "))
        if not helper.check(player, number):
            attempt -= 1
            if player > number:
                print("Too high.")
            else:
                print("Too low.")
        else:
            print(f"You got it! The answer was {number}")
            break