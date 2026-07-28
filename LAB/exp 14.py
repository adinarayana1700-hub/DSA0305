sentence = input("Enter a sentence: ").lower().split()

if len(sentence) != 3:
    print("Invalid sentence")
else:
    subject = sentence[0]
    verb = sentence[1]

    if (subject in ["he", "she", "it"] and verb.endswith("s")) or \
       (subject in ["i", "you", "we", "they"] and not verb.endswith("s")):
        print("Sentence is Correct")
    else:
        print("Sentence is Incorrect")
