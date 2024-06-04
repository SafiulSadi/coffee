# check resources sufficient to make drink order
# MENU = {
#     "espresso": {
#         "ingredients": {
#             "water": 50,
#             "coffee": 18,
#         },
#         "cost": 1.5,
#     },
#     "latte": {
#         "ingredients": {
#             "water": 200,
#             "milk": 150,
#             "coffee": 24,
#         },
#         "cost": 2.5,
#     },
#     "cappuccino": {
#         "ingredients": {
#             "water": 250,
#             "milk": 100,
#             "coffee": 24,
#         },
#         "cost": 3.0,
#     }
# }
#
# resources = {
#     "water": 300,
#     "milk": 200,
#     "coffee": 100,
# }
# print(resources["water"])
# prompt the user by asking "What would you like? (espresso/latte/cappuccino): "
# state variables
# run = True
# resources["money"] = 0
# MENU["espresso"]["ingredients"]["milk"] = 0
#
# def process_coin():
#     q = int(input("input amount of quarter: "))
#     d = int(input("input amount of dime: "))
#     n = int(input("input amount of nickel: "))
#     p = int(input("input amount of penny: "))
#     total = q * 0.25 + d * 0.10 + n * 0.05 + p * 0.01
#     return total
#
#     #
#
# def add_money(cost):
#     resources["money"] += cost
#     print(resources["money"])
#
# def check_resources(order):
#     # add money
#     # This deals with the coffee check
#     if "coffee" in order and resources["coffee"] >= order["coffee"]:
#         print(f'the amount of coffee needed : {order["coffee"]}')
#         resources["coffee"] = resources["coffee"] - order["coffee"]
#         print(f"coffee after {resources['coffee']}")
#     else:
#         print(f"Sorry there is not enough coffee.")
#         return False
#     # Water check
#     if "water" in order and resources["water"] >= order["water"]:
#         print(f'the amount of water needed : {order["water"]}')
#         resources["water"] = resources["water"] - order["water"]
#         print(f"water after {resources['water']}")
#     else:
#         print(f"Sorry there is not enough water.")
#         return False
#     # Water check
#     if "milk" in order and resources["milk"] >= order["milk"]:
#         print(f'the amount of milk needed : {order["milk"]}')
#         resources["milk"] = resources["milk"] - order["milk"]
#         print(f"milk after {resources['milk']}")
#
#     else:
#         print(f"Sorry there is not enough milk..")
#         print(f'{order["milk"]} this is important')
#         return False
#     return True
# #  make it repeat.
# while run == True:
#     # print report
#     print(f"Water: {resources['water']}")
#     print(f"Milk: {resources['milk']}")
#     print(f"Coffee: {resources['coffee']}")
#     print(f"Money: {resources['money']}")

    # user_order = input("What would you like? (espresso/latte/cappuccino): ").lower()
    # if user_order == "off":
    #     run = False
    # elif user_order == "espresso":
    #     o = MENU["espresso"]["ingredients"]
    #     c = MENU["espresso"]["cost"]
    #     p = process_coin()
    #     if p >= c:
    #         if check_resources(o) == True:
    #             add_money(c)
    #             print(f"Here is your {user_order} enjoy. You paid {p} and the cost was {c}. The change is {p - c}")
    #         else:
    #             print(f"You paid {p}. Not enough resources. Take {p} back ")
    #     else:
    #         print(f"Not enough money. Take {p} back ")
    # elif user_order == "latte":
    #     o = MENU["latte"]["ingredients"]
    #     c = MENU["latte"]["cost"]
    #     p = process_coin()
    #     if p >= c:
    #         if check_resources(o) == True:
    #             add_money(c)
    #             print(f"Here is your {user_order} enjoy. You paid {p} and the cost was {c}. The change is {p - c}")
    #         else:
    #             print(f"You paid {p}. Not enough resources. Take {p} back ")
    #     else:
    #         print(f"Not enough money. Take {p} back ")
    #
    # elif user_order == "cappuccino":
    #     o = MENU["cappuccino"]["ingredients"]
    #     c = MENU["cappuccino"]["cost"]
    #     p = process_coin()
    #     if p >= c:
    #         if check_resources(o) == True:
    #             add_money(c)
    #             print(f"Here is your {user_order} enjoy. You paid {p} and the cost was {c}. The change is {p - c}")
    #         else:
    #             print(f"You paid {p}. Not enough resources. Take {p} back ")
    #     else:
    #         print(f"Not enough money. Take {p} back ")
    # else:
    #     print("Not a valid input")
#
# from turtle import Turtle, Screen
# import another_module
# timmy = Turtle()
# print(another_module.another_variable)
# print(timmy)
# my_screen = Screen()
# print(my_screen.canvheight)
# # function tied to an object is called method
# timmy.shape("turtle")
# timmy.color("coral")
# timmy.forward(100 )
# my_screen.exitonclick()

# python packages

# pypi.org
# from prettytable import PrettyTable
# table = PrettyTable()
# table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
# table.add_column("Type", ["Electric", "Water", "Fire"])
# table.align = "r"
# print(table)

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

profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

def is_resource_sufficient(order_ingredients):
    """Returns True when order can be made, false if ingredients are insufficient"""
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"Sorry ter is not enough {item}.")
            return False
    return True


def process_coins():
    """Returns the total calculated from coins inserted"""
    print("Please insert coins.")
    total = int(input("how many quarters?: ")) * 0.25
    total += int(input("how many dimes?: ")) * 0.10
    total += int(input("how many nickles?: ")) * 0.05
    total += int(input("how many pennies?: ")) * 0.01
    return total


def make_coffee(drink_name, order_ingredients):
    """Deduct the required ingredients from the resources"""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name} ☕.")


def is_transaction_successful(money_received, drink_cost):
    """Return True when payment is accepted,or False if money is insufficient."""
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Here is ${change} in change.")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded")
        return False


is_on = True

while is_on:
    choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if choice == "off":
        is_on = False
    elif choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${profit}")
    else:
        drink = MENU[choice]
        if is_resource_sufficient(drink['ingredients']):
            payment = process_coins()
            if is_transaction_successful(payment,drink["cost"]):
                make_coffee(choice, drink['ingredients'])






























