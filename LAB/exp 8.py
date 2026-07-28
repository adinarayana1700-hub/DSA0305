# Simple Stochastic POS Tagger

# Probable POS tags
pos_tags = {
    "i": "PRON",
    "you": "PRON",
    "he": "PRON",
    "she": "PRON",
    "eat": "VERB",
    "eats": "VERB",
    "like": "VERB",
    "likes": "VERB",
    "apple": "NOUN",
    "apples": "NOUN",
    "mango": "NOUN",
    "book": "NOUN",
    "is": "VERB",
    "good": "ADJ",
    "big": "ADJ"
}

# Input sentence
sentence = input("Enter a sentence: ").lower().split()

print("\nPOS Tags:")
for word in sentence:
    tag = pos_tags.get(word, "UNKNOWN")
    print(word, "->", tag)
