# MODULE 14: FILE STREAMING
# 5: Text repeater (storage eater)
# Diff: Intermediate

# Just replace these vars LOLLL
text = "Thus. You cease to move. Trapped in the stopped time. For eternity."
count = 67676767 # WARNING: DON'T SET IT TOO HIGH

bytesCount = count * len(text.encode("utf-8")) + count - 1

print(f"Repeating: \"{text}\"")
print(f"    {count} Times")
print(f"    Possible allocation: {bytesCount} bytes\n")

print("Eating Storage...\n")

with open("M14/5/output.txt", "w") as file: file.write(text)
with open("M14/5/output.txt", "a") as file:
    lastPercent = 0

    for i in range(count - 1):
        file.write(f"\n{text}")

        percent = i / (count - 1)
        percent = percent - percent % 0.1

        if percent > lastPercent:
            lastPercent = percent
            print(f"{(percent * 100):.1f}%...")

print("Done (I think IDK)")