import streamlit as st 
import plotly.express as px 
import pandas as pd 

df = pd.read_csv("fifa_eda.csv")
df.dropna(inplace=True)
selected = st.selectbox("Select feature to see it's graph ",df.select_dtypes(include='number').columns)
N_10 = df.nlargest(10,selected)[['Name','Club',selected]]
fig = px.bar(N_10,x='Name',y=selected,color='Name',title=f'The nlargest players with {selected}',color_discrete_sequence=px.colors.sequential.Electric_r)
st.plotly_chart(fig)
col_1, col_2, col_3 = st.columns(3)
card_1 = col_1.container(border = 1)
card_2 = col_2.container(border = 1)
card_3 = col_3.container(border = 1)
card_1.metric(label=f'Max of {selected} ',value=df[selected].max())
card_2.metric(label=f'Min of {selected} ',value=df[selected].min())
card_3.metric(label=f'Mean of {selected} ',value=df[selected].mean())
