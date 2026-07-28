import re
sentence = input("Enter a sentence: ").split()
print("\nPOS Tags:")
for word in sentence:
    if re.fullmatch(r".*ing", word):
        print(word, "-> VERB")
    elif re.fullmatch(r".*ed", word):
        print(word, "-> VERB")
    elif re.fullmatch(r".*ly", word):
        print(word, "-> ADVERB")
    elif re.fullmatch(r".*ous", word):
        print(word, "-> ADJECTIVE")
    elif re.fullmatch(r".*ion", word):
        print(word, "-> NOUN")
    else:
        print(word, "-> UNKNOWN")
