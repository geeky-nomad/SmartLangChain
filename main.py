# This will integrate our code with OpenAI
import os

from config import SmartLandChainEnvLoader
from langchain.llms import OpenAI

import streamlit as st

# set open_api_key
os.environ['OPENAI_API_KEY'] = SmartLandChainEnvLoader().get('OPENAI_API_KEY')

# Streamlit framework
st.title('Langchain demo with OpenAI API')
input_text = st.text_input('Search the product you want')

# OpenAI LLMs
llm = OpenAI(temperature=0.8)
if input_text:
    st.write(llm(input_text))