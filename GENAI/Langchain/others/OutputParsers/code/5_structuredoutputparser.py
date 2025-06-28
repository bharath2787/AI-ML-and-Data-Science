from dotenv import load_dotenv
from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace
from langchain_core.prompts import PromptTemplate
from langchain.output_parsers import ResponseSchema, StructuredOutputParser

# Load environment variables (for HuggingFace token, etc.)
load_dotenv()

# Initialize the HuggingFace language model
gemma_model = HuggingFaceEndpoint(
    repo_id="google/gemma-2-2b-it",
    task="text-generation"
)
chat_interface = ChatHuggingFace(llm=gemma_model)

# Define the structure of the expected output
insight_schema = [
    ResponseSchema(name="insight_1", description="First key insight related to the subject"),
    ResponseSchema(name="insight_2", description="Second key insight"),
    ResponseSchema(name="insight_3", description="Third key insight"),
]

# Generate parser using the schema
insight_parser = StructuredOutputParser.from_response_schemas(insight_schema)

# Compose the instruction prompt
insight_prompt = PromptTemplate(
    template="""
You're an expert educator. Provide exactly 3 noteworthy insights on the topic below:
Topic: {concept}

{format_guidelines}
""",
    input_variables=["concept"],
    partial_variables={"format_guidelines": insight_parser.get_format_instructions()}
)

# print(insight_prompt.invoke({"concept": "Quantum Computing"}))
# Build the flow
workflow = insight_prompt | chat_interface | insight_parser

# Invoke the chain with a sample topic
response = workflow.invoke({"concept": "Quantum Computing"})

# Output the structured result
print(response)
