
sentence = input("Enter sentence: ").lower().split()
if len(sentence) == 3:
    print("\nParse Tree")
    print("        S")
    print("      / | \\")
    print("    NP  VP  ")
    print("    |   / \\")
    print(" ", sentence[0], sentence[1], sentence[2])
else:
    print("Invalid sentence")
