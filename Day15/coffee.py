from art import logo
from helper import MENU, resources, check, process_coins, transaction
import os

print(logo)
# TODO: 1 Prompt user for drink
coffee = input("What would you like? (espresso/latte/cappuccino) ").lower()
# TODO: 2 Turn off the machine
if coffee == 'off':
    off = True
# TODO: 3 Print report
if coffee == 'report':
    resource = list(resources.keys())
    print(f"{resource[0]}: {resources[resource[0]]}ml")
    print(f"{resource[1]}: {resources[resource[1]]}ml")
    print(f"{resource[2]}: {resources[resource[2]]}g")
     
    if len(resource) == 4:
        print(f"{resource[0]}: ${resources[resource[3]]}")   
        
# TODO: 6 Check transaction success
coins = process_coins(coffee=coffee)
if coins == -1:
    print("Sorry thats not enough money. Money refunded.")
else:
    if check(coffee=coffee):
        print(f"Here is ${coins} in change.")
        print(f"Here is your {coffee} Enjoy!")
        transaction()
    else:
        check(coffee=coffee)
        
# TODO: 7 Make coffee
