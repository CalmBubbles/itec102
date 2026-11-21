# MODULE 8: LISTS OF LISTS
# 6: Grid min, max, ave
# Diff: Intermediate

print("Width: ", end = "")
width = int(input())
print("Height: ", end = "")
height = int(input())

print("\nSeparate X using spaces")
print("Separate Y using enter")
print("Like...")
print("\t0 0 0")
print("\t0 0 0")
print("\t0 0 0")

grid = []

print("\nGrid:")

for y in range(height):
    print("\t", end = "")
    inDat = input().split(" ")

    grid.append([float(inDat[x]) for x in range(width)])

lineMins = [min(line) for line in grid]
lineMaxs = [max(line) for line in grid]
lineAves = [sum(line) / len(line) for line in grid]

print("\nLine lowests:")
for s in lineMins: print(f"\t{s:.2f}")

print("Line highests:")
for s in lineMaxs: print(f"\t{s:.2f}")

print("Line averages:")
for s in lineAves: print(f"\t{s:.2f}")


allMin = min(lineMins)
allMax = max(lineMaxs)
allAve = sum(lineAves) / len(lineAves)

print(f"\nLowest: {allMin:.2f}")
print(f"Highest: {allMax:.2f}")
print(f"Average: {allAve:.2f}")