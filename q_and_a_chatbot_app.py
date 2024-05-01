# Q & A Chatbot
from langchain_openai import OpenAI

import os

from dotenv import load_dotenv

load_dotenv() # will load all the environemnt variables from .env

import streamlit as st

# 1. Function to load the OpenAI model and get response
def get_openai_response(question):
    llm = OpenAI(openai_api_key=os.getenv("OPENAI_API_KEY"), model_name="gpt-3.5-turbo-instruct", temperature=0.5)
    return llm(question)
    
# 2. Initialize the Streamlit App
st.set_page_config(page_title="Q&A Chatbot Demo")

st.header("Langchain Application")
    
input = st.text_input("The input: ", key="input")
response = get_openai_response(input)

submit = st.button("Ask the question")

# If button is clicked
if submit:
    st.subheader("The response is:")
    st.write(response)