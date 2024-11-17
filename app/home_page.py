from pathlib import Path
import streamlit as st


st.title("Welcome to TheDataFestAI", anchor=False)
st.caption("Learn and explore new technologies and tools in easy and efficient way.")
st.html("<hr>")
# st.markdown("<h1 style='text-align: center; color: red;'>Some title</h1>", unsafe_allow_html=True)
st.markdown((Path(__file__).parents[1]/"README.md").read_text())