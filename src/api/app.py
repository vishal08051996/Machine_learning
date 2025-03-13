import streamlit as st
import numpy as np
import tensorflow as tf
import os

# Load the trained model
MODEL_PATH = "models/ann_model.h5"

st.title("🏗️ Construction Strength Prediction")

if os.path.exists(MODEL_PATH):
    model = tf.keras.models.load_model(MODEL_PATH)
    st.success("✅ Model Loaded Successfully!")
else:
    st.error("❌ Model file not found! Train and save the model first.")
    st.stop()

st.write("Enter the input values below to predict building strength:")

# User input fields
cement = st.number_input("Cement (kg)", min_value=0.0, value=200.0)
slag = st.number_input("Slag (kg)", min_value=0.0, value=50.0)
ash = st.number_input("Ash (kg)", min_value=0.0, value=30.0)
water = st.number_input("Water (kg)", min_value=0.0, value=400.0)
superplastic = st.number_input("Superplasticizer (kg)", min_value=0.0, value=20.0)
coarseagg = st.number_input("Coarse Aggregate (kg)", min_value=0.0, value=1000.0)
fineagg = st.number_input("Fine Aggregate (kg)", min_value=0.0, value=800.0)
age = st.number_input("Age (days)", min_value=1, value=28)

# Prediction button
if st.button("Predict Strength"):
    input_data = np.array([[cement, slag, ash, water, superplastic, coarseagg, fineagg, age]])
    prediction = model.predict(input_data)
    strength = prediction[0][0]
    st.success(f"🏠 **Predicted Strength: {strength:.2f} MPa**")
