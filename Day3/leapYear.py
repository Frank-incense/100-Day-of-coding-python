# Take in users input 
year = int(input("Enter a year: "))

# First check of the leap
test = year % 4
if test == 0:
    
    # Second check
    check = year % 100
    if check == 0:

        # Third check
        confirm = year % 400
        if confirm == 0:
            print(f"{year} is a leap year")
        else:
            print(f"{year} is not a leap year")
    else:
        print(f"{year} is a leap year")
else:

    print(f"{year} is not a leap year")