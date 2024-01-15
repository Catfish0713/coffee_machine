from typing import Dict

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

resources: dict[str, int] = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}



resources["money"] = 0
def check_sufficiency(order):
    keys = MENU[order]["ingredients"].keys()
    lack = 0
    for i in keys:
        if MENU[order]["ingredients"][i] > resources[i]:
            lack += 1
            print(f'Sorry there is not enough {i}.')
    if lack == 0:
        return "sufficient"

def is_deal(order):
    if check_sufficiency(order) == "sufficient":
        quarter = int(input("Please insert coins.\nhow many quarters?:"))
        dime = int(input("how many dimes?:"))
        nickle = int(input("how many nickles?:"))
        penny = int(input("how many pennies?:"))
        total = 0.25 * quarter + 0.1 * dime + 0.05 * nickle + 0.01 * penny
        if total >= MENU[order]["cost"]:
            change = round(total - MENU[order]["cost"],2)
            print(f"Here is ${change} in change.")
            print(f"Here is your {order} ☕️. Enjoy!")
            return "deal_made"
        else:
            print("Sorry that's not enough money. Money refunded.")



end_sale = False
while not end_sale:
    order = input('What would you like? (espresso/latte/cappuccino):')

    if order == "off":
        end_sale = True
    elif order == "report":
        for key, value in resources.items():
            print(key, ":", value)
    else:
        check = check_sufficiency(order)
        print(check)
        deal = is_deal(order)
        print(deal)
        if deal == "deal_made":
            keys = MENU[order]["ingredients"].keys()
            for i in keys:
                resources[i] -= MENU[order]["ingredients"][i]
            resources["money"] += MENU[order]["cost"]

