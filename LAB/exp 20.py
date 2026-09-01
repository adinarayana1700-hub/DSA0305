from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
documents = [
    "Python is a programming language",
    "Java is a programming language",
    "Python is easy to learn"
]
query = input("Enter search query: ")
vectorizer = TfidfVectorizer()
matrix = vectorizer.fit_transform(documents + [query])
scores = cosine_similarity(matrix[-1], matrix[:-1]).flatten()
print("Document Ranking:")
ranking = scores.argsort()[::-1]
for i in ranking:
    print("Document", i + 1, "Score:", round(scores[i], 3))
