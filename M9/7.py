# MODULE 9: LIST METHODS
# 7: Grades "analyzer"
# Diff: Intermediate

def isValidGrade (val: str):
    try:
        dat = float(val)
        return dat >= 0 and dat <= 100
    except (ValueError, TypeError):
        return False

print("Insert grades (0-100) separeted w/ spaces:\n\t", end = "")
grades = input().split(" ")
grades = [float(grade) for grade in grades if isValidGrade(grade)]

print(f"\nValid grades ({len(grades)}):\n    ", end = "")
for g in grades: print(f"{g:.2f} ", end = "")

ave = sum(grades) / len(grades)
highest = max(grades)
lowest = min(grades)
sortedA = sorted(grades)
sortedD = sorted(grades, reverse = True)

print(f"\n\nAverage: {ave:.2f}")
print(f"Lowest: {lowest:.2f}")
print(f"Highest: {highest:.2f}")

print("\nSorted (Ascending):")
for g in sortedA: print(f"    {g:.2f}")

print("\nSorted (Descending):")
for g in sortedD: print(f"    {g:.2f}",)