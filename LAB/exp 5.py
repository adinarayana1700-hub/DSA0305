
from nltk.stem import PorterStemmer

# Create Porter Stemmer object
ps = PorterStemmer()

# List of words
words = ["playing", "running", "studies", "jumping", "cats", "happily"]

print("Original Word\tStemmed Word")
print("-----------------------------")

# Perform stemming
for word in words:
    stem = ps.stem(word)
    print(word, "\t\t", stem)
