grammar = {
    "I eat apple": 0.90,
    "She likes mango": 0.85,
    "He reads book": 0.80
}
sentence = input("Enter a sentence: ")
if sentence in grammar:
    print("Sentence Accepted")
    print("Probability =", grammar[sentence])
else:
    print("Sentence Rejected")
