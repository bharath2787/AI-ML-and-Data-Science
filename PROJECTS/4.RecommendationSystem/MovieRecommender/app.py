# Import required libraries
import pickle  # For loading serialized Python objects
import streamlit as st  # For creating the web app
import requests  # For making API calls to fetch movie poster data

# Function to fetch the movie poster from TMDB using movie ID
def fetch_poster(movie_id):
    # Construct the API URL with the given movie ID
    # https://developer.themoviedb.org/reference/movie-details
    url = "https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US".format(movie_id)
    
    # Send GET request to TMDB API
    data = requests.get(url)
    
    # Parse the JSON response
    data = data.json()
    
    # Extract poster path and construct full URL for image
    poster_path = data['poster_path']
    full_path = "https://image.tmdb.org/t/p/w1280/" + poster_path
    
    # Return the full URL of the poster
    return full_path

# Function to recommend movies based on the selected movie
def recommend(movie):
    # Find the index of the selected movie in the dataframe
    index = movies[movies['title'] == movie].index[0]
    
    # Retrieve similarity scores for the selected movie
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    
    # Lists to store names and posters of recommended movies
    recommended_movie_names = []
    recommended_movie_posters = []
    
    # Loop over the top 5 most similar movies (excluding the selected one)
    for i in distances[1:6]:
        movie_id = movies.iloc[i[0]].movie_id  # Get the movie ID for poster fetching
        recommended_movie_posters.append(fetch_poster(movie_id))  # Fetch poster
        recommended_movie_names.append(movies.iloc[i[0]].title)  # Fetch title
    
    # Return both lists
    return recommended_movie_names, recommended_movie_posters

# Set the title/header of the Streamlit app
st.header('Movie Recommender System')

# Load movie metadata and similarity matrix from pickle files
movies = pickle.load(open('model/movie_list.pkl','rb'))  # DataFrame containing movie info
similarity = pickle.load(open('model/similarity.pkl','rb'))  # Similarity matrix

# Get the list of movie titles
movie_list = movies['title'].values

# Create a dropdown for the user to select or type a movie title
selected_movie = st.selectbox(
    "Type or select a movie from the dropdown",
    movie_list
)

# When the "Show Recommendation" button is clicked
if st.button('Show Recommendation'):
    # Get recommended movie names and posters
    recommended_movie_names, recommended_movie_posters = recommend(selected_movie)
    
    # Create five columns for displaying recommendations side by side
    col1, col2, col3, col4, col5 = st.columns(5)
    
    # Display the first recommended movie
    with col1:
        st.text(recommended_movie_names[0])
        st.image(recommended_movie_posters[0])
    
    # Display the second recommended movie
    with col2:
        st.text(recommended_movie_names[1])
        st.image(recommended_movie_posters[1])

    # Display the third recommended movie
    with col3:
        st.text(recommended_movie_names[2])
        st.image(recommended_movie_posters[2])
    
    # Display the fourth recommended movie
    with col4:
        st.text(recommended_movie_names[3])
        st.image(recommended_movie_posters[3])
    
    # Display the fifth recommended movie
    with col5:
        st.text(recommended_movie_names[4])
        st.image(recommended_movie_posters[4])
