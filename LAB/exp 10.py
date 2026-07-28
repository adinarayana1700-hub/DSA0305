ags
tags = {
    "I": "PRON",
    "dogs": "NOUN",
    "run": "NOUN",   # Initial tag
    "fast": "ADV"
}

sentence = input("Enter a sentence: ").split()

print("\nPOS Tags:")

for word in sentence:
    tag = tags.get(word, "UNKNOWN")
    if word == "run" and tag == "NOUN":
        tag = "VERB"

    print(word, "->", tag)
