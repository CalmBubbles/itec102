# MODULE 11: FUNCTIONS
# 4: Recursion
# Diff: Intermediate

def goldenRatio (n: int):
    if n <= 1: return 1
    else: return 1 + 1 / goldenRatio(n - 1)

print(f"{goldenRatio(999):.17}")
print(f"{goldenRatio(1000):.17}") # Too much recursion breaks stuff