import streamlit as st
import requests

st.title("SHL Assessment Recommendation Engine")
query = st.text_input("Enter Job Role or Skill:")

if st.button("Recommend"):
    response = requests.get(f"https://your-api-url/recommend?query={query}")
    results = response.json()
    for item in results:
        st.subheader(item["assessment_name"])
        st.write(item["description"])
