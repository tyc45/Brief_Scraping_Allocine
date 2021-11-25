import streamlit as st
import pandas as pd

'''
App that will allow to search through a list of movies or tv shows by some criterias
'''

st.title("The Amazing Show Sorting App!!!!")
best_movies = pd.read_csv("best_movies.csv", sep=",")



# st.dataframe(best_movies.style.highlight_max('rating'))