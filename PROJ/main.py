from Loop import Loop
import os;
import keyboard
import random

for i in range(150): keyboard.block_key(i)

# Loop.targetFrameRate = 30
Loop.Start()

bye = False
chaosMode = 0
consoleSize = None
cMInp = False

def clearConsole ():
    os.system("cls" if os.name == "nt" else "clear")

def update ():
    global bye, consoleSize, consoleResized, chaosMode

    if bye:
        print("\033[0m")
        return

    consoleSize = os.get_terminal_size()

    updateInput()
    updateMeter()

    if chaosMode: drawChaos()
    else: drawMeter()

    consoleResized = False

def updateInput ():
    global bye, chaosMode, cMInp

    if keyboard.is_pressed("esc"):
        bye = True
        Loop.End()
        clearConsole()
    
    if keyboard.is_pressed("1"):
        if not cMInp:
            chaosMode = not chaosMode
            print("\033[0m")
            clearConsole()

        cMInp = True
    else: cMInp = False


time = 0
duration = 0.5
aveDT = 0
aveUDT = 0
deltas = []
unscaledDeltas = []

def updateMeter ():
    global time, aveDT, aveUDT

    deltas.append(Loop.deltaTime)
    unscaledDeltas.append(Loop.unscaledDeltaTime)

    time += Loop.deltaTime
    if time < duration: return

    sum = 0
    for i in range(len(deltas)): sum += deltas[i]
    aveDT = sum / len(deltas)

    uSum = 0
    for i in range(len(unscaledDeltas)): uSum += unscaledDeltas[i]
    aveUDT = uSum / len(unscaledDeltas)

    deltas.clear()
    unscaledDeltas.clear()
    time = 0

def drawMeter ():
    global consoleResized, aveDT, aveUDT
        
    clearConsole()

    lines = [
        "",
        "Your keyboard is currently immobilized, but you can:",
        "Press Esc to Close",
        "Press 1 to Toggle Screen",
        "",
        f"Target FPS: {Loop.targetFrameRate}",
        f"Frame Count: {Loop.frameCount}",
        f"Time Scale: {Loop.timeScale}",
        f"Max Delta Time: {Loop.maximumDeltaTime}",
        "",
        f"Time: {round(Loop.time, 2)}s",
        f"Unscaled Time: {round(Loop.unscaledTime, 2)}s",
        "",
        f"In {duration}s",
        f"  FPS : {round(1 / aveDT if aveDT != 0 else 0, 2)}",
        f"  ms  : {round(1e3 * aveDT, 2)}",
        f"  Unscaled FPS : {round(1 / aveUDT if aveUDT != 0 else 0, 2)}",
        f"  Unscaled ms  : {round(1e3 * aveUDT, 2)}"
    ]
    print("\n".join(lines), flush = True)


colorRnd = random.randint(0, 5)
color = ""

def drawChaos ():
    global consoleSize, colorRnd, color

    for y in range(consoleSize.lines):
        if (int(Loop.time) % 10 == 0): colorRnd = random.randint(0, 5)

        match colorRnd:
            case 0: color = "\033[94m"
            case 1: color = "\033[96m"
            case 2: color = "\033[92m"
            case 3: color = "\033[93m"
            case 4: color = "\033[0m"
            case 5: color = "\033[91m"

        text = ""
        
        zero = "0"
        one = "1"

        # zero = "▓"
        # one = "█"

        for x in range(consoleSize.columns):
            text += one if random.randint(0, 1) == 1 else zero

        print(f"{color}{text}", flush = True)


clearConsole()
Loop.Append(update, 0, lambda: bye)