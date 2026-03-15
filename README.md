# Telecom Customer Churn Prediction

This project predicts whether a telecom customer is at risk of churning using a machine learning model.  
The model analyzes customer features such as tenure, monthly charges, and contract type to estimate churn risk.

## Live Application
https://customer-segmentation-ml-5af3encwh2beacpsny3bj8.streamlit.app/

# 📊 Telecom Customer Segmentation & Retention Analysis

## 📌 Project Overview
This project segments telecom customers based on their usage behavior and spending patterns using K-Means clustering. The goal is to identify different customer groups and support data-driven retention strategies.

## 🎯 Objectives
- Identify different types of telecom customers
- Detect high-value and loyal customers
- Identify customers who may leave the service
- Support targeted retention strategies

## ⚙️ Methodology
- Data cleaning and preprocessing
- Feature engineering and feature selection
- Customer segmentation using K-Means clustering
- Deployment of the model using Streamlit

**Final features used in the model:**
- enure
- MonthlyCharges
- TotalCharges
- Contract
- InternetService
- SeniorCitizen

## 📊 Key Customer Segments
**High-Spending New Customers**
- Low tenure
- High monthly charges
- Higher churn risk

**Loyal Customers**
- High tenure
- Stable spending
- Long-term users

**Low Spending Customers**
- Lower monthly charges
- Moderate tenure
- 
## 📈 Business Insights
- **Who should get retention offers?** Customers with high monthly charges but low tenure, as they generate good revenue but may leave early.
- **Who should get early access to new features?** Loyal customers with high tenure and consistent usage, since they are long-term users and valuable to the business.
- **Who is likely to churn no matter what you do?** Customers with very low tenure and low spending, as they show weak engagement with the service.

## 💼 Business Impact
- Helps telecom companies identify valuable customers
- Supports targeted marketing strategies
- Improves customer retention
- Enables data-driven decision making

## 🛠️ Technologies Used
- Python
- Pandas
- Scikit-learn
- K-Means Clustering
- Streamlit
