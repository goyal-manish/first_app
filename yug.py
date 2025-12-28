import streamlit as st

st.title("My First Streamlit App 📱")
st.write("Hello! This app is running on mobile 😄")

name = st.text_input("Enter your name")

if st.button("Submit"):
    st.success(f"Welcome, {name} 🎉")
