# MODULE 8: LISTS OF LISTS
# 2: Print nested
# Diff: Easy

print("Count: ", end = "")
count = int(input())

print("Items:")
alist = []

for i in range(count):
    print("    ", end = "")
    alist.append([input()])

print()
print(*alist)