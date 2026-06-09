import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("cleaned_supplement_data.csv")

st.title("Data Visualization")

st.header("Looker Dashboard")
st.image("looker_dashboard.png")

st.header("Initial Weight vs Final Weight")

fig, ax = plt.subplots()

sns.scatterplot(
    data=df,
    x="Initial_WT",
    y="Final_WT",
    ax=ax
)

st.pyplot(fig)
st.header("Final Weight by Supplement")

fig, ax = plt.subplots()

sns.boxplot(
    data=df,
    x="Supplement",
    y="Final_WT",
    ax=ax
)

st.pyplot(fig)
st.header("Final Weight by Supplement")

fig, ax = plt.subplots()

sns.boxplot(
    data=df,
    x="Supplement",
    y="Final_WT",
    ax=ax
)

st.pyplot(fig)
st.header("Business Insights")

st.write("""
1. Combined supplement use produced the highest average final weight.

2. Creatine generated higher strength gains than Mass Gainer.

3. The dataset is balanced across gender groups.
""")

