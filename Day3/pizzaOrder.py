print("Thank you for choosing Pizza Python Deliveries")
size = input("What size pizza do you want? S, M or L\n").lower()
extra_pepperoni = input("Do you want pepperoni? Y or N\n").lower()
extra_cheese = input("Do you want extra cheese? Y or N\n").lower()

# User inputs to be checked against
small = ["s", "small"]
medium = ["m", "medium"]
accept = ["y", "yes"]
bill = 0

# S = 15, M = 20, L = 25
if size in small:
    bill += 15
elif size in medium:
    bill += 20
else:
    bill += 25

# pepperoni = +2, cheese +1
if extra_pepperoni in accept:
    bill += 2
if extra_cheese in accept:
    bill += 1

print(f"Your final bill is ${bill}")

