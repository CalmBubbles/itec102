# MODULE 8: LISTS OF LISTS
# 3: Nest to odd even
# Diff: Easy

print("Count: ", end = "")
count = int(input())

print("Numbers:")
alist = []

for i in range(count):
    print("    ", end = "")
    alist.append(int(input()))

oList = [i for i in alist if i % 2 != 0]
eList = [i for i in alist if i % 2 == 0]

nested = [oList, eList]

print("\n[[\"ODD\"], [\"EVEN\"]]")
print(nested)