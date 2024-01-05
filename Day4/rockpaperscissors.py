import random
rock = ('''
                _    
               | |   
 _ __ ___   ___| | __
| '__/ _ \ / __| |/ /
| | | (_) | (__|   < 
|_|  \___/ \___|_|\_\\
''')
paper = (
'''
 _ __   __ _ _ __   ___ _ __ 
| '_ \ / _` | '_ \ / _ \ '__|
| |_) | (_| | |_) |  __/ |   
| .__/ \__,_| .__/ \___|_|   
| |         | |              
|_|         |_|              
'''
)
scissors = (
'''
          _                        
         (_)                       
 ___  ___ _ ___ ___  ___  _ __ ___ 3
/ __|/ __| / __/ __|/ _ \| '__/ __|
\__ \ (__| \__ \__ \ (_) | |  \__ \\
|___/\___|_|___/___/\___/|_|  |___/
'''
)
choice = [rock, paper, scissors]

play = int(input("What do you chose type 0 for Rock, 1 for Paper, 2 for Scissors!!\n"))

computer = choice[random.randint(0,2)]
player = choice[play]

print(f"{player}\nComputer chose:\n{computer}")
if computer == player:
    print('Its a tie')
elif computer == rock and player == scissors:
    print('You lose')
elif computer == scissors and player == paper:
    print('You lose')
elif computer == paper and player == scissors:
    print('You win')
elif computer == rock and player == paper:
    print('You win')