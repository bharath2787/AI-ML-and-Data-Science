from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

embedding = OpenAIEmbeddings(model='text-embedding-3-large', dimensions=32)

documents = [
    "Rose is known as the king of flowers",
    "Tulip is a popular spring-blooming flower",
    "Sunflower follows the direction of the sun"
]

result = embedding.embed_documents(documents)

print(str(result))