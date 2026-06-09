import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("cleaned_supplement_data.csv")

st.title("Data Visualization")

st.header("Looker Dashboard")
import streamlit.components.v1 as components
st.header("Interactive Looker Dashboard")

components.iframe(
    "https://datastudio.google.com/embed/reporting/e395bc86-9c7f-46fb-8193-a544b88365c5/page/7yX0F",
    height=800,
    scrolling=True
)



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

