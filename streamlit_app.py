import streamlit as st
import numpy as np
import joblib

# Load the trained model
model = joblib.load("optimized_xgboost_model.pkl")

# Streamlit UI
st.title("🔥 Calories Burned Prediction App")
st.write("Enter your details below to predict the calories burned during exercise")


# User input fields
age = st.number_input("Age", min_value=20, max_value=79, value=25, step=1)
height = st.number_input("Height (cm)", min_value=153.0, max_value=195.0, value=170.0)
weight = st.number_input("Weight (kg)", min_value=36.00, max_value=123.00, value=70.00)
duration = st.number_input("Exercise Duration (minutes)", min_value=1.00, max_value=30.00, value=30.00, step=1.00)
heart_rate = st.number_input("Heart Rate (bpm)", min_value=67.00, max_value=125.00, value=120.00 , step=1.00)
body_temp = st.number_input("Body Temperature (°C)", min_value=38.0, max_value=42.0, value=37.0)
gender = st.selectbox("Gender", ["Male", "Female"])



# Convert gender to numeric
gender_numeric = 1 if gender == "Male" else 0

# Predict button
if st.button("Predict Calories"):
    # Create input array
    input_data = np.array([[age, height, weight, duration, heart_rate, body_temp, gender_numeric]])
    prediction = model.predict(input_data)[0]
    
    # Display result
    st.success(f"🔥 Estimated Calories Burned: {prediction:.2f} kcal")
