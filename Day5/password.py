import random

LETTERS = [
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
    'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
    'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X',
    'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 
    'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 
    'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 
    'w', 'x', 'y', 'z'
]

NUMBERS = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
SYMBOLS = ['!', '#', '$', '%', '&', '(', ')', '+', '*']

print("Welcome to the PyPassword Generator!")
num_letters = int(input("How many letters would you like in your password: \n"))
num_symbols = int(input("How many symbols would you like in your password: \n"))
num_numbers = int(input("How many numbers would you like in your password: \n"))

password = []
nums = 0 
lets = 0
syms = 0
length = num_letters + num_numbers + num_symbols
for i in range(length):
    if lets < num_letters:
        password.append(random.choice(LETTERS))
        lets += 1
    elif nums < num_numbers:
        password.append(str(random.choice(NUMBERS)))
        nums += 1
    else:
        password.append(random.choice(SYMBOLS))
        syms += 1
random.shuffle(password)
password = "".join(password)
print("Your password is: ", password)