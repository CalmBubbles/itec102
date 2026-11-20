# MODULE 9: LIST METHODS
# 4: Names sorter
# Diff: Intermediate

print("Target name count: ", end = "")
nameCount = int(input())

print("Names:")
names = []

for i in range(nameCount):
    print(f"  {i + 1}. ", end = "")
    name = input().strip()
    names.append(name)

names = [name for name in names if not name.isspace() and name != ""]
nameCount = len(names)
print(f"\nValid name count: {nameCount}")

names.sort()
sNamesByLengthA = sorted(names, key = len)
sNamesByLengthD = sorted(names, key = len, reverse = True)

print("\nSorted alphabetically (A-Z):")
for i in range(nameCount): print(f"  {i + 1}. {names[i]}")

print("\nSorted by length (Ascending):")
for i in range(nameCount): print(f"  {i + 1}. {sNamesByLengthA[i]}")

print("\nSorted by length (Descending):")
for i in range(nameCount): print(f"  {i + 1}. {sNamesByLengthD[i]}")