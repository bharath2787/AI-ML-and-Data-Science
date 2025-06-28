# from langchain_community.chat_models import ChatOllama
from langchain_ollama import ChatOllama
from langchain_core.tools import tool
import requests
from langchain_community.tools import DuckDuckGoSearchRun
from langchain.agents import create_react_agent, AgentExecutor
from langchain import hub


# defining tools

#search tool
search_tool = DuckDuckGoSearchRun()

#wheather tool
@tool
def get_weather_data(city: str) -> str:
  """
  This function fetches the current weather data for a given city
  """
  url =  f"https://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&appid=fdfb4aae850e1a7e86de77674a21bfbf"

  response = requests.get(url)

  return response.json()

#model
llm = ChatOllama(model="mistral")  # you can also use "mistral", "gemma", etc.


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

