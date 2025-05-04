import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

class SHLRecommender:
    def __init__(self, data_path):
        self.data = pd.read_csv(data_path)
        self.vectorizer = TfidfVectorizer()
        self.tfidf_matrix = self.vectorizer.fit_transform(self.data['description'])

    def recommend(self, query, top_k=5):
        query_vec = self.vectorizer.transform([query])
        similarity = cosine_similarity(query_vec, self.tfidf_matrix)
        top_indices = similarity[0].argsort()[-top_k:][::-1]
        return self.data.iloc[top_indices][['assessment_name', 'description']]
