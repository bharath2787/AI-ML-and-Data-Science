from langchain_huggingface import HuggingFacePipeline
from transformers import pipeline
from dotenv import load_dotenv
import os

load_dotenv()

# Create a pipeline directly using transformers (LangChain will wrap this)
pipe = pipeline(
    task='text-generation',
    model='TinyLlama/TinyLlama-1.1B-Chat-v1.0',
)

# Wrap the pipeline for LangChain
llm = HuggingFacePipeline(pipeline=pipe)

# Directly invoke
response = llm.invoke("Question: What is the capital of India? Answer:")
print(response)
