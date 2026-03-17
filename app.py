import streamlit as st

st.title("AI Healthcare Assistant")

symptom = st.text_input("Enter your symptom:")

if st.button("Predict"):
    if symptom:
        st.success(f"You entered: {symptom}. Please consult a doctor.")
    else:
        st.warning("Please enter a symptom")
