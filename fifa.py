import streamlit as st 
import plotly.express as px 
import pandas as pd 

st.markdown("<h1 style='text-align: center; color: black;'> Wide view on fifa data </h1>", unsafe_allow_html=True)
st.image('https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQWZcrpscY23Bvf2BbdIEe6xNC8dvxC3BNZIg&usqp=CAU',width=800)
st.markdown(''' 
The FIFA dataset typically refers to a collection of data related to real-life football (soccer) players,
rather than the FIFA video game series.
This dataset encompasses various attributes and statistics about professional football players from around the world.
[Fifa](https://www.kaggle.com/datasets/javagarm/fifa-19-complete-player-dataset)

''')
df = pd.read_csv(r"C:\Users\fg\Downloads\Project 12_FIFA EDA\fifa_eda.csv")
df.dropna(inplace=True)