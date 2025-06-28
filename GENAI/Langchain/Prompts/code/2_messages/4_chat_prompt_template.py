from langchain_core.prompts import ChatPromptTemplate

chat_template = ChatPromptTemplate([
    ('system', 'You are an expert in the field of {field}'),
    ('human', 'Can you break down the concept of {concept} in simple language?')
])

prompt = chat_template.invoke({
    'field': 'machine learning',
    'concept': 'overfitting'
})

print(prompt)
