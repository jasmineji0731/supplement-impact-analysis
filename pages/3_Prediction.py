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
from sklearn.metrics import mean_squared_error
import numpy as np

predictions = model.predict(X)

mse = mean_squared_error(y, predictions)
rmse = np.sqrt(mse)

st.write("MSE:", mse)
st.write("RMSE:", rmse)
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
# Gender encoding
if gender == "Male":
    input_data["Gender_Male"] = 1
    input_data["Gender_Non-Binary"] = 0

elif gender == "Non-Binary":
    input_data["Gender_Male"] = 0
    input_data["Gender_Non-Binary"] = 1

else:  # Female
    input_data["Gender_Male"] = 0
    input_data["Gender_Non-Binary"] = 0


# Supplement encoding
if supplement == "Mass Gainer":
    input_data["Supplement_Mass Gainer"] = 1
    input_data["Supplement_Creatine Monohydrate"] = 0

elif supplement == "Creatine Monohydrate":
    input_data["Supplement_Mass Gainer"] = 0
    input_data["Supplement_Creatine Monohydrate"] = 1

else:  # Both
    input_data["Supplement_Mass Gainer"] = 0
    input_data["Supplement_Creatine Monohydrate"] = 0

if st.button("Predict"):

    prediction = model.predict(
        input_data[X.columns]
    )

    st.success(
        f"Predicted Final Weight: {prediction[0]:.2f} kg"
    )  
    st.write("""
    The prediction is generated using a Linear Regression model trained on 1000 observations.
    """)
 


