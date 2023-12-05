# 100-Day-of-coding-python
My journey of learning and revisiting topics about coding.

## Day one
On the first day, the main task was to create a Band Name Generator for a band that is unable to come up with the a name. The sample provided worked as stated below:
- The program asked The city the user grew in.
- The program as well asked about the user's pet's name.

From that the program gave a sample name for the user.

### Lessons Learnt.

I learnt about the print function. The print function takes input and displays it to the user. The princt function take input of certain input like **strings**. Strings are basically a collection of characters. I got some insight into syntax highlighting on code editors.
- Print function.
- Input function.
- Strings.
- Variable.
- Naming.

## Day 2

On the second day we went through the following:
- Primitive Data types.
  - Subscripting - picking specific characters from a string using index i.e. [0] e.g. "Hello"[0] = H
  - Integer e.g. 1,2,3,4
  - Float .e.g. 1.2,2.3,2.4
  - Boolean e.g. True, False
- Type checking.
- Type conversion - Changing the type cast of a variable for your desired output. 
 
### Coding test
#### Add the numbers in a 2 digit input
```
# user input
two_digit_number = input()

# Change the type 
a = int(two_digit_number[0])
b = int(two_digit_number[1])

# Print the sum 
print(a+b)
```
#### Coding a BMI calculalator
 
The test to create a bmi calcalator was next. This required the users to input their height and weight. The calculator then used the formula **BMI = Weight/Height\*\*2** in metric measurements.
 ```
# Let user input their height
height = input("Height:\n")

# Let user input their weight
weight = input("Weight:\n")

# Calculate the BMI for the user bmi= weight/height**
height = int(height) / 100

bmi = int(weight) // height**2

print(f"Your BMI is : {int(round(bmi, 0))}")
 ```

#### Weeks left

This program takes the users age as input. The program assumes death comes at 90. Using that the program outputs the remaining weeks a user has.
```
# Use constant for death at 90
DEATH = 90
# User inputs their age
age = input("Age\n")

# Calculate weeks
weeks = (DEATH - int(age)) * 52

# Display to the user
print(f"You have {weeks} weeks left.")
```

#### Tip calculator.

The program takes the users bill. The program then inquires on what amount of tip the user is willing to give. The program then asks how many people are there for the split. Then the program calculates the total to be paid and the split for everyone to pay.

```
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
```