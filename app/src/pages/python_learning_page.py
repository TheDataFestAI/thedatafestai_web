import streamlit as st
from ..page_utils import WebPage

class PythonLearningPage(WebPage):
    def __init__(self):
        pass
    
    def write(self):
        st.write("Python Learning Page")