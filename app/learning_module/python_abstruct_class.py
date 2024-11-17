# import re
# import requests
from pathlib import Path
import streamlit as st


st.title("Python Learning", help="https://www.python.org/")
st.html("<hr>")

# FILTER_SHARE = re.compile(r"^.*\[share_\w+\].*$", re.MULTILINE)
# content = requests.get(f"https://raw.githubusercontent.com/TheDataFestAI/thedatafestai_web/main/developer_guide.md").text
# st.markdown(FILTER_SHARE.sub("", content))
st.markdown((Path(__file__).parents[2]/"assets/learning_modules_md/python_module/python_abstruct_class.md").read_text())