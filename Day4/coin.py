import random

coin = random.randint(1,2)
    
match coin:
    case 1:
        print("Heads") 
    case 2:
        print("Tails")