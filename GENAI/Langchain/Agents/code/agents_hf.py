# from langchain_community.chat_models import ChatOllama
from langchain_huggingface import HuggingFacePipeline
from transformers import pipeline
from langchain_community.utilities import GoogleSerperAPIWrapper

from langchain_core.tools import tool
import requests
from dotenv import load_dotenv
from langchain.tools import Tool

from langchain_community.tools import DuckDuckGoSearchRun
load_dotenv()

search_tool = DuckDuckGoSearchRun()
# search = GoogleSerperAPIWrapper()

# search_tool = Tool(
#     name="google_search",
#     func=search.run,
#     description="Useful for answering questions by searching the web using Google Serper."
# )
@tool
def get_weather_data(city: str) -> str:
  """
  This function fetches the current weather data for a given city
  """
  url =  f"https://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&appid=fdfb4aae850e1a7e86de77674a21bfbf"

  response = requests.get(url)

  return response.json()

pipe = pipeline(
    task="text-generation",
    model="mistralai/Mistral-7B-Instruct-v0.2",  # ✅ or try Nous-Hermes, Llama-3 etc.
    max_new_tokens=512,
    temperature=0.7,
    return_full_text=False
)

# Wrap it for LangChain
llm = HuggingFacePipeline(pipeline=pipe)


from langchain.agents import create_react_agent, AgentExecutor
from langchain import hub

# Step 2: Pull the ReAct prompt from LangChain Hub
prompt = hub.pull("hwchase17/react")  # pulls the standard ReAct agent prompt

# Step 3: Create the ReAct agent manually with the pulled prompt
agent = create_react_agent(
    llm=llm,
    tools=[search_tool, get_weather_data],
    prompt=prompt
)

# Step 4: Wrap it with AgentExecutor
agent_executor = AgentExecutor(
    agent=agent,
    tools=[search_tool, get_weather_data],
    verbose=True,
    handle_parsing_errors =True
)

# Step 5: Invoke
response = agent_executor.invoke({"input": "Find the capital of Andhra Pradesh, then find it's current weather condition"})
print(response)

print(response['output'])

