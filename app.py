import streamlit as st
import requests
import pandas as pd
import os
from dotenv import load_dotenv

load_dotenv()

APP_ID = os.getenv("ADZUNA_APP_ID")
APP_KEY = os.getenv("ADZUNA_APP_KEY")

st.title("Live Job Market Insights Dashboard")

role = st.text_input("Job Role")
location = st.text_input("Location")

if st.button("Search Jobs"):
    if not role or not location:
        st.warning("Please enter both a job role and location.")
    else:
        url = "https://api.adzuna.com/v1/api/jobs/us/search/1"
        params = {
            "app_id": APP_ID,
            "app_key": APP_KEY,
            "what": role,
            "where": location,
            "results_per_page": 20
        }

        response = requests.get(url, params=params)
        data = response.json()
        jobs = data["results"]

        rows = []
        for job in jobs:
            rows.append({
                "Title": job["title"],
                "Company": job["company"]["display_name"],
                "Location": job["location"]["display_name"],
                "Min Salary": job.get("salary_min"),
                "Max Salary": job.get("salary_max")
            })

        df = pd.DataFrame(rows)
        st.dataframe(df)

        st.subheader("Top Hiring Companies")
        st.bar_chart(df["Company"].value_counts())

        st.subheader("Salary Distribution")
        salary_df = df[["Title", "Min Salary"]].dropna()
        salary_df = salary_df.set_index("Title")
        st.bar_chart(salary_df)