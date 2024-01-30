import os
import time
import streamlit as st
from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate, ChatPromptTemplate
from langchain.chains.llm import LLMChain
from langchain_core.messages import HumanMessage, AIMessage

from dotenv import load_dotenv
load_dotenv()


class TherapyChatbot:
    def __init__(self):
        self.llm = ChatOpenAI()
        self.prompt = ChatPromptTemplate.from_messages(
            [
                ('system',
                 "You are a therapy chatbot. Please provide a helpful and empathetic response to the user's input: {input}"),
                ('human', "{input}")
            ]
        )
        self.chain = LLMChain(llm=self.llm, prompt=self.prompt)

    def generate_response(self, input):
        response = self.chain.run(input=input)
        return response


def main():
    st.set_page_config(page_title="Therapy Chatbot", page_icon="💬")
    st.header("Therapy Chatbot")
    st.markdown('---')

    st.sidebar.markdown(
        "Welcome to our therapy chatbot. Feel free to share your thoughts and feelings, and we'll do our best to provide a helpful and empathetic response.")

    chatbot = TherapyChatbot()

    # Initialize chat history
    if "messages" not in st.session_state:
        st.session_state.messages = []

    # Display chat messages from history on app rerun
    for message in st.session_state.messages:
        with st.chat_message(message.role):
            st.markdown(message.content)

    if user_input := st.chat_input('You: '):
        # Add user message to chat history
        st.session_state.messages.append(
            HumanMessage(content=user_input))

        # Display user message in chat message container
        with st.chat_message('user'):
            st.markdown(user_input)

        # Display assistant response in chat message container
        with st.chat_message("therapist"):
            message_placeholder = st.empty()
            full_response = ""

            bot_response = chatbot.generate_response(user_input)
            for response_chunk in bot_response.split():
                full_response += response_chunk + " "
                time.sleep(0.05)
                message_placeholder.markdown(full_response + "|")
            message_placeholder.markdown(full_response)
        # Add assistant response to chat history
        st.session_state.messages.append(
            AIMessage(content=full_response))


if __name__ == "__main__":
    main()
