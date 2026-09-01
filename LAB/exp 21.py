import nltk
sentence = input("Enter sentence: ")
words = nltk.word_tokenize(sentence)
tags = nltk.pos_tag(words)
grammar = "NP: {<DT>?<JJ>*<NN.*>+}"
parser = nltk.RegexpParser(grammar)
tree = parser.parse(tags)
print("Noun Phrases:")
for subtree in tree.subtrees():
    if subtree.label() == "NP":
        print(" ".join(word for word, tag in subtree.leaves()))
