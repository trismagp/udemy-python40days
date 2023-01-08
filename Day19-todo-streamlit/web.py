from functions import get_todos,add_todo,edit_todo,complete_todo
import streamlit as st

def add_todo_web():
    todo = st.session_state['new_todo']
    add_todo(todo)
    st.session_state['new_todo'] = ""

todos = get_todos()

st.title('My todo app')
st.subheader('this is my todo app')
st.write('this app is awesome')

for index,todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        complete_todo(todo)
        del st.session_state[todo]
        st.experimental_rerun()

st.text_input(label="", 
            placeholder="Add new todo...",
            on_change=add_todo_web,key="new_todo")