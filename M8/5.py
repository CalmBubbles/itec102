# MODULE 8: LISTS OF LISTS
# 5: Grid sum
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


lineSums = [sum(line) for line in grid]
print("\nLine sums:")
for s in lineSums: print(f"\t{s:.2f}")


allSum = sum(lineSums)
print(f"\nSum: {allSum:.2f}")