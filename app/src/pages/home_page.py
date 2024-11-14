import streamlit as st

from ..page_utils import WebPage


class HomePage(WebPage):
    def __init__(self):
        pass
    
    def write(self):
        st.title("Home Page")