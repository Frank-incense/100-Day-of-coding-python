import random
from art import logo, stages
from hangman_words import word_list

print(logo)
lives = len(stages) - 1


while lives > -1:
    chosen_word = random.choice(word_list) 
    guesses = []
    endOfGame = False 

    for letter in chosen_word:
        guesses.append('_')
    print(guesses)

    while not endOfGame:
        
        guess = input("Guess a character:\n").lower()
        length = len(guesses)

        if guess in guesses:
            print(f"You have already pressed {guess}")

        for i in range(length):
            
            if guess == chosen_word[i]:
                guesses[i] = guess
            
        print(guesses)
        if guess not in chosen_word:
            print(stages[lives])
            lives -= 1 
            if lives < 0:
                endOfGame = True
                print(f"You lose. the word was {chosen_word}")

        # Win condition.
        if '_' not in guesses:
            endOfGame = True
            print("You win")
        
