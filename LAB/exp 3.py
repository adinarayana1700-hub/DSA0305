import nltk
from nltk.stem import PorterStemmer
stemmer = PorterStemmer
text = input("Enter a sentence: ")
words = text.split()

print("\nOriginal Words\tRoot Words")
print("-------------------------------")
for word in words:
    root = stemmer.stem(word)
    print(word, "\t\t", root)
