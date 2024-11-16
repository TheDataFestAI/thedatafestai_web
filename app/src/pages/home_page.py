import streamlit as st
from ..page_utils import WebPage


class HomePage(WebPage):
    def __init__(self):
        pass
    
    def write(self):
        st.title("Home Page", anchor=False)
        # st.markdown("<h1 style='text-align: center; color: red;'>Some title</h1>", unsafe_allow_html=True)
        