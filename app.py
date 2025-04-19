import streamlit as st
from chatbot import load_chatbot
from langchain_core.chat_history import InMemoryChatMessageHistory

st.set_page_config(page_title="ClearMind AI 💬", page_icon="💬")
st.title("💬 ClearMind AI")

# Store memory in session_state so it's persistent
if "chat_memory" not in st.session_state:
    st.session_state.chat_memory = InMemoryChatMessageHistory()

# Define a fixed session ID or generate a unique one if you want multi-session support
session_id = "default"

# Load bot and pass in a function that returns the stored chat memory
bot = load_chatbot(lambda sid: st.session_state.chat_memory)

# Chat input
user_input = st.chat_input("How are you feeling today?")

# Chat history UI display
for msg in st.session_state.chat_memory.messages:
    with st.chat_message("user" if msg.type == "human" else "assistant"):
        st.write(msg.content)

# Handle new user input
if user_input:
    with st.chat_message("user"):
        st.write(user_input)

    response = bot.invoke(
        {"input": user_input},
        config={"configurable": {"session_id": session_id}}
    )
    with st.chat_message("assistant"):
        st.write(response)
