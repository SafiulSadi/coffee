# check resources sufficient to make drink order
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
# print(resources["water"])
# prompt the user by asking "What would you like? (espresso/latte/cappuccino): "
# state variables
run = True
resources["money"] = 0
MENU["espresso"]["ingredients"]["milk"] = 0

def process_coin():
    q = int(input("input amount of quarter: "))
    d = int(input("input amount of dime: "))
    n = int(input("input amount of nickel: "))
    p = int(input("input amount of penny: "))
    total = q * 0.25 + d * 0.10 + n * 0.05 + p * 0.01
    return total

    #

def add_money(cost):
    resources["money"] += cost
    print(resources["money"])

def check_resources(order):
    # add money
    # This deals with the coffee check
    if "coffee" in order and resources["coffee"] >= order["coffee"]:
        print(f'the amount of coffee needed : {order["coffee"]}')
        resources["coffee"] = resources["coffee"] - order["coffee"]
        print(f"coffee after {resources['coffee']}")
    else:
        print(f"Sorry there is not enough coffee.")
        return False
    # Water check
    if "water" in order and resources["water"] >= order["water"]:
        print(f'the amount of water needed : {order["water"]}')
        resources["water"] = resources["water"] - order["water"]
        print(f"water after {resources['water']}")
    else:
        print(f"Sorry there is not enough water.")
        return False
    # Water check
    if "milk" in order and resources["milk"] >= order["milk"]:
        print(f'the amount of milk needed : {order["milk"]}')
        resources["milk"] = resources["milk"] - order["milk"]
        print(f"milk after {resources['milk']}")

    else:
        print(f"Sorry there is not enough milk..")
        print(f'{order["milk"]} this is important')
        return False
    return True
#  make it repeat.
while run == True:
    # print report
    print(f"Water: {resources['water']}")
    print(f"Milk: {resources['milk']}")
    print(f"Coffee: {resources['coffee']}")
    print(f"Money: {resources['money']}")

    user_order = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if user_order == "off":
        run = False
    elif user_order == "espresso":
        o = MENU["espresso"]["ingredients"]
        c = MENU["espresso"]["cost"]
        p = process_coin()
        if p >= c:
            if check_resources(o) == True:
                add_money(c)
                print(f"Here is your {user_order} enjoy. You paid {p} and the cost was {c}. The change is {p - c}")
            else:
                print(f"You paid {p}. Not enough resources. Take {p} back ")
        else:
            print(f"Not enough money. Take {p} back ")
    elif user_order == "latte":
        o = MENU["latte"]["ingredients"]
        c = MENU["latte"]["cost"]
        p = process_coin()
        if p >= c:
            if check_resources(o) == True:
                add_money(c)
                print(f"Here is your {user_order} enjoy. You paid {p} and the cost was {c}. The change is {p - c}")
            else:
                print(f"You paid {p}. Not enough resources. Take {p} back ")
        else:
            print(f"Not enough money. Take {p} back ")

    elif user_order == "cappuccino":
        o = MENU["cappuccino"]["ingredients"]
        c = MENU["cappuccino"]["cost"]
        p = process_coin()
        if p >= c:
            if check_resources(o) == True:
                add_money(c)
                print(f"Here is your {user_order} enjoy. You paid {p} and the cost was {c}. The change is {p - c}")
            else:
                print(f"You paid {p}. Not enough resources. Take {p} back ")
        else:
            print(f"Not enough money. Take {p} back ")
    else:
        print("Not a valid input")










