import streamlit as st
import joblib
import numpy as np

st.title("Churn Prediction App")

st.divider()

st.write("Please enter the values and hit the prediction button to see the prediction")

st.divider()

age = st.number_input("Enter age", min_value=18, max_value=100, value=25)
tenure = st.number_input("Enter tenure", min_value=0, max_value=130, value=10)
monthly_charge = st.number_input("Enter monthly charge", min_value=30, max_value=150)
gender = st.selectbox("Enter gender", ["Male", "Female"])

st.divider()

predict_button = st.button("Predict")

if predict_button:
    # Load the model
    model = joblib.load("model/model.pkl")

    # Make prediction
    gender_selected = 1 if gender == "Female" else 0
    X = [age, gender_selected, tenure, monthly_charge]
    X_array = np.array(X).reshape(1, -1)
    prediction = model.predict(X_array)[0]
    
    predicted = "Yes" if prediction == 1 else "No"
    st.write(f"The prediction is {predicted}")

else:
    st.write("Please enter the values and hit the prediction button")