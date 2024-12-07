from pathlib import Path
import streamlit as st

# root = 'https://raw.githubusercontent.com/TheDataFestAI/thedatafestai_web/main/'


def home_pg():
    st.title("Welcome to TheDataFestAI", anchor=False)
    st.caption("Learn and explore new technologies and tools in easy and efficient way.")

    st.markdown("### Follow Our Learning Modules:")
    col1, col2, col3, col4 = st.columns([2,2,2,2])
    col1.markdown("![image](https://github.com/user-attachments/assets/84d45118-b796-43fe-b470-e51fcebffb61)")
    col2.markdown("![image](https://github.com/user-attachments/assets/5c5973eb-0e67-47ba-8479-ee528e711cf6)")
    col3.markdown("![image](https://github.com/user-attachments/assets/15ae45c3-9c2c-4c4d-82b4-fc236f3deca4)")
    col4.markdown("![image](https://github.com/user-attachments/assets/cc06edc8-4f14-413a-96cb-0dbc18dfdb96)")

    col1, col2, col3, col4 = st.columns([3,3,3,3])
    btn_home_data_analyst = col1.button("Learn DA")
    btn_home_data_engineer = col2.button("Learn DE")
    btn_home_devops_engieer = col3.button("Learn SE")
    btn_home_data_scientist = col4.button("Learn DS")
    
    if btn_home_data_analyst:
        st.session_state.tdf_product = "Learn Data Analyst"
        st.rerun()
    if btn_home_data_engineer:
        st.session_state.tdf_product = "Learn Data Engineer"
        st.rerun()
    if btn_home_devops_engieer:
        st.session_state.tdf_product = "Learn Devops Engineer"
        st.rerun()
    if btn_home_data_scientist:
        st.session_state.tdf_product = "Learn Data Scientist"
        st.rerun()
    # print(f"st.session_state.tdf_product: {st.session_state.tdf_product}")

    st.html("<br>")
    st.markdown("### Follow Our Other Apps:")
    col1, col2, col3, col4 = st.columns([2,2,2,2])
    col1.image("https://github.com/user-attachments/assets/77a34805-bfef-41cc-b255-699b66d6f1c7", caption="EMI Calculator")
    col2.image("https://github.com/user-attachments/assets/ff47dc01-cb80-4162-a052-3cd8038ec7f1", caption="Create CV/Resume")

    col1, col2, col3, col4 = st.columns([3,3,3,3])
    btn_home_emi_calculator = col1.button("EMI Calculator")
    btn_home_create_cv = col2.button("Create CV")
    if btn_home_emi_calculator:
        st.session_state.tdf_product = "Finance Apps"
        st.rerun()
    if btn_home_create_cv:
        st.session_state.tdf_product = "Other Apps"
        st.rerun()
    st.html("<hr>")
    # st.markdown("<h1 style='text-align: center; color: red;'>Some title</h1>", unsafe_allow_html=True)
    st.markdown((Path(__file__).parents[2]/"README.md").read_text())
    
home_pg()