# MODULE 11: FUNCTIONS
# 8: Mini library of babel
# Diff: Hard

# this was a bad idea...

import random

length = 1600
chars = "abcdefghijklmnopqrstuvwxyz,. "
charsLength = len(chars)
b36 = "0123456789abcdefghijklmnopqrstuvwxyz"

def char2dec (text: str):
    output = 0

    for c in text: output = chars.index(c) + charsLength * output

    return output

def dec2base36 (no: int):
    if no == 0: return "0"

    output = []

    while no > 0:
        no, re = (no // 36, no % 36)
        output.append(b36[re])

    return "".join(reversed(output))

def find (text: str):
    safeText = "".join([c if c in chars else " " for c in text])
    safeText = safeText.lower().ljust(length)

    return dec2base36(char2dec(safeText))

# def placeholdertext (address: str):
#     no = int(hex_address, 36)
    
#     output

print(find("hi"))