# Import the OpenAI wrapper from LangChain
from langchain_openai import OpenAI

# Import the dotenv loader to read environment variables (like your OpenAI API key)
from dotenv import load_dotenv

# Load environment variables from a .env file (required for accessing OpenAI)
load_dotenv()

# Initialize the OpenAI language model (LLM) with the desired model name
# 'gpt-3.5-turbo-instruct' is an instruction-tuned model that understands direct prompts
# https://platform.openai.com/docs/models/gpt-3.5-turbo
llm = OpenAI(model='gpt-3.5-turbo-instruct')

# Use the LLM to get an answer for the given prompt
response = llm.invoke("What is the capital of India")

# Print the result to the console
print(response)
