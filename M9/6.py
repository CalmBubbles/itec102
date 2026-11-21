# MODULE 9: LIST METHODS
# 6: Flatter
# Diff: Intermediate

nested = [1, 2, 3, [4, [5, 6, [7], 8], 9, 10], [11, [12], 13, 14, [[[[[[[[[[[[15]]]]]]]]]]]]]]

def flatten (nested):
    output = []

    for item in nested:
        if isinstance(item, list): output.extend(flatten(item))
        else: output.append(item)
    
    return output

flat = flatten(nested)
print(flat)