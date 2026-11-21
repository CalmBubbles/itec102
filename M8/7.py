# MODULE 8: LISTS OF LISTS
# 7: Transpose grid
# Diff: Hard

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

transed = [
    [grid[y][x] for y in range(height)]
    for x in range(width)
]

print("\nTransposed: ")
for r in transed: print(f"\t{" ".join([f"{i:.2f}" for i in r])}")