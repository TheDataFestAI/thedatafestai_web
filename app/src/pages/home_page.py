from pathlib import Path
import streamlit as st
from ..page_utils import WebPage


class HomePage(WebPage):
    def __init__(self):
        pass
    
    def write(self):
        st.title("Welcome to Indra's Blog Site", anchor=False)
        st.html("<hr>")
        # st.markdown("<h1 style='text-align: center; color: red;'>Some title</h1>", unsafe_allow_html=True)
        st.markdown((Path(__file__).parents[3]/"README.md").read_text())
        