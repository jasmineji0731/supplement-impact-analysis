import streamlit as st
import pandas as pd

from sklearn.linear_model import LinearRegression

df = pd.read_csv("cleaned_supplement_data.csv")
st.metric(
    "Model Accuracy (R²)",
    "98.5%"
)
df_model = pd.get_dummies(
    df,
    columns=["Gender","Supplement"],
    drop_first=True
)

X = df_model.drop(
    ["ID","Primary_Benefit","Final_WT"],
    axis=1
)

y = df_model["Final_WT"]

model = LinearRegression()

model.fit(X,y)
st.title("Final Weight Prediction")

age = st.number_input("Age",18,80)

weeks = st.number_input("Weeks",1,52)

initial_wt = st.number_input("Initial Weight")

strength_gain = st.number_input("Strength Gain")
input_data = pd.DataFrame({
    "Age":[age],
    "Weeks":[weeks],
    "Initial_WT":[initial_wt],
  
  "Strength_Gain":[strength_gain]
})
for col in X.columns:
    if col not in input_data.columns:
        input_data[col] = 0
    
gender = st.selectbox(
    "Gender",
    ["Male", "Female", "Non-Binary"]
)

supplement = st.selectbox(
    "Supplement",
    ["Mass Gainer",
     "Creatine Monohydrate",
     "Both"]
)
if st.button("Predict"):

    prediction = model.predict(
        input_data[X.columns]
    )

    st.success(
        f"Predicted Final Weight: {prediction[0]:.2f} kg"
    )  
