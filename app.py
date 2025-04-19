import streamlit as st
from chatbot import load_chatbot

st.set_page_config(page_title="Mental Health Check-In 💬", page_icon="💬")
st.title("💬 Mental Health Check-In Bot")

# Initialize the bot in session state so it persists
if "bot" not in st.session_state:
    st.session_state.bot = load_chatbot()

# Initialize chat history
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Display chat history
for message in st.session_state.chat_history:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Handle user input
user_input = st.chat_input("How are you feeling today?")
if user_input:
    # Add user message to chat and display it
    st.session_state.chat_history.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)
    
    # Get bot response using the conversation chain
    result = st.session_state.bot.predict(input=user_input)
    
    # Extract just the response text from the result
    # The ConversationChain's predict method returns just the text response
    response = result  # The result should already be just the text
    
    # Add bot response to chat and display it
    st.session_state.chat_history.append({"role": "assistant", "content": response})
    with st.chat_message("assistant"):
        st.markdown(response)