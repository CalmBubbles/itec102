# MODULE 13: TUPLES, SETS & DICTIONARIES
# 6: Menu "kiosk"
# Diff: Intermediate

# stolen from spooky month lol
title = "THE HOT CAULDRON"
menu = {
    "Appetizer": {
        "Child Fingers": 5,
        "Eye Eggs": 5,
        "Teeth Tater Tots": 9,
        "Mrushchetta": 10,
        "Prosciutto": 16
    },
    "Soups and Salads": {
        "Mushroom Cream Soup": 5,
        "Teeth Soup": 10,
        "Soupy Creamy Soup": 12,
        "Hag Salad": 5,
        "Mushroom Slaw": 5,
        "Twig Slaw": 10
    },
    "Main Course": {
        "Mushburger": 15,
        "Vegan Steak": 15,
        "Hair Bolognese": 20,
        "Witch Style Ribs": 20,
        "Baby Bread Bowl": 20,
        "Low Carbs Meal": 25,
        "Mushroom Butter Steak": 30,
        "Sauteed Soul": 50,
        "Dry Age Steak": 50,
        "Meat Platter": 100 
    },
    "Sides": {
        "Eyeballs wedges": 2.50,
        "Fried teeth": 2.50,
        "Fried fingers": 2.50,
        "Toasted Ears": 2.50,
        "Nails chips": 2.50,
        "Mushroom": 2.50
    }
}

menuFlat = []
cart = []
payment = 0

for category in menu:
    categoryItems = menu[category]

    for item in categoryItems: menuFlat.append((item, categoryItems[item]))

iProceed = len(menuFlat)
iExit = iProceed + 1

def line (length: int = 10):
    text = "".join(["-" for i in range(length)])
    print(text)

def cont ():
    print("Enter to continue... ", end = "")
    input()

def updateTotal ():
    global payment
    payment = 0

    for item in cart:
        payment += menuFlat[item][1]

def usure ():
    print("Are you sure? (*N/Y): ", end = "")
    return input().lower().startswith("y")

def checkout ():
    itemCount = len(cart)

    if itemCount == 0:
        print("NO ITEMS SELECTED")
        cont()
        return False

    print("\nCHECKOUT")
    line(20)

    for i in range(itemCount):
        item = cart[i]
        print(f"{i + 1}. {menuFlat[item][0]} @ ₱{menuFlat[item][1]:.2f}")
    
    line(20)

    print(f"Item Count: {itemCount}")
    print(f"Total: ₱{payment:.2f}")

    line()

    print(f"≤{itemCount}: Remove")
    print(f"{itemCount + 1}: Finish")
    print(f"{itemCount + 2}: Back\n")

    inDat = input()

    if inDat.isdigit():
        inDat = int(inDat) - 1

        if inDat in range(itemCount):
            cart.pop(inDat)
            updateTotal()

            print(f"Removed {menuFlat[inDat][0]} @ ₱{menuFlat[inDat][1]:.2f}")
            cont()
        elif inDat == itemCount:
            return finish()
        elif inDat == itemCount + 1:
            return False
    
    return checkout()

def finish ():
    print("FINISH: ", end = "")
    
    if not usure():
        print("Canceled Finish")
        cont()
        return checkout()
    
    print("\nYOUR ORDER I GUESS")
    line(30)
    
    itemCount = len(cart)

    for i in range(itemCount):
        item = cart[i]
        print(f"{i + 1}. {menuFlat[item][0]} @ ₱{menuFlat[item][1]:.2f}")
    
    line(20)

    print(f"Item Count: {itemCount}")
    print(f"Total: ₱{payment:.2f}\n")

    return True

def bye():
    if len(cart) == 0: return True

    print("EXIT: You will discard your items. ", end = "")
    
    if not usure():
        print("Cancelled Exit")
        cont()
        return False
    
    return True

def main ():
    print(title.upper())
    line(30)

    currentCount = 0

    for category in menu:
        print(category.upper())
        line(20)

        categoryItems = menu[category]

        for item in categoryItems:
            print(f"  {currentCount}: {item} @ ₱{categoryItems[item]:.2f}")
            currentCount += 1

        print()
        line(20)
    
    print(f"{iProceed}: Proceed to Checkout")
    print(f"{iExit}: Exit")

    line()

    print(f"Item Count: {len(cart)}")
    print(f"Total: ₱{payment:.2f}\n")

    inDat = input()

    if inDat.isdigit():
        inDat = int(inDat)

        if inDat in range(iProceed):
            cart.append(inDat)
            updateTotal()

            print(f"Added {menuFlat[inDat][0]} @ ₱{menuFlat[inDat][1]:.2f}")
            cont()
        elif inDat == iProceed:
            if (checkout()): return
        elif inDat == iExit:
            if (bye()): return
    
    print()
    main()

    
main()