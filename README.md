# Movie Recommender System

## Overview
This project implements a Movie Recommender System using machine learning techniques. It utilizes a dataset of movies to provide recommendations based on user-selected titles. The system fetches movie posters and displays them alongside the recommended titles.

## Features
- *Movie Recommendations*: Users can select a movie from a dropdown, and the system will recommend similar movies.
- *Poster Fetching*: The application fetches and displays movie posters from an external API.
- *Interactive UI*: Built using Streamlit for a user-friendly interface.

## Technologies Used
- Python
- Streamlit
- Requests
- Pickle
- The Movie Database (TMDb) API

## Installation
1. Clone the repository:
   bash
   git clone https://github.com/sravs-01/movie-recommender-system.git
   
2. Navigate to the project directory:
   bash
   cd movie-recommender-system
   
3. Install the required packages:
   bash
   pip install -r requirements.txt
   

## Usage
1. Run the application:
   bash
   streamlit run app.py
   
2. Open your web browser and go to http://localhost:8501 to access the Movie Recommender System.

## Dataset
The dataset used for this project includes movie titles, genres, and other relevant information. It is sourced from Kaggle:
- [TMDb Movie Metadata Dataset](https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata)

The dataset is stored in a pickle file for easy loading.

## Contributing
Contributions are welcome! Please open an issue or submit a pull request for any enhancements or bug fixes.

## Acknowledgments
- The Movie Database (TMDb) for providing the movie data and posters.
- Streamlit for creating an easy-to-use web application framework.
