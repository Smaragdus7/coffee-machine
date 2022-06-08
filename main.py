from data import resources, MENU


def check_resources(drink):
    if drink != "espresso":
        if MENU[drink]["ingredients"]["water"] > resources["water"]:
            print("Sorry there is not enough water.")
        elif MENU[drink]["ingredients"]["coffee"] > resources["coffee"]:
            print("Sorry there is not enough coffee.")
        elif MENU[drink]["ingredients"]["milk"] > resources["milk"]:
            print("Sorry there is not enough milk.")
        else:
            return "OK"
    else:
        if MENU[drink]["ingredients"]["water"] > resources["water"]:
            print("Sorry there is not enough water.")
        elif MENU[drink]["ingredients"]["coffee"] > resources["coffee"]:
            print("Sorry there is not enough coffee.")
        else:
            return "OK"


def check_money(q, d, n, p, drink):
    money_inserted = (q * 0.25) + (d * 0.10) + (n * 0.05) + (p * 0.01)
    if MENU[drink]["cost"] > money_inserted:
        print("Sorry that's not enough money. Money refunded.")
        return "REF"
    else:
        resources["money"] += MENU[drink]["cost"]
        change = money_inserted - MENU[drink]["cost"]
        return round(change, 2)


def make_coffee(drink):
    if drink != "espresso":
        resources["water"] -= MENU[drink]["ingredients"]["water"]
        resources["milk"] -= MENU[drink]["ingredients"]["milk"]
        resources["coffee"] -= MENU[drink]["ingredients"]["coffee"]
    else:
        resources["water"] -= MENU[drink]["ingredients"]["water"]
        resources["coffee"] -= MENU[drink]["ingredients"]["coffee"]


resources["money"] = 0

is_off = False
should_end = False

while not is_off and not should_end:
    instruction = input("What would you like? (espresso/latte/cappuccino): ")
    if instruction == "off":
        is_off = True
    elif instruction == "report":
        print(f"Water: {resources['water']}")
        print(f"Milk: {resources['milk']}")
        print(f"Coffee: {resources['coffee']}")
        print(f"Money: {resources['money']}")
    else:
        check_resources(instruction)
        if check_resources(instruction) == "OK":
            print("Please insert coins.")
            quarters = int(input("how many quarters?: "))
            dimes = int(input("how many dimes?: "))
            nickles = int(input("how many nickles?: "))
            pennies = int(input("how many pennies?: "))
            cm = check_money(quarters, dimes, nickles, pennies, instruction)
            if cm != "REF":
                print(f"Here is ${cm} dollars in change.")
                make_coffee(instruction)
                print(f"Here is you {instruction}. Enjoy!")

        else:
            should_end = True
