# MODULE 13: TUPLES, SETS & DICTIONARIES
# 7: Text Combo
# Diff: Hard

print("Insert anything to combo:\n\t", end = "")
text = input().strip()

combos = set()

# why classify this as hard?
# i was sleepy when doing this
# so i kinda did struggle lol
# majik cus it just kinda works LOLLL
def majik (chars, ok):
    if len(chars) == len(text):
        combos.add("".join(chars).strip())
        return

    for i in range(len(text)):
        if ok[i]: continue

        nextChars = [*chars, text[i]]
        nextOk = [*ok]
        nextOk[i] = True
        majik(nextChars, nextOk)

if len(text) <= 1: print("\nTHAT AIN'T COMBOABLE")
else:
    majik([], [False] * len(text))
    combos = sorted(combos)

    print(f"\nMade {len(combos)} combos...", end = "")
    input()

    for i in range(len(combos)): print(f"    {i + 1}: {combos[i]}")