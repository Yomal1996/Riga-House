# -*- coding: utf-8 -*-
"""app

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1oqr6_8KFcb0DBXi48Bn9HDXNEU8Bg2oF
"""

import streamlit as st
import pandas as pd
import joblib

# Load model and encoders
model = joblib.load("model.pkl")
encoders = joblib.load("encoders.pkl")

st.title("🏡 Riga House Price Predictor")

# User Inputs
district = st.selectbox("District:", encoders["district"].classes_)
area = st.number_input("Area (m²):", min_value=10, value=50)
rooms = st.selectbox("Number of Rooms:", encoders["rooms"].classes_)
house_type = st.selectbox("House Type:", encoders["house_type"].classes_)
condition = st.selectbox("Condition:", encoders["condition"].classes_)

# Prediction
if st.button("Predict Price"):
    input_data = pd.DataFrame([{
        "district": encoders["district"].transform([district])[0],
        "area": area,
        "rooms": encoders["rooms"].transform([rooms])[0],
        "house_type": encoders["house_type"].transform([house_type])[0],
        "condition": encoders["condition"].transform([condition])[0]
    }])

    prediction = model.predict(input_data)[0]
    st.success(f"💶 Predicted Price: €{prediction:,.2f}")