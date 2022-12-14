import streamlit as st
import time
import functions

todos = functions.get_todos()


def add_todo():
    todo = st.session_state["new_todo"] + "\n"
    todos.append(todo)
    functions.write(todos)


st.title("Nulist Idea Mapping Service")
#now = time.strftime("%b %m, %Y %H:%M")
st.subheader("Control your day! Add todo.")

for item in todos:
    st.checkbox(item)

st.text_input(label="", placeholder="Add todo", on_change=add_todo,
              key="new_todo")


st.session_state