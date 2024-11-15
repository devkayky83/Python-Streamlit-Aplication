import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")

try:
    df_ps4_reviews = pd.read_csv("../Games Aplication/datasets/PS4_GamesSales.csv", encoding="utf-8")
except UnicodeDecodeError:
    df_ps4_reviews = pd.read_csv("../Games Aplication/datasets/PS4_GamesSales.csv", encoding="latin-1")
    
df_games_sales = pd.read_csv("../Games Aplication/datasets/Video_Games_Sales_as_at_22_Dec_2016.csv")

games = df_games_sales["Name"].unique()
game = st.sidebar.selectbox("Games", games)

df_game = df_games_sales[df_games_sales["Name"] == game]
df_review = df_ps4_reviews[df_ps4_reviews["Game"] == game]

game_title = df_game["Name"].iloc[0]
game_platform = df_game["Platform"].iloc[0]
game_genre = df_game["Genre"].iloc[0]
game_score = df_game["Critic_Score"].iloc[0]
game_release = df_game["Year_of_Release"].iloc[0]

st.title(game_title)
st.subheader(game_genre)

colun1, colun2, colun3 = st.columns(3)
colun1.metric("Genre", game_genre)
colun2.metric("Critic Score", game_score)
colun3.metric("Year of Publication", game_release) 

st.divider()