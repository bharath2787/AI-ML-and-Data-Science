from langchain_huggingface import HuggingFaceEmbeddings

embedding = HuggingFaceEmbeddings(model_name='sentence-transformers/all-MiniLM-L6-v2')

documents = [
    "Rose is known as the king of flowers",
    "Tulip is a popular spring-blooming flower",
    "Sunflower follows the direction of the sun"
]

vector = embedding.embed_documents(documents)

print(str(vector))