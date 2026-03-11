import streamlit as st
import pandas as pd
import joblib

# Load model and scaler
model = joblib.load("kmeans_model.joblib")
scaler = joblib.load("scaler.joblib")

st.title("Telecom Customer Churn Risk Prediction")

st.header("Enter Customer Details📑")

# Inputs
tenure = st.number_input("Tenure (months)", min_value=0)

monthly = st.number_input("Monthly Charges", min_value=0.0)

total = st.number_input("Total Charges", min_value=0.0)

senior = st.selectbox("Senior Citizen", [0,1])

contract = st.selectbox(
    "Contract Type",
    ["Month-to-month","One year","Two year"]
)

internet = st.selectbox(
    "Internet Service",
    ["DSL","Fiber optic","No"]
)

# Encoding (same as training)
contract_map = {
    "Month-to-month":0,
    "One year":1,
    "Two year":2
}

internet_map = {
    "DSL":0,
    "Fiber optic":1,
    "No":2
}

contract = contract_map[contract]
internet = internet_map[internet]

# Predict
if st.button("Check Churn Risk"):

    input_data = pd.DataFrame([[
        tenure,
        monthly,
        total,
        contract,
        internet,
        senior
    ]],
    columns=[
        "tenure",
        "MonthlyCharges",
        "TotalCharges",
        "Contract",
        "InternetService",
        "SeniorCitizen"
    ])

    scaled_data = scaler.transform(input_data)

    cluster = model.predict(scaled_data)[0]

    # Interpret clusters as churn risk
    churn_map = {
        0: "Low Churn Risk",
        1: "Medium Churn Risk",
        2: "High Churn Risk"
    }

    st.success(f"Prediction: {churn_map[cluster]}")