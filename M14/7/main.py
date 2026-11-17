# MODULE 14: FILE STREAMING
# 7: UNDERTALE Save Editor
# Diff: Hard

unusedLines = {
    3, 30, 31, 32, 33, 48, 49, 59, 68, 69,
    78, 79, 91, 101, 114, 117, 131, 146, 147, 148,
    149, 150, 151, 152, 153, 154, 155, 156, 157, 158,
    159, 187, 188, 189, 190, 191, 192, 193, 194, 195,
    196, 197, 198, 199, 200, 201, 202, 203, 204, 205,
    206, 207, 208, 209, 210, 211, 212, 213, 214, 215,
    216, 217, 218, 219, 220, 237, 238, 239, 240, 241,
    242, 243, 244, 245, 246, 247, 248, 249, 250, 256,
    257, 258, 259, 260, 261, 262, 263, 264, 265, 266,
    267, 268, 269, 270, 271, 272, 273, 274, 275, 276,
    277, 278, 279, 287, 288, 289, 298, 303, 304, 315,
    327, 328, 329, 354, 355, 356, 357, 358, 359, 360,
    361, 362, 363, 364, 365, 366, 367, 368, 369, 370,
    371, 372, 373, 374, 375, 376, 377, 378, 379, 389,
    395, 414, 422, 424, 440, 441, 442, 452, 457, 458,
    459, 468, 469, 476, 477, 478, 479, 481, 493, 494,
    496, 497, 498, 499, 501, 502, 503, 504, 507, 508,
    528
}
labels = []
lines = []
indexing = ()
longestLabel = 0
edited = False

def cont ():
    print("Enter to continue... ", end = "")
    input()

def line (length: int = 10):
    text = "".join(["-" for i in range(length)])
    print(text)

def fixLabel (text: str):
    addCount = longestLabel - len(text)
    end = "".join([" " for i in range(addCount)])
    return f"{text}{end}"

def usure ():
    print("Are you sure? (*N/Y): ", end = "")
    return input().lower().startswith("y")

def display ():
    line(longestLabel)

    for i in range(len(indexing)):
        index = indexing[i]
        label = fixLabel(f"{i}. {labels[index]}")
        print(f"{label}: {lines[index]}")
    
    line(longestLabel)

    print("edit: e {index} {new value}")
    print("save: s")
    print("save and quit: w")
    print("just quit: q\n")

    inDat = input().split(" ")

    match inDat.pop(0).lower():
        case "e": edit(inDat)
        case "s": save()
        case "w": 
            if (savequit()): return
        case "q":
            if (bye()): return
    
    print()
    display()
            
def edit (inDat):
    global edited

    if len(inDat) < 2:
        print("MISSING ARGUMENTS")
        cont()
        return
    
    index = inDat.pop(0)

    if not index.isdigit() or int(index) not in range(len(indexing)):
        print("INVALID INDEX")
        cont()
        return

    value = " ".join(inDat)
    realIndex = indexing[int(index)]

    print(f"EDITED: {index}. {labels[realIndex]}: \"{lines[realIndex]}\" -> \"{value}\"")
    lines[realIndex] = value
    edited = True

    cont()

def bye ():
    print("QUIT", end = "")

    if not edited: return True

    print(": You have unsaved stuff. ", end = "")
    return usure()

def savebase ():
    content = "\n".join([
        f"{lines[i]} " if i > 0 else lines[i]
        for i in range(len(lines))
    ])
    with open("M14/7/save", "w") as file:
        file.write(content)
    
    edited = False

    print("Saved")
    cont()

def save ():
    print("SAVE: This will overwrite the file. ", end = "")

    if (not usure()):
        print("Cancelled save")
        cont()
        return

    savebase()

def savequit():
    print("SAVE & QUIT: This will overwrite the file. ", end = "")

    if (not usure()):
        print("Cancelled save and quit")
        cont()
        return False
    
    savebase()
    return True

def main ():
    global labels, lines, indexing, longestLabel

    print("Simple UNDERTALE Save Editor")

    with open("M14/7/labels", "r") as file:
        labels = [line.strip() for line in file.readlines()]

    try:
        with open("M14/7/save", "r") as file:
            lines = [line.strip() for line in file.readlines()]
    except FileNotFoundError:
        print("FILE \"save\" NOT FOUND")
        return

    if len(lines) < len(labels):
        print("INVALID SAVE")
        return

    indexing = tuple(set(range(len(labels))) - unusedLines)
    longestLabel = 3 + len(str(len(labels))) + len(max(labels, key = len))
    
    display()

main()


# Credits:
#     UNDERTALE by Toby Fox
#     Line-by-line breakdown from https://docs.google.com/spreadsheets/d/1kQZ3FvunKb2PSkFkjVzK3BhIDLvIZkf-tsKGhuUa_0A