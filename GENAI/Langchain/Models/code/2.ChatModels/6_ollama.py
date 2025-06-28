from langchain_community.chat_models import ChatOllama

# Load the local Ollama model
model = ChatOllama(model="mistral")  # you can also use "mistral", "gemma", etc.

# Make a query
response = model.invoke("What is the capital of India?")

# Print the result
print(response.content)
