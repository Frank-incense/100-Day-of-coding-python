# Let user input their height
height = input("Height:\n")

# Let user input their weight
weight = input("Weight:\n")

# Calculate the BMI for the user bmi= weight/height**
height = int(height) / 100

bmi = int(weight) // height**2

print(f"Your BMI is : {int(round(bmi, 0))}")

