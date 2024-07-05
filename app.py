import streamlit as st
import requests

st.title("Ask Gemma!")
user_input = st.text_input("Ask a question:")

if st.button("Send"):
    if user_input:
        response = requests.post("http://localhost:8000/generate_text/", json={"question": user_input})
        if response.status_code == 200:
            answer = response.json()['answer']
            st.write("BOT:", answer)
        else:
            st.error("Failed to get an answer from the backend.")
    else:
        st.error("Please enter a question.")
