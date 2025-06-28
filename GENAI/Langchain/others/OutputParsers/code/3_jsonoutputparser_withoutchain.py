from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser

load_dotenv()

# Define the model
llm = HuggingFaceEndpoint(
    repo_id="google/gemma-2-2b-it",
    task="text-generation"
)

model = ChatHuggingFace(llm=llm)

parser = JsonOutputParser()

template = PromptTemplate(
    template='Give me top 5 interview questions on  {topic} \n {format_instruction}',
    input_variables=['topic'],
    partial_variables={'format_instruction': parser.get_format_instructions()}  # this is called partial variable becuase its filled before runtime, not given by user
)

prompt = template.invoke({'topic':'Neural Networks'})

print(f"This is the prompt : \n {prompt}")

result = model.invoke(prompt)

print(f"This is the output of LLM : \n {result}")

final_result = parser.parse(result.content)

print(f"This is the final parsed ouput : \n {final_result}")

