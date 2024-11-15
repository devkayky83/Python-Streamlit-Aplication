import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(layout="wide")

df_games_sales = pd.read_csv("../Games Aplication/datasets/Video_Games_Sales_as_at_22_Dec_2016.csv")

year_max = df_games_sales["Year_of_Release"].max()
year_min = df_games_sales["Year_of_Release"].min()

max_year = st.sidebar.slider("Year_of_Release", year_min, year_max, year_max)
df_games = df_games_sales[df_games_sales["Year_of_Release"] <= max_year]
st.write(df_games)

fig1 = px.bar(df_games["Year_of_Release"].value_counts())
fig2 = px.histogram(df_games["Global_Sales"].value_counts()) 
colun1, colun2 = st.columns(2)
colun1.plotly_chart(fig1)
colun2.plotly_chart(fig2)

