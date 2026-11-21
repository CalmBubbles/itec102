# MODULE 9: LIST METHODS
# 5: Gridder
# Diff: Hard

flat = [1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1]
sideLen = int(len(flat) * 0.25)
gridded = []
currentList = []

for i in range(len(flat)):
    currentList.append(flat[i])

    if len(currentList) >= sideLen:
        gridded.append(currentList)
        currentList = []

for item in gridded: print(item)