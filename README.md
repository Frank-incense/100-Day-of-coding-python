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
## Day 3

On the third day of the practice, we learnt a couple of  things listed below:
 - Conditionals  - if  and else statements.
   - Comparison operators : These are >, <, >=, <=, ==, != the operators for the comparing.
   - Nested if statements : Conditional statements within conditional statements. 
   - Multiple condition statements: Here there are multiple conditional statements. e.g. if, elif, elif.
   - Multiple if statements.
 - Logical operators.

### Coding test.
#### Odd or Even.

The program here is to workout whether if a number given by the user is either odd or even. To determine this the number given by the user is divided by 2 to obtain a modulo operator. If the result is an integer then the number is even. If the result is a float then the number is odd.

```
# Get input from user
number = int(input("Please input the number?\n"))

# Modulo checks
check = number % 2

# Conditional checks
if  check == 0:
    print("This is an even number.")
else:
    print("This is an odd number.")
```
#### BMI calculator upgrade.

With the upgrader the program takes the result of the calculation. Thie result is then weighd on a scale of what status th users index would represent.
 ```
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
 ```

 #### Leap year.

This exercise was a dificult one as expressed by the instructor Angela Yu. The main task was to take input from a user. i.e. years.

```
# Take in users input 
year = int(input("Enter a year: "))

test = year % 4
if test == 0:
    check = year % 100
    if check == 0:
        confirm = year % 400
        if confirm == 0:
            print(f"{year} is a leap year")
        else:
            print(f"{year} is not a leap year")
    else:
        print(f"{year} is not a leap year")
else:

    print(f"{year} is not a leap year")
```

#### Python Pizza
The task for this problem was to create a program that takes users orders and then return the amount for the user to pay.
```
print("Thank you for choosing Pizza Python Deliveries")
size = input("What size pizza do you want? S, M or L\n")
extra_pepperoni = input("Do you want pepperoni? Y or N\n")
extra_cheese = input("Do you want extra cheese? Y or N\n")
small = "Ss"
medium = "Mm"
bill = 0
# S = 15, M = 20, L = 25
if size in small:
    print("For a small pizza pay $15")
    bill = 15
elif size in medium:
    print("For a medium pizza pay $20")
    bill = 20
else:
    print("For a large pizza pay $20")
    bill = 25

# pepperoni = +2, cheese +1
if extra_pepperoni == "Y":
    bill += 2
if extra_cheese == "Y":
    bill += 1

print(f"Your bill is ${bill}")
```
#### Love calculator.

This is a love calculator. The program tests the compatibility between 2 people. The program takes input by taking the names of both users. Take the names and check for the number of the letters occurence in the word **true**. This is done with regards to letters in the word **love** as well. The totals of both are then concatenated to give a response. The response is then graded on a percentage base.
