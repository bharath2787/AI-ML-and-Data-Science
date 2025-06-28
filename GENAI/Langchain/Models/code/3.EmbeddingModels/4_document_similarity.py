# Import necessary libraries
from langchain_openai import OpenAIEmbeddings           # For generating text embeddings using OpenAI
from dotenv import load_dotenv                          # To load environment variables from a .env file
from sklearn.metrics.pairwise import cosine_similarity  # For computing cosine similarity between vectors
import numpy as np                                      # For numerical operations (used by sklearn)

# Load environment variables (e.g., OpenAI API key from .env)
load_dotenv()

# Initialize the OpenAI embedding model with desired configuration
embedding = OpenAIEmbeddings(model='text-embedding-3-large', dimensions=300)

# Define a list of documents to compare against
documents = [
    "C. V. Raman was awarded the Nobel Prize in Physics for his work on light scattering, known as the Raman Effect.",
    "Homi Bhabha was the father of India's nuclear program and played a key role in founding the TIFR.",
    "APJ Abdul Kalam, known as the Missile Man of India, later served as the President of India.",
    "Satyendra Nath Bose collaborated with Einstein, leading to the development of Bose-Einstein statistics.",
    "Venkatraman Ramakrishnan won the Nobel Prize in Chemistry for his work on the structure of the ribosome."
]

# Define the user query
query = "who worked with Einstein?"
# query = "who was C. V. Raman ?"
# Convert the documents into embeddings (vector representations)
doc_embeddings = embedding.embed_documents(documents)

# Convert the query into an embedding (same vector space as documents)
query_embedding = embedding.embed_query(query)

print(cosine_similarity([query_embedding], doc_embeddings)) #  this is a 2D list
# Compute cosine similarity between query and each document embedding
scores = cosine_similarity([query_embedding], doc_embeddings)[0]  # fetching 1D list [0]

# Find the index of the most similar document (highest similarity score) 
# purpose of enumerate is to mark every embedding with its records index , so we can later sort it without losing indices
# sorting on the basis of second item (score) x[1]
# getting the highest score which is at the end. we get index and score both
index, score = sorted(list(enumerate(scores)), key=lambda x: x[1])[-1] 

# # Output the results
# print(query)                         # Original query
print(documents[index])             # Most similar document
print("similarity score is:", score)  # Similarity score
