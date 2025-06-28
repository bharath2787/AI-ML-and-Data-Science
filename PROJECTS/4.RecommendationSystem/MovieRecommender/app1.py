# Importing necessary libraries
import streamlit as st  # For building the web interface
import pickle  # For loading pre-saved model/data files
import pandas as pd  # For handling tabular data

# Function to recommend similar movies
def recommend(movie):
    # Get the index of the selected movie from the DataFrame
    movie_index = movies[movies['title'] == movie].index[0]

    # Fetch the similarity scores for that movie
    distances = similarity[movie_index]

    # Sort all movies based on similarity score in descending order
    # Exclude the first result as it will be the movie itself (index 0)
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    # Prepare a list to hold recommended movie titles
    recommended_movies = []
    for i in movies_list:
        # Append the title of the recommended movie using its index
        recommended_movies.append(movies.iloc[i[0]].title)
    
    # Return the list of recommended movie titles
    return recommended_movies

# Load the movie metadata (title, etc.) from a pickle file
movies_dict = pickle.load(open('model/movie_list.pkl', 'rb'))

# Convert the dictionary to a DataFrame for easy manipulation
movies = pd.DataFrame(movies_dict)

# Load the precomputed similarity matrix (e.g., cosine similarity)
similarity = pickle.load(open('model/similarity.pkl', 'rb'))

# Streamlit app title
st.title('Movie Recommender System')

# Dropdown menu for selecting a movie from the dataset
selected_movie_name = st.selectbox(
    'Select a movie name for checking Recommendations...',
    movies['title'].values
)

# Button to trigger recommendation generation
if st.button('Recommend'):
    # Get the recommended movie list
    recommendations = recommend(selected_movie_name)

    # Display each recommended movie title in the Streamlit app
    for i in recommendations:
        st.write(i)
