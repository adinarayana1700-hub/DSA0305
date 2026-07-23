import nltk

# Input sentence
text = input("Enter a sentence: ")

# Tokenize the sentence into words
words = nltk.word_tokenize(text)

# Perform POS tagging
tags = nltk.pos_tag(words)

print("\nWord\t\tPOS Tag")
print("-------------------------")

for word, tag in tags:
    print(word, "\t\t", tag)
