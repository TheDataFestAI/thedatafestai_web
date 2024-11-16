import re
import requests
import streamlit as st
from ..page_utils import WebPage

class PythonLearningPage(WebPage):
    def __init__(self):
        pass
    
    def write(self):
        st.title("Python Learning", help="https://www.python.org/")            
        
        st.write("Python Learning Page")
        
        FILTER_SHARE = re.compile(r"^.*\[share_\w+\].*$", re.MULTILINE)
        # content = requests.get(f"https://raw.githubusercontent.com/TheDataFestAI/thedatafestai_web/main/developer_guide.md").text
        content = requests.get(f"https://raw.githubusercontent.com/TheDataFestAI/thedatafestai_web/main/assets/learning_modules_md/python_learning_module.ipynb").text
        
        st.markdown(FILTER_SHARE.sub("", content))