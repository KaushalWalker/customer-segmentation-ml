import streamlit as st
import pandas as pd
import joblib

# Load model and scaler
model = joblib.load("kmeans_model.joblib")
scaler = joblib.load("scaler.joblib")

st.set_page_config(page_title="Telecom Customer Segmentation", layout="centered")

st.title("📊 Telecom Customer Segmentation App")

st.write(
    "This app predicts the **customer segment** based on service usage, spending, and tenure."
)

st.header("Enter Customer Details 📑")

# Inputs
tenure = st.number_input("Tenure (in months)", min_value=0, max_value=120, value=12)
monthly = st.number_input("Monthly Charges", min_value=0.0, value=50.0, step=0.1)
total = st.number_input("Total Charges", min_value=0.0, value=500.0, step=0.1)
contract = st.selectbox("Contract Type", ["Month-to-month", "One year", "Two year"])
internet = st.selectbox("Internet Service", ["DSL", "Fiber optic", "No"])
senior = st.selectbox("Senior Citizen", [0, 1])

# Optional: Check for unrealistic input
if monthly == 0:
    st.warning("Monthly charges cannot be zero for a valid prediction.")

# Predict Button
if st.button("Predict Customer Segment"):

    input_data = pd.DataFrame({
        "tenure": [tenure],
        "MonthlyCharges": [monthly],
        "TotalCharges": [total],
        "Contract": [contract],
        "InternetService": [internet],
        "SeniorCitizen": [senior]
    })

    scaled_data = scaler.transform(input_data)
    cluster = int(model.predict(scaled_data)[0])

    segment_map = {
        0: "Moderate and Stable Users",
        1: "High-Spending but New Customers",
        2: "High-Value Loyal Customers",
        3: "Low-Usage Budget Customers"
    }

    description_map = {
        0: "These customers have average spending and stable usage. Good candidates for upselling services.",
        1: "These customers spend a lot but have short tenure. Retention strategies are important.",
        2: "These are loyal long-term customers with high spending and strong service adoption.",
        3: "These customers use basic services with low spending. Marketing campaigns may increase engagement."
    }

    st.success(f"### Predicted Segment: {segment_map[cluster]}")
    st.info(description_map[cluster])
    st.write(f"Cluster Number: **{cluster}**")
    