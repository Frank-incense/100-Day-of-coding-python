# Let user input their height
height = input("Height:\n")

# Let user input their weight
weight = input("Weight:\n")

# Calculate the BMI for the user bmi= weight/height**
height = int(height) / 100

bmi = int(weight) // height**2

if bmi < 18.5:
    print(f"Your BMI is {bmi: .1f}, you are underweight.")
elif bmi < 25:
    print(f"Your BMI is {bmi: .1f}, you have normal weight.")
elif bmi < 30: 
    print(f"Your BMI is {bmi: .1f}, you are slightly overweight.")
elif bmi < 35:
    print(f"Your BMI is {bmi: .1f}, you are obese.")
else:
    print(f"Your BMI is {bmi: .1f}, you are clinically obese.")