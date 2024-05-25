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

coins = {
    "quarter": 0.25,
    "dime": 0.10,
    "nickle": 0.05,
    "penny": 0.01,
}


# TODO: 4. Check resources sufficient?
def check_resources(coffee_selected):
    """Check if there are available resources to proceed with making the coffee"""
    water_used = MENU[coffee_selected]["ingredients"]["water"]
    coffee_used = MENU[coffee_selected]["ingredients"]["coffee"]
    global resources
    if water_used <= resources["water"] and coffee_used <= resources["coffee"]:
        # TODO: 7. Make Coffee
        if coffee_selected == "espresso":
            resources["water"] -= water_used
            resources["coffee"] -= coffee_used
            return True
        else:
            milk_used = MENU[coffee_selected]["ingredients"]["milk"]
            if milk_used <= resources["milk"]:
                resources["milk"] -= milk_used
                resources["water"] -= water_used
                resources["coffee"] -= coffee_used
                return True
            else:
                return False
    else:
        return False


# TODO: 5. Process coins.
def process_coins():
    """Return the total amount of coins inserted in the machine by the user"""
    print("Please insert coins.")
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickles = int(input("How many nickles?: "))
    pennies = int(input("How many pennies?: "))
    return (quarters * coins["quarter"]) + (dimes * coins["dime"]) + (nickles * coins["nickle"]) + (
            pennies * coins["penny"])


# TODO: 1. Prompt user by asking “What would you like? (espresso/latte/cappuccino)
machine_money = 0
machine_running = True

while machine_running:
    coffee_selected = input("What would you like to drink? (espresso/latte/cappuccino): ").lower()
    if coffee_selected in MENU:
        if check_resources(coffee_selected):
            cost = MENU[coffee_selected]["cost"]
            total_coins = process_coins()
            # TODO: 6. Check transaction successful?
            if total_coins >= cost:
                change_coins = total_coins - cost
                machine_money += cost
                print(f"Here is ${change_coins:.2f} in change.")
                print(f"Here is your {coffee_selected} ☕. Enjoy!")
            else:
                print("Sorry that's not enough money. Money refunded.")
        else:
            print("Sorry there is not enough water.")
    elif coffee_selected == "report":
        # TODO: 3. Print report of all coffee machine resources
        print(f"Water: {resources["water"]} ml")
        print(f"Milk: {resources["milk"]} ml")
        print(f"Coffee: {resources["coffee"]} g")
        print(f"Money: ${machine_money}")
    elif coffee_selected == "off":
        # TODO: 2. Turn off the Coffee Machine by entering “off” to the prompt.
        print("Goodbye")
        machine_running = False
    else:
        print("The option that you entered doesn't exist.")
