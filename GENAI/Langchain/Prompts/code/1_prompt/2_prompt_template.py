import streamlit as st
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv

# Load environment variables (e.g., OpenAI key)
load_dotenv()

# Define the prompt template inline
template = PromptTemplate(
    template="""
You are an expert educator. Convert the blog titled "{blog_title}" into a beginner-friendly explanation.

Audience Level: {audience_level}  
Tone: {tone_input}  
Target Format: {output_format}

Guidelines:
1. Simplify jargon using everyday language or analogies.  
2. Where applicable, include code snippets or diagrams to explain concepts.  
3. Highlight real-world applications or use-cases.  
4. If certain parts of the blog are ambiguous or missing, clearly state: "Details not provided."

Ensure the explanation is accessible to someone new to the topic and matches the selected tone and format.
""",
    input_variables=["blog_title", "audience_level", "tone_input", "output_format"],
    validate_template=True
)

# Initialize the LLM
model = ChatOpenAI( max_tokens=300 )

# Streamlit UI
st.title(" Blog Generator App")

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

# Format prompt first
prompt_text = template.invoke({
    "blog_title": blog_title,
    "audience_level": audience_level,
    "tone_input": tone_input,
    "output_format": output_format
})


# Run when button clicked
if st.button("Generate Explanation"):
    result = model.invoke(prompt_text)

    st.markdown("### Explanation")
    st.write(result.content)
