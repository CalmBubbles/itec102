# MODULE 13: TUPLES, SETS & DICTIONARIES
# 4: Custom dictionary by dictionary
# Diff: Intermediate

daDic = {}

def line (length: int = 10):
    text = "".join(["-" for i in range(length)])
    print(text)

def cont ():
    print("Enter to continue... ", end = "")
    input()

def addDef ():
    print("\nADD/EDIT DEFINITION")
    line()

    print("Entry: ", end = "")
    entry = input()

    print("Definition: ", end = "")
    defin = input()

    daDic[entry] = defin
    print(f"\nAdded {entry}")
    cont()

def rmDef ():
    print("\nREMOVE DEFINITION")
    line()

    print("Entry: ", end = "")
    entry = input()

    if entry not in daDic:
        print("NO DEFINITION FOUND")
        cont()
        return

    daDic.pop(entry)
    print(f"\nRemoved {entry}")
    cont()

def display ():
    if len(daDic) == 0: return
    
    line()

    entries = sorted([entry for entry in daDic])

    for i in range(len(entries)):
        print(f"{entries[i]}:")
        print(f"    {daDic[entries[i]]}")
        if i < len(entries) - 1: print()

def main ():
    print("DICTIONARING CUSTOM (EYYYYY)")
    line(20)

    print("0: Add/Edit Definition")
    print("1: Remove Definition")
    print("2: Exit")

    display()

    print()

    inDat = input()

    match (inDat):
        case "0": addDef()
        case "1": rmDef()
        case "2": return

    main()

main()