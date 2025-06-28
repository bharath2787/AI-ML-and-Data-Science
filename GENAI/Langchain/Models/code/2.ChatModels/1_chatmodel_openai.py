# Import the ChatOpenAI wrapper from LangChain
# This is used to interact with chat-based models like GPT-4
from langchain_openai import ChatOpenAI

# Import dotenv to load environment variables (e.g., your OpenAI API key)
from dotenv import load_dotenv

# Load variables from the .env file into the environment
load_dotenv()

# Initialize the ChatOpenAI model
# - model: specifies which model to use (e.g., 'gpt-4')
# - temperature: controls creativity (0 = factual, 1.5 = very creative)
# - max_completion_tokens: limits the length of the response (10 tokens = very short)
model = ChatOpenAI(model='gpt-4', temperature=0, max_completion_tokens=50)

# You can also test more creativity by using a higher temperature:
# model = ChatOpenAI(model='gpt-4', temperature=1.5, max_completion_tokens=10)

# Send a prompt to the model and receive a structured response
response = model.invoke("Write a 3 line poem on India")

# Print the full response object (contains metadata and content)
print(response)

# Print only the main content (the model's actual text output)
print(response.content)
