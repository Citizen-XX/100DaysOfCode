from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
# print(menu.get_items())
latte = menu.find_drink("latte")

# menu_item = MenuItem()
# print(menu_item)

# money_machine = MoneyMachine()
# money_machine.report()
# print(money_machine.process_coins())
# money_machine.report()
coffee_maker = CoffeeMaker()
coffee_maker.report()
print(coffee_maker.is_resource_sufficient(latte))