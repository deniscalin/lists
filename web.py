import streamlit as st
import time
import functions

todos = functions.get_todos()

st.title("Nulist Idea Mapping Service")
#now = time.strftime("%b %m, %Y %H:%M")
st.subheader("Control your day! Add todo.")

for item in todos:
    st.checkbox(item)

st.text_input(label="", placeholder="Add todo")

