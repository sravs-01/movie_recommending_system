import pickle
import streamlit as st
import requests
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry
import os
import time

# Dictionary to cache poster URLs locally
poster_cache = {}

# Retry logic for API calls with increased backoff
def fetch_poster(movie_id):
    if movie_id in poster_cache:
        # Return cached poster if available
        return poster_cache[movie_id]
    
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US"
    session = requests.Session()

    # Retry strategy with longer backoff
    retries = Retry(total=5, backoff_factor=2, status_forcelist=[429, 500, 502, 503, 504])
    session.mount('https://', HTTPAdapter(max_retries=retries))

    try:
        response = session.get(url, timeout=10)  # Timeout set to 10 seconds
        response.raise_for_status()
        data = response.json()
        poster_path = data.get('poster_path', None)
        if poster_path:
            full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
            poster_cache[movie_id] = full_path  # Cache the poster
            return full_path
        else:
            return "https://via.placeholder.com/500x750.png?text=No+Poster+Available"
    except requests.exceptions.RequestException as e:
        st.error(f"Error fetching poster: {e}")
        return "https://via.placeholder.com/500x750.png?text=Error"  # Placeholder for failed requests

# Recommendation function
def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recommended_movie_names = []
    recommended_movie_posters = []

    for i in distances[1:4]:  # Reduce the number of recommendations to 3
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movie_names.append(movies.iloc[i[0]].title)
        poster = fetch_poster(movie_id)
        recommended_movie_posters.append(poster)
        time.sleep(2)  # Add a delay to avoid API rate limiting

    return recommended_movie_names, recommended_movie_posters

# Streamlit app
st.header('Movie Recommender System')

# Load data
movies = pickle.load(open('model/movie_list.pkl', 'rb'))
similarity = pickle.load(open('model/similarity.pkl', 'rb'))

movie_list = movies['title'].values
selected_movie = st.selectbox("Type or select a movie from the dropdown", movie_list)

# Display recommendations
if st.button('Show Recommendation'):
    recommended_movie_names, recommended_movie_posters = recommend(selected_movie)
    
    # Display results using columns
    cols = st.columns(3)  # 3 recommendations
    for idx, col in enumerate(cols):
        if idx < len(recommended_movie_names):
            col.text(recommended_movie_names[idx])
            col.image(recommended_movie_posters[idx])

