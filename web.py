import streamlit as st
import functions

file_path = "todo.txt"

todos = functions.get_todo(file_path)

def add_todo():
    todo = st.session_state["new_todo"]+"\n"
    todos.append(todo)
    functions.write_todo(todos,file_path)
    



st.title("My todo App")
st.subheader("This is my tofo app")
st.write("This app is to increase your productivity")

for todo in todos:
    st.checkbox(todo)
    
st.text_input(label="",placeholder="Add a new todo...",on_change=add_todo,key='new_todo')

st.session_state

 