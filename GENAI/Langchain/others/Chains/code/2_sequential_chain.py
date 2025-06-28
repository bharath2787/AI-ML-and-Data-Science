# First, generate a detailed product description based on a product name, then create a short FAQ section from that description to assist customer support or ecommerce listings.

from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

# Step 1: Generate product description
description_prompt = PromptTemplate(
    template="Write a comprehensive product description for the product named: {product_name}",
    input_variables=["product_name"]
)

# Step 2: Generate FAQ from product description
faq_prompt = PromptTemplate(
    template="Based on the following product description, generate 4 frequently asked questions and answers:\n\n{description}",
    input_variables=["description"]
)

model = ChatOpenAI()
parser = StrOutputParser()

# Chain: Product description → FAQ generation
chain = description_prompt | model | parser | faq_prompt | model | parser

# Run
result = chain.invoke({'product_name': 'Wireless Noise Cancelling Headphones'})

print(result)

chain.get_graph().print_ascii()
