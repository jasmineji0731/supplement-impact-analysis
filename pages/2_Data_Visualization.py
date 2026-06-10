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
st.subheader("Relationship Between Numerical Variables")
st.header("Correlation Heatmap")

numeric_df = df.select_dtypes(include=["number"])

fig, ax = plt.subplots(figsize=(8,6))

sns.heatmap(
    numeric_df.corr(),
    annot=True,
    cmap="coolwarm",
    fmt=".2f",
    ax=ax
)

st.pyplot(fig)
st.subheader("Correlation with Final Weight")

corr_table = (
    numeric_df.corr()["Final_WT"]
    .sort_values(ascending=False)
)

st.dataframe(corr_table)

st.header("Business Insights")

st.markdown("""
### 1. Combined Supplement Usage Delivers the Best Overall Results

Participants who used a combination of supplements achieved both the highest average final weight and the highest average strength gain. Compared with participants who used only one supplement, the combined approach appears to provide more comprehensive fitness benefits.

### 2. Creatine Monohydrate Is More Effective for Strength Development

The analysis shows that participants using Creatine Monohydrate experienced greater average strength gains than those using Mass Gainer. This suggests that Creatine may be the better option when the primary goal is improving muscular strength and athletic performance.

### 3. Mass Gainer Supports Weight Gain

Participants using Mass Gainer achieved relatively high final body weights, indicating that the supplement is effective for weight gain. However, the associated strength gains were lower than those observed among Creatine users and participants using both supplements.
""")





