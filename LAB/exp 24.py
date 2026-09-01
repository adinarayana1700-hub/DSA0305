def dialog_act(sentence):
    sentence = sentence.lower()
    if sentence.startswith(("hi", "hello", "good morning", "good evening")):
        return "Greeting"
    elif sentence.endswith("?"):
        return "Question
    elif sentence.startswith(("please", "can you", "could you")):
        return "Request"
    else:
        return "Statement"
text = input("Enter dialog: ")
sentences = text.split("|")
for sentence in sentences:
    print(sentence, "->", dialog_act(sentence.strip()))
