MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

def enough_resource(coffee):
    '''Return a string of either the ingredient or just yes'''
    ingredients = MENU[coffee]['ingredients']
    for ingredient in ingredients:
        if ingredients[ingredient] > resources[ingredient]:
            return ingredient
        else:
            return 'yes'

def get_coins():
    '''Returns the total money received form the client'''
    quarter = int(input("How many quarters?: "))
    dime = int(input("How many dimes?: "))
    nickel = int(input("How many nickels?: "))
    penny = int(input("How many pennies?: "))
    
    # machine processes the total coins
    coins = (quarter * .25) + (dime * 0.1) + (nickel * 0.05) + (penny * 0.01)
    return coins

def process(money, coffee):
    '''Returns the amount of change owed'''
    change = money - MENU[coffee]['cost']
    if 'money' not in resources:
        resources['money'] = MENU[coffee]['cost']
    else:
        resources['money'] += MENU[coffee]['cost']

    return change

def make_coffee(coffee):
    '''Returns a string after altering the resources'''
    for resource in resources:
        if resource in MENU[coffee]['ingredients']:
            resources[resource] = resources[resource] - MENU[coffee]['ingredients'][resource]

    return f"Here is your {coffee}. Enjoy!"