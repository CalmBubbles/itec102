# MODULE 8: LISTS OF LISTS
# 8: Matrix multiplication
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

print("\nMatrix A:")
matA = []

for y in range(height):
    print("\t", end = "")
    inDat = input().split(" ")

    matA.append([float(inDat[x]) for x in range(width)])

print("\nMatrix B:")
matB = []

for y in range(height):
    print("\t", end = "")
    inDat = input().split(" ")

    matB.append([float(inDat[x]) for x in range(width)])

outputMat = [
    [0 for b in range(len(matB[0]))]
    for a in range(len(matA))
]

for a in range(len(matA)):
    for b in range(len(matB[0])):
        for ab in range(len(matB)): outputMat[a][b] += matA[a][ab] * matB[ab][b]

print("\nOutput: ")
for r in outputMat: print(f"\t{" ".join([f"{i:.2f}" for i in r])}")