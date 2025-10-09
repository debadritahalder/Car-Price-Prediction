import streamlit as st
import pandas as pd
import joblib


model = joblib.load("models/ridge_model.pkl")

st.title("Car Price Prediction")
st.write("Enter the details to predict the price of a car.")

Entry_price = st.number_input("Entry Price ($)", min_value=500, max_value=100000, value=20000)
Engine_size = st.number_input("Engine Size (L)", min_value=0.5, max_value=8.0, value=2.0, step=0.1)
Average_mpg = st.number_input("Average MPG", min_value=5, max_value=500, value=30)
Engine_power = st.number_input("Engine Power", min_value=50, max_value=1000, value=150)
Average_Sales = st.number_input("Average Sales", min_value=0, max_value=1000000, value=5000)

input_data = pd.DataFrame({
    "Entry Price ($)": [Entry_price],
    "Engine Size (L)": [Engine_size],
    "Average MPG": [Average_mpg],
    "Engine Power": [Engine_power],
    "Average Sales": [Average_Sales]
})

if st.button("Predict Price"):
    prediction = model.predict(input_data)[0]
    st.success(f"Estimated Car Price: ${prediction:,.2f}")