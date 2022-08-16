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




def report():
    water = resources["water"]
    print(f"Water: {water} ml")
    milk = resources["milk"]
    print(f"Milk: {milk} ml")
    coffee = resources["coffee"]
    print(f"Coffee: {coffee} ml")
    money = "{:.2f}".format(resources["money"])
    print(f"Money: ${money}")




def check_resources(water_needed, milk_needed, coffee_needed):
    water = resources["water"]
    milk = resources["milk"]
    coffee = resources["coffee"]
    if water_needed > water:
        print("Sorry there is not enough water.")
        transaction_start()
    if milk_needed > milk:
        print("Sorry there is not enough milk.")
        transaction_start()
    if coffee_needed > coffee:
        print("Sorry there is not enough coffee.")
        transaction_start()


def water_required(coffeeType):
    water_needed = int(MENU[str(coffeeType)]['ingredients']['water'])
    return water_needed


def milk_required(coffeeType):
    milk_needed = int(MENU[str(coffeeType)]['ingredients']['milk'])
    return milk_needed


def coffee_required(coffeeType):
    coffee_needed = int(MENU[str(coffeeType)]['ingredients']['coffee'])
    return coffee_needed


def deduct_resources(water_needed, milk_needed, coffee_needed):
    water_remaining = resources['water'] - water_needed
    resources['water'] = water_remaining
    milk_remaining = resources['milk'] - milk_needed
    resources['milk'] = milk_remaining
    coffee_remaining = resources['coffee'] - coffee_needed
    resources['coffee'] = coffee_remaining


def coin_process(q,d,n,p):
    total = q + d + n + p
    return total


def transaction_start():
    machine_on = True
    while machine_on:

        user_input = input("What would you like? (espresso/latte/cappuccino): ").lower()


        if user_input == "off":
            print("Goodbye.")
            machine_on = False

        if user_input == "report":
            report()

        if user_input == "latte" or user_input == "cappuccino" or user_input == "espresso":
            cost = MENU[user_input]['cost']
            formatted_cost = "{:.2f}".format(cost)
            print(f"A {user_input} costs ${formatted_cost} ")
            water_needed = water_required(coffeeType=user_input)
            if user_input == "espresso":
                MENU['espresso']['ingredients']['milk'] = 0
            milk_needed = milk_required(coffeeType=user_input)
            coffee_needed = coffee_required(coffeeType=user_input)
            check_resources(water_needed, milk_needed, coffee_needed)
            deduct_resources(water_needed, milk_needed, coffee_needed)
            q = int(input("How many quarters do you have? ")) * 0.25
            d = int(input("How many dimes do you have? ")) * 0.10
            n = int(input("How many nickels do you have? ")) * 0.05
            p = int(input("How many pennies do you have? ")) * 0.01
            total = coin_process(q,d,n,p)
            if total >= MENU[user_input]['cost']:
                change = total - MENU[user_input]['cost']
                formatted_change = "{:.2f}".format(change)
                print(f"Here is ${formatted_change} in change.")
                resources['money'] += MENU[user_input]['cost']
                print(f"Here is your {user_input}. Enjoy!")
            else:
                print("Sorry that's not enough money. Money refunded. ")


money = 0
resources["money"] = money

transaction_start()


