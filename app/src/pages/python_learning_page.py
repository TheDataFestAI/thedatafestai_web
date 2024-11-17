# import re
# import requests
from pathlib import Path
import streamlit as st
from ..page_utils import WebPage

class PythonLearningPage(WebPage):
    def __init__(self):
        pass
    
    def write(self):
        st.title("Python Learning", help="https://www.python.org/")
        st.html("<hr>")
        
        # FILTER_SHARE = re.compile(r"^.*\[share_\w+\].*$", re.MULTILINE)
        # # content = requests.get(f"https://raw.githubusercontent.com/TheDataFestAI/thedatafestai_web/main/developer_guide.md").text
        # content = requests.get(f"https://raw.githubusercontent.com/TheDataFestAI/thedatafestai_web/dev_15112024/assets/learning_modules_md/python_learning_module.md").text
        # st.markdown(FILTER_SHARE.sub("", content))
        
        st.markdown((Path(__file__).parents[3]/"assets/learning_modules_md/python_learning_module.md").read_text())