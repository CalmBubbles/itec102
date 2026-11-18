# MODULE 13: TUPLES, SETS & DICTIONARIES
# 5: Listahan ng may utang sakin
# Diff: Intermediate

utang = {}

def isValidAmount (val: str):
    try:
        return float(val) > 0
    except (ValueError, TypeError):
        return False

def trunc (no):
    return int(no * 100) / 100

def line (length: int = 10):
    text = "".join(["-" for i in range(length)])
    print(text)

def cont ():
    print("Enter to continue... ", end = "")
    input()

def addUtang ():
    print("ADD")
    line()

    print("Name: ", end = "")
    name = input().strip()

    print("Amount: ", end = "")
    amount = input().strip()

    if not isValidAmount(amount):
        print("INVALID AMOUNT")
        cont()
        return
    
    amount = trunc(float(amount))
    
    if name not in utang: utang[name] = 0
    utang[name] += amount

    print(f"Added {amount:.2f} to {name}")
    cont()

def rmUtang ():
    if len(utang) == 0:
        print("WLA PANG NANGUNGUTANG")
        cont()
        return
    
    print("REMOVE")
    line()
    
    print("Name: ", end = "")
    name = input().strip()

    if name not in utang:
        print("WLANG UTANG YAN")
        cont()
        return

    print("Amount: ", end = "")
    amount = input().strip()

    if not isValidAmount(amount):
        print("INVALID AMOUNT")
        cont()
        return
    
    amount = min(trunc(float(amount)), trunc(utang[name]))
    
    utang[name] -= amount
    if (utang[name] <= 0): utang.pop(name)

    print(f"Removed {amount:.2f} from {name}")
    cont()

def display():
    if len(utang) == 0:
        return
    
    for tao in utang: print(f"{tao}: {utang[tao]:.2f}")

    line()

def main ():
    print("\nMGA MAY UTANG SAKIN")
    line(20)

    display()

    print("0: Add")
    print("1: Remove")
    print("2: Exit\n")

    inDat = input().strip()

    match (inDat):
        case "0": addUtang()
        case "1": rmUtang()
        case "2": return

    main()

main()