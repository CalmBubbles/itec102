# MODULE 13: TUPLES, SETS & DICTIONARIES
# 8: Text "analyzer"
# Diff: Hard

print("Insert text:\n\t", end = "")
text = input()

sentenceShouldBreak = 0
breakers = (".", "!", "?")
sentences = [""]
punc = "!?,.:;\"()\\/{}[]`"
noPuncText = "".join([" " if char in punc else char for char in text])
words = [word for word in noPuncText.split(" ") if not (word.isspace() or word == "")]

# NOTE: some sentences might break unintentionally, especially on abbr.
for i in text:
    if sentenceShouldBreak == 1 and i.isspace(): sentenceShouldBreak = 2
    elif sentenceShouldBreak == 2 and not i.isspace():
        sentenceShouldBreak = 0
        sentences.append("")

    sentences[-1] += i

    if sentenceShouldBreak == 0 and i in breakers: sentenceShouldBreak = 1

sentences = [s.strip() for s in sentences]

def line (length: int = 10):
    text = "".join(["-" for i in range(length)])
    print(text)

print()
line(40)
print(f"Sentence count: {len(sentences)}")
print(f"Shortest sentence: {min(sentences, key = len)}")
print(f"Longest sentence: {max(sentences, key = len)}")
line(30)

for i in range(len(sentences)): print(f"    {i + 1}: {sentences[i]}\n")

line(40)

loweredWords = [word.lower() for word in words]
uniqueWords = {}

for word in loweredWords:
    if word in uniqueWords: uniqueWords[word] += 1
    else: uniqueWords[word] = 1

uniqueWords = dict(sorted(uniqueWords.items()))

print(f"Word count: {len(words)}")
print(f"Unique word count: {len(uniqueWords)}")
print(f"Shortest word: {min(uniqueWords, key = len)}")
print(f"Longest word: {max(uniqueWords, key = len)}")
line(30)
print("UNIQUE WORDS AND APPEARANCE COUNT")
line(30)

uniqueWordsCounter = 1

for word in uniqueWords:
    print(f"    {uniqueWordsCounter}: {word} ({uniqueWords[word]})")
    uniqueWordsCounter += 1

line(40)

charset = sorted(set(text))

print(f"Character count: {len(text)}")
print(f"Unique character count: {len(charset)}")
line(30)

for i in range(len(charset)): print(f"    {i + 1}: {charset[i]}")