import streamlit as st
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate, load_prompt
from dotenv import load_dotenv

# Load environment variables (e.g., OpenAI key)
load_dotenv()

# Initialize model
model = ChatOpenAI()

# App UI
st.title(" Blog Simplifier Tool")

blog_title = st.selectbox(
    "Select Blog Title", 
    [
        "Understanding Transformers in NLP", 
        "How Convolutional Neural Networks Work", 
        "An Introduction to Reinforcement Learning", 
        "What is Prompt Engineering?"
    ]
)

audience_level = st.selectbox(
    "Choose Audience Level", 
    ["Complete Beginner", "Intermediate Student", "High School CS Student"]
)

tone_input = st.selectbox(
    "Select Explanation Tone", 
    ["Friendly", "Professional", "Casual"]
)

output_format = st.selectbox(
    "Choose Output Format", 
    ["Bullet Points", "Narrative Explanation", "Step-by-Step Guide"]
)

# Load the saved template
template = load_prompt("explain_blog_template.json")

# Run when button clicked
if st.button("Generate Explanation"):
    chain = template | model
    result = chain.invoke({
        "blog_title": blog_title,
        "audience_level": audience_level,
        "tone_input": tone_input,
        "output_format": output_format
    })
    st.markdown("###  Explanation")
    st.write(result.content)
