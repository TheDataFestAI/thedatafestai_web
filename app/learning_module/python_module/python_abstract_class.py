# import re
# import requests
from pathlib import Path
import streamlit as st


st.title("Python Learning", help="https://www.python.org/", anchor=False)
st.html("<hr>")

# FILTER_SHARE = re.compile(r"^.*\[share_\w+\].*$", re.MULTILINE)
# content = requests.get(f"https://raw.githubusercontent.com/TheDataFestAI/thedatafestai_web/main/developer_guide.md").text
# st.markdown(FILTER_SHARE.sub("", content))
st.markdown((Path(__file__).parents[3]/"assets/learning_modules_md/python_module/python_abstract_class.md").read_text(),
            unsafe_allow_html=True)