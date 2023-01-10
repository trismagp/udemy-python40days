import streamlit as st
import time
import pandas as pd


df = pd.read_csv('data.csv',delimiter=';')
df.reset_index()

st.set_page_config(layout="wide")
c1, c2 = st.columns(2)

with c1:
    st.image('images/photo.png', width=400)

with c2:
    st.title("This is the youhou porfolio")
    st.info("Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.")

st.header("below you can find some apps I have build with python")

c1, c2 = st.columns(2)

for index, row in df.iterrows():
    if index % 2 == 0:
        with c1:
            st.title(row['title'])
            st.write(row['description'])
            st.image('images/'+row['image'])
            st.write("[Source code]("+ row['url'] +")")
    else:
        with c2:
            st.title(row['title'])
            st.write(row['description'])
            st.image('images/'+row['image'])
            st.write("[Source code]("+ row['url'] +")")