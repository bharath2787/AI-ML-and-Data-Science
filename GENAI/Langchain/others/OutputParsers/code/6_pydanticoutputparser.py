from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="google/gemma-2-2b-it",
    task="text-generation"
)

model = ChatHuggingFace(llm=llm)

class Book(BaseModel):
    title: str = Field(description="Title of the book")
    author: str = Field(description="Fictional author's name")
    genre: str = Field(description="Genre of the book")
    page_count: int = Field(..., description="Number of pages", gt=50)  # must be > 50
# In Pydantic, the ... (three dots) is used as a special value called Ellipsis and it means "this field is required".
parser = PydanticOutputParser(pydantic_object=Book)

prompt = PromptTemplate(
    template=(
        "Create a fictional book based on the theme: {theme}.\n"
        "Respond ONLY with a JSON object matching this format:\n"
        "{format_instruction}\n"
        "Do not include any explanations or extra text."
    ),
    input_variables=["theme"],
    partial_variables={"format_instruction": parser.get_format_instructions()}
)

prompt_str = prompt.invoke({"theme": "Quantum Computing"})

raw_response = model.invoke(prompt_str)
print("Raw LLM output:")
print(raw_response.content)

# result = parser.parse(raw_response.content)
# print("Parsed structured output:")
# print(result)

# chain = prompt | model | parser

# result = chain.invoke({"theme": "Quantum Computing"})
# print(result)