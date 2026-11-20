# MODULE 11: FUNCTIONS
# 6: Nicer Russian roulette (i was planning something worse sorry)
# Diff: Intermediate

# Run as Admin for maximum immersion

import platform
import subprocess
import random

automove = 0
amovelist = [
    "Off",
    "Shuffle",
    "Turn"
]
os = platform.system()
bulletPos = random.randint(1, 6)
currentPos = random.randint(1, 6)

def cont ():
    print("Enter to continue... ", end = "")
    input()

def die ():
    print("BANG!!!")

    if os == "Windows":
        subprocess.run("shutdown /f /s /t 0".split(" "), check = True)
    elif os in ("Linux", "Darwin"):
        subprocess.run("sudo shutdown -h now".split(" "), check = True)
    else:
        print("??????????????????")

    cont()

def shuffle (nocont: bool = False):
    global currentPos

    currentPos = random.randint(1, 6)

    print("Shuffled")
    if not nocont: cont()

def turn (nocont: bool = False):
    global currentPos

    currentPos += 1
    if currentPos > 6: currentPos = 1

    print("Turned")
    if not nocont: cont()

def shoot ():
    if currentPos == bulletPos: die()
    else:
        print("Click!")
        cont()
    
    if automove == 1: shuffle(True)
    elif automove == 2: turn(True)

def amove ():
    global automove

    automove += 1
    if automove > 2: automove = 0

    print(f"Automove: {amovelist[automove]}")
    cont()

def main ():
    print("\nRussian Roulette")
    print("--------------------")
    print("0: Shuffle")
    print("1: Turn")
    print("2: Shoot")
    print(f"3: Automove (RN: {amovelist[automove]})")
    print("4: Stop\n")

    inDat = input().strip()

    match inDat:
        case "0": shuffle()
        case "1": turn()
        case "2": shoot()
        case "3": amove()
        case "4": return
    
    main()

main()