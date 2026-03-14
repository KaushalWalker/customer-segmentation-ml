import streamlit as st
import pandas as pd
import joblib

# Load model and scaler
model = joblib.load("kmeans_model.joblib")
scaler = joblib.load("scaler.joblib")

# Streamlit page config
st.set_page_config(page_title="Telecom Customer Segmentation", layout="centered")
st.title("📊 Telecom Customer Segmentation App")
st.write("This app predicts the **customer segment** based on service usage, spending, and tenure.")
st.header("Enter Customer Details 📑")

# Inputs
tenure = st.number_input("Tenure (in months)", min_value=0, max_value=120, value=12)
monthly = st.number_input("Monthly Charges", min_value=0.0, value=50.0, step=0.1)
total = st.number_input("Total Charges", min_value=0.0, value=500.0, step=0.1)
contract = st.selectbox("Contract Type", ["Month-to-month", "One year", "Two year"])
internet = st.selectbox("Internet Service", ["DSL", "Fiber optic", "No"])
senior = st.selectbox("Senior Citizen", [0, 1])

# Encode categorical variables
contract_mapping = {"Month-to-month": 0, "One year": 1, "Two year": 2}
internet_mapping = {"DSL": 0, "Fiber optic": 1, "No": 2}

contract_encoded = contract_mapping[contract]
internet_encoded = internet_mapping[internet]

# Cap extreme values based on typical training data
max_monthly = 200
max_total = 8000
max_tenure = 72

if monthly > max_monthly:
    st.warning(f"Monthly Charges are unusually high (capped at {max_monthly}).")
    monthly = max_monthly
if total > max_total:
    st.warning(f"Total Charges are unusually high (capped at {max_total}).")
    total = max_total
if tenure > max_tenure:
    st.warning(f"Tenure is unusually long (capped at {max_tenure}).")
    tenure = max_tenure

# Predict Button
if st.button("Predict Customer Segment"):

    # Prepare numeric input as pandas DataFrame
    input_data = pd.DataFrame({
        "tenure": [tenure],
        "MonthlyCharges": [monthly],
        "TotalCharges": [total],
        "Contract": [contract_encoded],
        "InternetService": [internet_encoded],
        "SeniorCitizen": [senior]
    })

    try:
        # Scale data
        scaled_data = scaler.transform(input_data)

        # Predict cluster
        cluster = int(model.predict(scaled_data)[0])

        # -------------------------------
        # Step 1: Override cluster for loyal customers
        # -------------------------------
        if tenure >= 36 and monthly >= 70 and total >= 3000:
            cluster = 2  # Force loyal customer cluster

        # Segment mapping
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

    except Exception as e:
        st.error(f"Prediction failed: {e}")