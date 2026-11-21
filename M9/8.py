# MODULE 9: LIST METHODS
# 8: Popped list
# Diff: Hard

import random

poppedListBag = list(range(440))
tryCount = random.randint(len(poppedListBag), len(poppedListBag) * 4)
tryIndex = 0
unpopped = poppedListBag.copy()

while tryIndex < tryCount:
    index = random.randint(0, len(poppedListBag) - 1)
    popped = poppedListBag.pop(index)

    if popped in unpopped: unpopped.remove(popped)

    poppedListBag.append(popped)

    tryIndex += 1

for i in range(len(poppedListBag)):
    if i == poppedListBag[i]: unpopped.append(i)

print("The bag:")
print(*poppedListBag)

print("\nUnpopped:")
print(*unpopped)