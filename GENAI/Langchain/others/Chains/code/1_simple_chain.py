from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

# Load environment variables from .env file (e.g., OpenAI API key)
load_dotenv()

# Define the prompt template to generate top 5 interview questions for a given topic
prompt = PromptTemplate(
    template='Generate top 5 interview questions on {topic}',
    input_variables=['topic']
)

# Initialize the OpenAI language model wrapper
model = ChatOpenAI()

# Initialize a parser to extract the plain text string output from the model's response
parser = StrOutputParser()

# Create a simple chain by piping the prompt through the model and then the parser
chain = prompt | model | parser

# Invoke the chain with the specific topic input
result = chain.invoke({'topic': 'MachineLearning'})

# Print the generated interview questions
print(result)

# Display the chain's execution graph in ASCII format for visualization
chain.get_graph().print_ascii()
