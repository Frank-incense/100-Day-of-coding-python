def is_leap(year):
    """
    Determines whether its a leap year meaning 29 days in Fubruary.
    """
    test = year % 4
    if test == 0:
       
        # Second check
        check = year % 100
        if check == 0:

            # Third check
            confirm = year % 400
            if confirm == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

def day_in_month(year, month):
    month_days = [31,28,31,30,31,31,30,31,30,31,30,31]
    if is_leap(year) and month == 2:
        return month_days[month-1] + 1
    else:
        return month_days[month-1]


year = int(input())
month = int(input())
days = day_in_month(year, month)
print(days)