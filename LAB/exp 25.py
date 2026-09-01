prompt = input("Enter a prompt: ")
responses = {
    "artificial intelligence":
        "Artificial Intelligence enables computers to perform intelligent tasks.",
    "python":
        "Python is a popular programming language used in many applications.",
    "machine learning":
        "Machine learning allows computers to learn patterns from data."
}
key = prompt.lower()
if key in responses:
    print("Generated Text:")
    print(responses[key])
else:
    print("Generated Text:")
    print("This is a sample response generated from the given prompt.")
