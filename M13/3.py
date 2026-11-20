# MODULE 13: TUPLES, SETS & DICTIONARIES
# 3: Dictionaries
# Diff: Easy

adictionary = {
    "is": "a collection of key:value pairs",
    "where": "a key is used to address a value"
}

print(adictionary)

adictionary["is"] = "something idk"
print(adictionary["is"])

adictionary["where"] = "somewhere idk"
print(adictionary.get("where"))

adictionary.pop("where")
print(adictionary)