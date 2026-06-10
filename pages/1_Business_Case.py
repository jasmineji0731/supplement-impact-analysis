import streamlit as st
import pandas as pd

df = pd.read_csv("cleaned_supplement_data.csv")

st.title("Business Case")
st.image(
    "picture.webp",
    caption="Supplement Impact Analysis",
    use_container_width=True
)
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
st.header("Dataset Summary Statistics")
st.subheader("Numerical Variables Summary")

st.dataframe(
    df.describe()
)
st.subheader("Missing Values Analysis")

missing_values = df.isnull().sum()

missing_df = pd.DataFrame({
    "Column": missing_values.index,
    "Missing Values": missing_values.values
})

st.dataframe(missing_df)
total_missing = df.isnull().sum().sum()

st.metric(
    "Total Missing Values",
    total_missing
)
st.subheader("Column Data Types")

dtype_df = pd.DataFrame({
    "Column": df.columns,
    "Data Type": df.dtypes.astype(str)
})

st.dataframe(dtype_df)

st.header("Download Dataset")

csv = df.to_csv(index=False)

st.download_button(
    label="Download Full Dataset",
    data=csv,
    file_name="supplement_dataset.csv",
    mime="text/csv"
)
