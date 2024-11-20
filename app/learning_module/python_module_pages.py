import streamlit as st
from pathlib import Path
# import re
# import requests

def python_abstract_class_pg():
    st.title("TheDataFestAI - Python Class", help="https://www.python.org/", anchor=False)
    st.html("<hr>")
    # FILTER_SHARE = re.compile(r"^.*\[share_\w+\].*$", re.MULTILINE)
    # content = requests.get(f"https://raw.githubusercontent.com/TheDataFestAI/thedatafestai_web/main/developer_guide.md").text
    # st.markdown(FILTER_SHARE.sub("", content))
    st.markdown((Path(__file__).parents[2]/"assets/learning_modules_md/python_module/python_abstract_class.md").read_text(),
            unsafe_allow_html=True)
    
def python_global_local_variable_pg():
    st.title("TheDataFestAI - Python Variables", anchor=False, help="https://www.geeksforgeeks.org/global-local-variables-python/")
    st.html("<hr>")
    st.markdown((Path(__file__).parents[2]/"assets/learning_modules_md/python_module/python_global_local_variable.md").read_text(),
            unsafe_allow_html=True)
    
