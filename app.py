import streamlit as st
from chatbot import load_chatbot

st.set_page_config(page_title="Mental Health Check-In 💬", page_icon="💬")
st.title("💬 Mental Health Check-In Bot")

bot = load_chatbot()

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

user_input = st.chat_input("How are you feeling today?")

if user_input:
    with st.spinner("Thinking..."):
        response = bot.run(user_input)
        st.session_state.chat_history.append(("user", user_input))
        st.session_state.chat_history.append(("bot", response))

for role, message in st.session_state.chat_history:
    if role == "user":
        with st.chat_message("user"):
            st.write(message)
    else:
        with st.chat_message("assistant"):
            st.write(message)
