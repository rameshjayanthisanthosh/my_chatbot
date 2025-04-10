import streamlit as st
from chat_engine import get_response

st.set_page_config(page_title="My Chatbot")

st.title("🧠 My AI Chatbot")
st.write("Ask me anything!")

user_input = st.text_input("You:", "")

if user_input:
    response = get_response(user_input)
    st.write("🤖:", response)
