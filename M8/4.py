# MODULE 8: LISTS OF LISTS
# 4: Overnester
# Diff: Intermediate

print("Nest count: ", end = "")
count = int(input())
nested = []
last = nested

for i in range(count):
    current = []
    last.append(current)
    last = current

print()
print(nested)