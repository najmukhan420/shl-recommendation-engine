from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import pandas as pd
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

app = FastAPI()

# Enable CORS for UI
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load data and model
df = pd.read_csv("data/catalog.csv")
model = SentenceTransformer("all-MiniLM-L6-v2")
df["embedding"] = df["combined_text"].apply(lambda x: model.encode(x).tolist())

@app.get("/recommend")
def recommend(query: str):
    query_embedding = model.encode([query])
    scores = cosine_similarity(query_embedding, df["embedding"].tolist())[0]
    top_indices = scores.argsort()[-5:][::-1]
    results = df.iloc[top_indices][["assessment_name", "description"]]
    return results.to_dict(orient="records")
