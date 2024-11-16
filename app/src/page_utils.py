import streamlit as st
from abc import ABC, abstractmethod


class WebPage(ABC):
    @abstractmethod
    def write(self):
        pass

  
def add_custom_css():
    # set page icon and page name in browser's title bar or in the page's tab.
    st.set_page_config(page_title="TheDataFestAI", 
                       page_icon="https://streamlit.io/favicon.svg", 
                       layout="wide",
                       menu_items={
                                    'Get Help': "https://github.com/TheDataFestAI/thedatafestai_web/discussions",
                                    'Report a bug': "https://github.com/TheDataFestAI/thedatafestai_web/issues",
                                    'About': "https://github.com/TheDataFestAI/thedatafestai_web/wiki"
                                }
                       )
    
    st.markdown(
        """
        <style>
        
        </style>
        """,
        unsafe_allow_html=True
    )