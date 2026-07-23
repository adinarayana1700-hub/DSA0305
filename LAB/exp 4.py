word = input("Enter a singular noun: ")

state = "START"

if state == "START":

    if word.endswith("y"):
        state = "Y_RULE"
        plural = word[:-1] + "ies"

    elif word.endswith(("s", "x", "z", "ch", "sh")):
        state = "ES_RULE"
        plural = word + "es"

    else:
        state = "S_RULE"
        plural = word + "s"

print("\nCurrent State :", state)
print("Singular Word :", word)
print("Plural Word   :", plural)
