from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
machine = CoffeeMaker()
cash = MoneyMachine()
off = False

while not off:
    choice = input(f"What would you like? ({menu.get_items()}): ")
    if choice == 'off':
        off = True
    elif choice == 'report':
        machine.report()
        cash.report()
    else:
        coffee = menu.find_drink(choice)
        if machine.is_resource_sufficient(coffee):
            if cash.make_payment(coffee.cost):
                machine.make_coffee(coffee)