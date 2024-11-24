import streamlit as st
from pathlib import Path

def devops_docker_pg():
    st.title("🎢 TheDataFestAI - Docker", help="https://docs.docker.com/manuals/", anchor=False)
    st.html("<hr>")
    st.markdown((Path(__file__).parents[2]/"assets/learning_modules_md/devops_module/devops_module_docker.md").read_text(),
            unsafe_allow_html=True)
