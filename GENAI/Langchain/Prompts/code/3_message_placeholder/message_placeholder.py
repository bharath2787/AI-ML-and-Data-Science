from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
# chat template
chat_template = ChatPromptTemplate([
    MessagesPlaceholder(variable_name='chat_history'),
    ('human','{query}')
])

chat_history = []
# loading chat history from txt file
with open('chathistory.txt') as f:
    chat_history.extend(f.readlines())

print(chat_history)

# # create prompt
prompt = chat_template.invoke({'chat_history':chat_history, 'query':'whats the update on my refund'})

# print(prompt)