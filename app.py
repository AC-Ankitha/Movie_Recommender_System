import streamlit as st
import pickle
import pandas as pd


# Define the recommend function
def recommend(movie):
    # Check if the movie exists in the dataset
    if movie not in movies['title'].values:
        return []

    # Get the index of the movie
    movie_index = movies[movies['title'] == movie].index[0]

    # Compute similarity scores
    distances = similarity_matrix[movie_index]

    # Get movie indices sorted by similarity
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    # Collect recommended movies
    recommended_movies = [movies.iloc[i[0]]['title'] for i in movies_list]

    return recommended_movies


# Load movie data and similarity matrix
movies_dict = pickle.load(open('movie_dict.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)
similarity_matrix = pickle.load(open('similarity_matrix.pkl', 'rb'))

# Streamlit app
st.title('Movie Recommender System')

selected_movie_name = st.selectbox(
    'Select a movie:',
    movies['title'].values)

if st.button('Recommend'):
    recommendations = recommend(selected_movie_name)
    if recommendations:
        for movie in recommendations:
            st.write(movie)
    else:
        st.write("No recommendations found.")