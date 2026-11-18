# MODULE 14: FILE STREAMING
# 1: It just reads and write
# Diff: Easy

with open("M14/1/read.txt", "r", encoding = "utf+8") as file:
    content = file.read()
    print(content)

with open("M14/1/write.txt", "w", encoding = "utf+8") as file:
    file.write(content)