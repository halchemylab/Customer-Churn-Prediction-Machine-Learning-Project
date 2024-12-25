import streamlit as st
import joblib
import numpy as np

st.title("Churn Prediction App")

st.divider()

st.write("Please enter the values and hit the prediction button to see the prediction")

st.divider()

age = st.number_input("Enter age", min_value=18, max_value=100, value=25)
monthlycharge = st.number_input("Enter monthly charge", min_value=30, max_value=150)
tenure = st.number_input("Enter tenure", min_value=0, max_value=130, value=10)
gender = st.selectbox("Enter gender", ["Male", "Female"])

st.divider()