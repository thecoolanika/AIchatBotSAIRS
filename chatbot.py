import os
from dotenv import load_dotenv
from langchain.memory import ConversationBufferMemory
from langchain.prompts import ChatPromptTemplate, SystemMessagePromptTemplate, HumanMessagePromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough, RunnableWithMessageHistory
from langchain_core.chat_history import InMemoryChatMessageHistory

load_dotenv()

def load_chatbot():
    system_prompt = open("prompts/system_prompt.txt", "r").read()

    llm = ChatGoogleGenerativeAI(
        model="gemini-pro",
        google_api_key=os.getenv("GOOGLE_API_KEY"),
        temperature=0.7,
        api_version="v1" 
    )

    memory = ConversationBufferMemory(
        return_messages=True,
        memory_key="history",
        input_key="input"
    )

    prompt = ChatPromptTemplate.from_messages([
        SystemMessagePromptTemplate.from_template(system_prompt),
        HumanMessagePromptTemplate.from_template("{input}")
    ])

    chain = prompt | llm | StrOutputParser()

    def get_session_history(session_id: str):
        return InMemoryChatMessageHistory()

    conversation = RunnableWithMessageHistory(
        runnable=chain,
        get_session_history=get_session_history,
        input_messages_key="input",
        history_messages_key="history"
    )

    return conversation
