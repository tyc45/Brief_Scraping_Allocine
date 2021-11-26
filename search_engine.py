import streamlit as st
import pandas as pd

'''
App that will allow to search through a list of movies or tv shows by some criterias
'''

st.title("The Amazing Show Sorting App!!!!")
best_movies = pd.read_csv("best_movies.csv", sep=",")
data_filtered = st.container()

# st.dataframe(best_movies.style.highlight_max('rating'))
# st.table(best_movies)
min_length = int(best_movies['length'].describe()['min'])
max_length = int(best_movies['length'].describe()['max'])
avg_length = int((min_length + max_length)/2)

min_rating = float(best_movies['rating'].describe()['min'])
max_rating = float(best_movies['rating'].describe()['max'])
avg_rating = (min_rating + max_rating)/2

            
actor_list = best_movies['staring'].str.split(',').explode()
actor_list = list(dict.fromkeys(actor_list))

# actor_list

genre_list = best_movies['genres'].str.split(',').explode()
genre_list = list(dict.fromkeys(genre_list))
# genre_list

# if checkbox then...
with data_filtered:
    title_mask = staring_mask = genre_mask = length_mask = rating_mask = pd.Series(True, best_movies.index)
    if st.sidebar.checkbox('Title'):
        title_mask = best_movies['title'] == st.sidebar.selectbox('', best_movies['title'])
    if st.sidebar.checkbox('Staring'):
        staring_mask = best_movies['staring'].str.contains(st.sidebar.selectbox('', actor_list))
    if st.sidebar.checkbox('Genre'):
        genre_mask = best_movies['genres'].str.contains(st.sidebar.selectbox('', genre_list))
    if st.sidebar.checkbox('Length'):
        length_mask = best_movies['length'] >= st.sidebar.slider('', min_value= min_length, max_value= max_length , value= avg_length)
    if st.sidebar.checkbox('Rating'):
        rating_mask = best_movies['rating'] >= st.sidebar.slider('', min_value= min_rating, max_value= max_rating , value= avg_rating)

    best_movies[title_mask & staring_mask & genre_mask & length_mask & rating_mask]
    
# best_movies
# best_movies[best_movies['title'] == title_filter]