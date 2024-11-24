import streamlit as st
from pathlib import Path

def ds_home_pg():
    st.title("🪐 TheDataFestAI - Data Science", help="", anchor=False)
    st.html("<hr>")
    st.markdown((Path(__file__).parents[2]/"assets/learning_modules_md/data_science_module/datascience_home.md").read_text(),
            unsafe_allow_html=True)