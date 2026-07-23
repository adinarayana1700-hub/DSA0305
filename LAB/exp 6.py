text = input("Enter a sentence: ")
words = text.split()

print("\nGenerated Bigrams:")
for i in range(len(words) - 1):
    print("(", words[i], ",", words[i + 1], ")")
