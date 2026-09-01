import re
text = input("Enter text: ")
sentences = text.split(".")
last_noun = None
pronouns = ["he", "she", "it", "they", "him", "her"]
for sentence in sentences:
    words = sentence.strip().split()
    for word in words:
        clean = re.sub(r'[^\w]', '', word)
        if clean.lower() not in pronouns:
            if clean[0:1].isupper():
                last_noun = clean
        if clean.lower() in pronouns and last_noun:
            print(clean, "->", last_noun)
