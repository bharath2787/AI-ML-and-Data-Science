# Extract FAQs from product description and then rewrite them in a friendly tone.

from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

# Load HuggingFace model
llm_endpoint = HuggingFaceEndpoint(
    repo_id="google/gemma-2-2b-it",
    task="text-generation"
)

chat_llm = ChatHuggingFace(llm=llm_endpoint)

# Step 1: Extract FAQs from product info
faq_extraction_prompt = PromptTemplate(
    template="""Extract 5 FAQs with answers from the following product description:\n\n{description}""",
    input_variables=["description"]
)

# Step 2: Rewrite FAQs in a more casual, friendly tone
rewrite_prompt = PromptTemplate(
    template="""Rewrite the following FAQs in a friendly, conversational style:\n\n{faqs}""",
    input_variables=["faqs"]
)

# Example product description
product_text = """
Our SmartFit Noise-Cancelling Wireless Earbuds offer up to 30 hours of playback, 
touch controls, water resistance (IPX5), and adaptive noise control for immersive sound. 
Supports fast charging and dual-device connectivity.
"""


parser = StrOutputParser()

chain = faq_extraction_prompt | chat_llm | parser | rewrite_prompt | chat_llm | parser

result = chain.invoke({'description':product_text})

print(result)

