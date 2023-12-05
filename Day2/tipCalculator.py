# Welcome the user
print("Welcome to the tip calculator.")
# Inquire the total bill
bill = input("What was the total bill? $")
# Inquire on the percentage of tip either 10, 12 or 15
tip = input("What percentage tip would you like to give? 10, 12 or 15? ")
# Get the number of people paying
people = input('How many people are spliting th bill? ')

percentage = 1 + int(tip) / 100
split = float(bill) * percentage / int(people)
# Give the split for the bill
print(f'Each person should pay: ${split : .2f}')