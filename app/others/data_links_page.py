import streamlit as st
from pathlib import Path
from utils.read_data import read_excel_sheet

st.title("🎷 Free Urls for Data -", anchor=False)
st.html("<hr>")

datalinks_df = read_excel_sheet(excel_file_path=(Path(__file__).parents[2]/"assets/data_links.xlsx"), sheet_name="sheet_data_link")
# print(datalinks_df.to_json())
# col1, col2, COl3 = st.columns([2, 2, 2])

for index, row in datalinks_df.iterrows():
    cols = st.columns(3)
    cols[0].write(str(row["id"]) +  ". " + row["data_source_name"])  
    cols[1].write(row["data_source_url_path"])

