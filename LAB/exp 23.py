from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
text = input("Enter two sentences separated by |: ")
sentences = text.split("|")
vectorizer = TfidfVectorizer()
matrix = vectorizer.fit_transform(sentences)
score = cosine_similarity(matrix[0], matrix[1])[0][0]
print("Coherence Score:", round(score, 2))
if score > 0.1:
    print("Text is Coherent")
else:
    print("Text is Less Coherent")
