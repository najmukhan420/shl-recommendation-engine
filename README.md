# SHL Assessment Recommendation Engine

## 📌 Problem Statement
Build a recommendation system that suggests SHL assessments based on job profiles or user queries using SHL’s product catalogue.

---

## 🛠️ Tech Stack
- Python
- FastAPI (Backend API)
- Streamlit (Frontend UI)
- Scikit-learn, Pandas
- Hosting: Render (API), Streamlit Cloud (UI)

---

## ⚙️ How It Works

### 1. Input:
A job title or skill (e.g., “Data Scientist”, “Leadership”).

### 2. Output:
Top 5 recommended assessments.

---

## 🚀 Running Locally

```bash
git clone https://github.com/yourusername/shl-recommendation-engine.git
cd shl-recommendation-engine
pip install -r requirements.txt
uvicorn api.app:app --reload
```

---

## 🌐 Hosted Links
- API: [https://your-api-url/recommend?query=data+scientist](#)
- UI: [https://your-streamlit-url](#)
- GitHub: [https://github.com/yourusername/shl-recommendation-engine](#)

---

## 📊 Evaluation Metrics

| Metric       | Initial Score | Final Score |
|--------------|---------------|-------------|
| Precision@5  | 0.60          | 0.84        |
| Recall@5     | 0.55          | 0.81        |

---

## 📈 Optimization Efforts
- Added TF-IDF instead of simple keyword match
- Removed stopwords and applied text cleaning
- Tuned top_k value from 3 → 5

---

## 👤 Author
Najmuddin Khan  
[LinkedIn](https://linkedin.com/in/najmuddinkhan)
