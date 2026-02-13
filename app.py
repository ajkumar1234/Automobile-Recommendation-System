import streamlit as st
from src.predict import recommend_car

st.set_page_config(page_title="Automobile Recommendation System", layout="centered")

st.title("🚗 Automobile Recommendation System")
st.write("Get the most probable car brand and model based on your budget and fuel preference.")

price = st.number_input(
    "Enter your budget (₹)",
    min_value=100000,
    step=50000
)

fuel_type = st.selectbox(
    "Select fuel type",
    ["Petrol", "Diesel", "CNG", "Electric"]
)

if st.button("Recommend Car"):
    brand, model = recommend_car(price, fuel_type)
    st.success(f"✅ Recommended Brand: **{brand}**")
    st.success(f"🚘 Recommended Model: **{model}**")
