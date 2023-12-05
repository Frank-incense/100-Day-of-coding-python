# Use constant for death at 90
DEATH = 90
# User inputs their age
age = input("Age\n")

# Calculate weeks
weeks = (DEATH - int(age)) * 52

# Display to the user
print(f"You have {weeks} weeks left.")