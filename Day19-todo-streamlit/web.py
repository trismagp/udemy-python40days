from functions import get_todos,add_todo,edit_todo,complete_todo
import streamlit as st

todos = get_todos()

st.title('My todo app')
st.subheader('this is my todo app')
st.write('this app is awesome')

for todo in todos:
    st.checkbox(todo)

st.text_input(label="", placeholder="Add new todo...")