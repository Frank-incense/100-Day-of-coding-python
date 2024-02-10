from art import logo
from helper import MENU, resources, enough_resource, get_coins, process, make_coffee
import os

off = False

while not off:
    
    print(logo)
    # The machine asks the user for a drink from 3 choices
    choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
    os.system('cls')
    # if user selects report, the machine prints a resources report
    if choice == 'report':
        for resource in resources:
            if resource == 'coffee':
                print(f"{resource.capitalize()}: {resources[resource]}g")
            elif resource == 'money':
                print(f"{resource.capitalize()}: ${resources[resource]}")
            else:
                print(f"{resource.capitalize()}: {resources[resource]}ml")

    # if user selects off, the machine stops
    elif choice == 'off':
        off = True

    # the machine checks if there are enough resources for the drink
    else:
        enough = enough_resource(coffee=choice)
        if enough != 'yes':
            print(f"Sorry there isn't enough {enough}.") 

        # Resources are enough continue
        else:

            # The machine takes the users coins
            coins = round(get_coins(), 2)
            
            if coins < MENU[choice]['cost']:
                print("Sorry that's not enough money. Money refunded")

            else:
                change = process(money=coins, coffee=choice)
                if change > 0:
                    print(f"Here is ${change : .2f} in change.")
                
                print(make_coffee(coffee=choice))

        # other wise the coffee machine goes back to the the start