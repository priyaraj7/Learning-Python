# Sandwich Maker
# Write a program that asks users for their sandwich preferences. The program should use PyInputPlus to ensure that they enter valid input, such as:
# Using inputMenu() for a bread type: wheat, white, or sourdough.
# Using inputMenu() for a protein type: chicken, turkey, ham, or tofu.
# Using inputYesNo() to ask if they want cheese.
# If so, using inputMenu() to ask for a cheese type: cheddar, Swiss, or mozzarella.
# Using inputYesNo() to ask if they want mayo, mustard, lettuce, or tomato.
# Using inputInt() to ask how many sandwiches they want. Make sure this number is 1 or more.

import pyinputplus as pyip

totalCost = 0
prices = {"wheat": 1, "white": 2, "sourdough": 2, "chicken": 4, "turkey": 3, "ham":2, "tofu": 5, "cheddar": 2, "swiss":5, "mozzarella":4, "mayo":4, "mustard":5, "lettuce":1, "tomato":2}

# To allow for different sandwiches in the order

while True:
    # make an empty dictonary to store the order details - resets order
    order = {}
    print("What bread you like?")
    order["bread"] = pyip.inputMenu(["wheat", "white", "sourdough"], numbered = True)
    print("How about the filling?")
    order["protein"] = pyip.inputMenu(["chicken", "turkey", "ham", "tofu"], numbered = True)
   
    wantCheese = pyip.inputYesNo("Would you like to have some cheese? ")
    if wantCheese == "yes":
        order["cheese"] = pyip.inputMenu(["cheddar", "Swiss", "mozzarella"], numbered = True)
    # Could put a while loop to allow for multiple options here
    wantDressing = pyip.inputYesNo("Would you like to have some more dressing? ")
    if wantDressing == "yes":
        order["side"] = pyip.inputMenu(["mayo", "mustard", "lettuce", "tomato"], numbered = True)
    orderNumber = pyip.inputInt("how many sandwiches you want?", min=1)

    # print(order) # {'bread': 'wheat', 'protein': 'turkey', 'cheese': 'cheddar'}

    # Calculate the price - loop through the order
    for item in order:
        if order[item] in prices.keys():
            totalCost += prices[order[item]]
     # Adjust if more than one
    totalCost *= orderNumber
    anotherOrder = pyip.inputYesNo("Will that be all: yes or no ")
    if anotherOrder == "yes":
        break

# THe string.format forces 2 decimal places (e.g. 13.10 rather than 13.1)
print(f'Your total price is ${totalCost}')

    