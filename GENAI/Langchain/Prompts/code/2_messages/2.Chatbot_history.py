from langchain_openai import ChatOpenAI
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI()

chat_history = []
while True:
    user_input = input('You: ')
    chat_history.append(user_input)
    if user_input == 'exit':
        break
    result = model.invoke(user_input)
    chat_history.append(result.content)
    print("AI: ",result.content)

print(chat_history)
#this implementation of chatbot does not have memory so cannot undersand context 