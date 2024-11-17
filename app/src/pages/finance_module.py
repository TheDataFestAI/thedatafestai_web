import streamlit as st
from ..page_utils import WebPage

class FinanceModule(WebPage):
    def __init__(self):
        pass
    
    def write(self):
        st.title("Finance Module")
        st.html("<hr>")