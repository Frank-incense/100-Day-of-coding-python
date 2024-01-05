import random

names_string = input("Input your names:\n")
names = names_string.split(", ")
number = len(names)
i = random.randint(0, number)

print(f"{names[i]} is going to buy the meal today!") 