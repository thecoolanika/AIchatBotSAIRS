import os
from langchain.chat_models import ChatGoogleGenerativeAI
from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory
from langchain.prompts import ChatPromptTemplate, SystemMessagePromptTemplate
from dotenv import load_dotenv

load_dotenv()

def load_chatbot():
    system_prompt = open("prompts/system_prompt.txt", "r").read()
    memory = ConversationBufferMemory()

    llm = ChatGoogleGenerativeAI(
        model="gemini-pro",  # or "gemini-1.5-pro" if you want latest
        google_api_key=os.getenv("GOOGLE_API_KEY"),
        temperature=0.7
    )

    chat_prompt = ChatPromptTemplate.from_messages([
        SystemMessagePromptTemplate.from_template(system_prompt)
    ])

    conversation = ConversationChain(
        llm=llm,
        memory=memory,
        prompt=chat_prompt
    )

    return conversation
