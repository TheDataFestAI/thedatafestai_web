from pathlib import Path
import streamlit as st


st.title("Python Learning", anchor=False, help="https://www.geeksforgeeks.org/global-local-variables-python/")
st.html("<hr>")
st.markdown((Path(__file__).parents[3]/"assets/learning_modules_md/python_module/python_global_local_variable.md").read_text(),
            unsafe_allow_html=True)