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

# TODO: 4 Check resources are sufficient
def check(coffee):
    drink = MENU[coffee]["ingredients"]
    for ing in drink:
        if drink[ing] > resources[ing]:
            return f"Sorry there is not enough {ing}"
    return True

# TODO: 5 Process coins
# penny = 0.01
# dime = 0.1
# quarter = 0.25
# nickel = 0.05
def process_coins(coffee):
    quarter = int(input("How many quarters?: "))
    nickel = int(input("How many nickels?: "))
    dime = int(input("How many dimes?: "))
    penny = int(input("How many pennys?: "))

    total = (quarter * 0.25) + (dime * 0.1) + (nickel * 0.05) + (penny * 0.01)
    if total > MENU[coffee]["cost"]:
        total = total - MENU[coffee]["cost"]
        return total
    
    return -1

def transaction():
    if "money" not in resources:
        print(resources)