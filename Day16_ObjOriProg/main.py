from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

keep_going = True
menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
coffee_items = menu.get_items()[:-1]

def payment(cost):
    if money_machine.make_payment(cost):
        coffee_maker.make_coffee(drink)
        choice = input("Would you like another drink?: (Y/N) ").lower()
        if choice != "y":
            return False
        else:
            return True

while keep_going:
    order = input(f"What would you like? ({coffee_items}): ")
    if order in coffee_items:
        if order == "latte":
            drink = menu.find_drink("latte")
            if coffee_maker.is_resource_sufficient(drink):
                cost = menu.menu[0].cost
                keep_going = payment(cost)
        elif order == "espresso":
            drink = menu.find_drink("espresso")
            if coffee_maker.is_resource_sufficient(drink):
                cost = menu.menu[1].cost
                keep_going = payment(cost)
        elif order == "cappuccino":
            drink = menu.find_drink("cappuccino")
            if coffee_maker.is_resource_sufficient(drink):
                cost = menu.menu[2].cost
                keep_going = payment(cost) 
    elif order == "report":
        print(money_machine.report())
        coffee_maker.report()
        choice = input("Would you like to select another option?: (Y/N) ")
        if choice != "y":
            keep_going = False
    elif order == "off":
        print("Turning Off the machine...")
        keep_going = False
    else:
        print("The drink was not chosen correctly, try again...")
