# MODULE 14: FILE STREAMING
# 7: Mail merge type ahh
# Diff: Hard

data = [[]]

with open("M14/7/data_format.txt", "r") as file:
    dataProps = [line.strip() for line in file.readlines()]

with open("M14/7/text.txt", "r", encoding = "utf-8") as file:
    text = file.read()

with open("M14/7/data.txt", "r") as file:
    lines = file.read().split("\n")

for line in lines:
    if line == "":
        data.append([])
        continue
    
    data[-1].append(line)

for i in range(len(data)):
    currentText = text
    args = data[i]

    for j in range(len(args)):
        currentText = currentText.replace(f"«{dataProps[j]}»", args[j])

    with open(f"M14/7/output/{i}.txt", "w", encoding = "utf-8") as file:
        file.write(currentText)