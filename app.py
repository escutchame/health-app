import streamlit as st
import pickle
import numpy as np

# Load trained model
model = pickle.load(open("Activity_model.pkl", "rb"))

st.title("🏋️ Activity Level Prediction")

# Collect user input
age = st.number_input("Enter your age", min_value=10, max_value=100, step=1, format="%d")
gender = st.selectbox("Select your gender", ("Male", "Female"))
steps = st.number_input("Enter steps count", min_value=0, max_value=30000, step=100, format="%d")
heart_rate = st.number_input("Enter heart rate", min_value=40, max_value=220, step=1, format="%d")
calories = st.number_input("Enter calories burned", min_value=0, max_value=5000, step=10, format="%d")
duration = st.number_input("Enter exercise duration (minutes)", min_value=0, max_value=180, step=5, format="%d")
temperature = st.number_input("Enter temperature (°C)", min_value=15, max_value=45, step=1)
location = st.selectbox("Select your location", ("Indoor", "Outdoor"))

# Encode inputs
gender_encoded = 1 if gender == "Male" else 0
location_encoded = 1 if location == "Outdoor" else 0

# Predict button
if st.button("Predict"):
    input_data = np.array([[steps, heart_rate, calories, duration, temperature, gender_encoded, age, location_encoded]])
    prediction = model.predict(input_data)[0]

    level_map = {0: "Low", 1: "Moderate", 2: "High"}
    
    st.subheader("Prediction Result")
    st.success(f"🏆 Predicted Activity Level: {level_map[prediction]}")
