import streamlit as st
import pandas as pd


movies = {
    "title" : ["Avengers", "Spiderman", "Hulk", "Avatar"]
}

df = pd.DataFrame(movies)

st.title("This is our movie recommendation system")

selected_movie = st.selectbox("Enter the movie name...", df["title"].values)

recommendBtn = st.button("Recommend")

if recommendBtn:
    st.write("Displaying recommendations for "+selected_movie)

