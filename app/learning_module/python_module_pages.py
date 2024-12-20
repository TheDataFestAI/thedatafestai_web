import streamlit as st
from pathlib import Path
# import re
# import requests

def python_class_pg():
    st.title("🐍 TheDataFestAI - Python Class", help="https://www.python.org/", anchor=False)
    st.html("<hr>")
    # FILTER_SHARE = re.compile(r"^.*\[share_\w+\].*$", re.MULTILINE)
    # content = requests.get(f"https://raw.githubusercontent.com/TheDataFestAI/thedatafestai_web/main/developer_guide.md").text
    # st.markdown(FILTER_SHARE.sub("", content))
    st.markdown((Path(__file__).parents[2]/"assets/learning_modules_md/python_module/python_class.md").read_text(),
            unsafe_allow_html=True)
    
def python_global_local_variable_pg():
    st.title("🐍 TheDataFestAI - Python Global/Nonlocal Variables", anchor=False, help="https://www.geeksforgeeks.org/global-local-variables-python/")
    st.html("<hr>")
    st.markdown((Path(__file__).parents[2]/"assets/learning_modules_md/python_module/python_global_local_variable.md").read_text(),
            unsafe_allow_html=True)
    
def python_decorator_pg():
    st.title("🐍 TheDataFestAI - Python Decorator", anchor=False, help="https://www.geeksforgeeks.org/decorators-in-python/")
    st.html("<hr>")
    st.markdown((Path(__file__).parents[2]/"assets/learning_modules_md/python_module/python_decorator.md").read_text(),
            unsafe_allow_html=True)

def python_unittest_pg():
    st.title("🐍 TheDataFestAI - Python Unittest", anchor=False, help="https://docs.python.org/3/library/unittest.mock.html")
    st.html("<hr>")
    st.markdown((Path(__file__).parents[2]/"assets/learning_modules_md/python_module/python_unittest.md").read_text(),
            unsafe_allow_html=True)    
    
def python_pandas_pg():
    st.title("🐍 TheDataFestAI - Pandas", anchor=False, help="https://pandas.pydata.org/docs/reference/index.html")
    st.html("<hr>")
    st.markdown((Path(__file__).parents[2]/"assets/learning_modules_md/python_module/python_pandas.md").read_text(),
            unsafe_allow_html=True)
