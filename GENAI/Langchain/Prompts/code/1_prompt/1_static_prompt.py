from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import streamlit as st


load_dotenv()
model = ChatOpenAI()

st.header("Blog Generator")

user_input = st.text_input("Enter your prompt")
submitBtn = st.button("Genrate")

if submitBtn:

    result = model.invoke(user_input)
    st.write(result.content)

