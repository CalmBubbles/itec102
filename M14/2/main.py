# MODULE 14: FILE STREAMING
# 2: Text merger
# Diff: Easy

mergeWhat = (
    "rick",
    "DOCUMENT.oneshot.txt",
    "en_US.json"
)
contents = []

for name in mergeWhat:
    try:
        with open(f"M14/2/input/{name}", "r", encoding = "utf+8") as file: contents.append(file.read())
    except FileNotFoundError: pass

contents = "\n\n".join(contents)

with open("M14/2/output", "w", encoding = "utf+8") as file: file.write(contents)