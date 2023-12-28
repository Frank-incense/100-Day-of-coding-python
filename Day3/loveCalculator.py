print("The love calculator is calculating your score...")
name1 = input("Enter your name: ").lower()
name2 = input("Enter their name: ").lower()

# Love metrics initialised to 0
true = 0
love = 0

# form one string by combining the strings
name = name1+name2

# Conditional check to add up the love count
true += name.count('t')
true += name.count('r')
true += name.count('u')
true += name.count('e')
love += name.count('l')
love += name.count('o')
love += name.count('v')
love += name.count('e')

answer = str(true)+str(love)
if int(answer) < 10 or int(answer) > 90:
    print(f"Your score is {answer} you are like coke and mentos.")
elif int(answer) > 40 and int(answer) < 50:
    print(f"Your score is {answer} you are alright.")
else:
    print(f"Your score is {answer}.")