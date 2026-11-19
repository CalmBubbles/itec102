# MODULE 14: FILE STREAMING
# 4: Text caser
# Diff: Intermediate

# NOTE: some sentences might break unintentionally, especially on abbr.

shouldBreak = False
breakers = (".", "!", "?")
sentences = [""]
words = []

with open("M14/4/input.txt", "r") as file:
    text = file.read()
    words = text.split(" ")

for i in text:
    if shouldBreak == 1 and i.isspace(): shouldBreak = 2
    elif shouldBreak == 2 and not i.isspace():
        shouldBreak = 0
        sentences.append("")

    sentences[-1] += i

    if shouldBreak == 0 and i in breakers: shouldBreak = 1

with open("M14/4/output/Sentence case.txt", "w") as file:
    sentenceCase = "".join([t.capitalize() for t in sentences])
    file.write(sentenceCase)

with open("M14/4/output/lowercase.txt", "w") as file:
    lowerCase = "".join([t.lower() for t in sentences])
    file.write(lowerCase)

with open("M14/4/output/UPPERCASE.txt", "w") as file:
    upperCase = "".join([t.upper() for t in sentences])
    file.write(upperCase)

with open("M14/4/output/Title Case.txt", "w") as file:
    titleCase = "".join([t.title() for t in sentences])
    file.write(titleCase)

with open("M14/4/output/PascalCase.txt", "w") as file:
    pascalCase = "".join([w.capitalize() for w in words])
    file.write(pascalCase)

with open("M14/4/output/camelCase.txt", "w") as file:
    camelCase = "".join([words[i].capitalize() if i > 0 else words[i].lower() for i in range(len(words))])
    file.write(camelCase)

with open("M14/4/output/snake_case.txt", "w") as file:
    snakeCase = "_".join([w.lower() for w in words])
    file.write(snakeCase)

with open("M14/4/output/SCREAMING_SNAKE_CASE.txt", "w") as file:
    file.write(snakeCase.upper())