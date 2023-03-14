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

# returns true if order can be made and false if there are not enough ingredients
def enough_resources(order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print("Sorry there is not enough "+ item)
            return False
    return True

# calc the total amount of coins
def process_coins():
    print("Please insert coins. ")
    total = int(input("How many quarters?: ")) * 0.25
    total += int(input("How many dimes?: ")) * 0.10
    total += int(input("How many nickels?: ")) * 0.05
    total += int(input("How many pennies?: ")) * 0.01
    return total

def enough_coins(amt_paid, drink_cost):
    if amt_paid >= drink_cost:
        global profit
        profit += drink_cost
        change = round(amt_paid - drink_cost, 2)
        print(f"Here is ${change} in change.")
        return True
    else:
      print("Sorry that's not enough money. Money refunded")
    return False

# rquired ingredients become subtracted
def coffee_made(drink_name, order_ingredients):
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name} ")

is_on = True
while is_on:
    order = input("What would you like? (espresso/latte/cappuccino): ")
    if order == "off":
        is_on = False
    elif order == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${profit}")
    else:
        drink = MENU[order]
        if enough_resources(drink["ingredients"]):
            payment = process_coins()
            if enough_coins(payment, drink["cost"]):
                coffee_made(order, drink["ingredients"])






