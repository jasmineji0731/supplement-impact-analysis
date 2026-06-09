import streamlit as st
import pandas as pd

df = pd.read_csv("cleaned_supplement_data.csv")

st.title("Business Case")

st.header("Problem Statement")

st.write("""
Many people use supplements to improve fitness outcomes, but it can be difficult
to estimate the results they will achieve.

This project uses Linear Regression to predict a participant's Final Weight based on:
- Age
- Gender
- Supplement Type
- Duration (Weeks)
- Initial Weight
- Strength Gain
""")

st.header("Dataset Overview")

st.write(f"Rows: {df.shape[0]}")
st.write(f"Columns: {df.shape[1]}")

st.dataframe(df.head())
