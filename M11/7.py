# MODULE 11: FUNCTIONS
# 7: Spinning spinning (RAM EATER)
# Diff: Hard (not really LOLLL)

# Example 4's recursion could only run 999 times
# This could go for longer

# For higher precision cus why not
from decimal import Decimal

def goldenRatio (n: int):
    output = 1

    for i in range(1, n):
        output = Decimal(1 + 1 / output)
    
    return output

# Now, this will only break when there's no more ram
# Set it too high and you freeze
print(f"{goldenRatio(99999):.27f}")