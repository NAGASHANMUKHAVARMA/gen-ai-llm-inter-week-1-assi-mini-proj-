import streamlit as st

st.title("AI Writing Assistant")

option = st.selectbox(
    "Choose",
    ["Blog", "Email", "Code Explanation", "Social Media"]
)

topic = st.text_input("Enter topic")

if st.button("Generate"):
    st.write("Task:", option)
    st.write("Topic:", topic)
