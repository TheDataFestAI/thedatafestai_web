import streamlit as st
from pathlib import Path
import pandas as pd

from utils.write_data import generate_pdf


if "diy_cv_data" not in st.session_state:
    diy_cv_data_df = pd.DataFrame({
        "diy_cv_first_name": [],
        "diy_cv_middle_name": [],
        "diy_cv_last_name": []
    })
    st.session_state.diy_cv_data = diy_cv_data_df

def add_cv_details():
    new_diy_cv_personal_data_df = pd.DataFrame({
        "diy_cv_first_name": [st.session_state.diy_cv_first_name],
        "diy_cv_middle_name": [st.session_state.diy_cv_middle_name],
        "diy_cv_last_name": [st.session_state.diy_cv_last_name]
    })
    
    new_diy_cv_data_df = new_diy_cv_personal_data_df.copy()
    st.session_state.diy_cv_data = pd.concat([st.session_state.diy_cv_data, new_diy_cv_data_df])
    
    cv_content = str(st.session_state.diy_cv_data.to_json(orient='records'))
    st.session_state.cv_pdf_out_file_name = generate_pdf(file_name="sample_cv.pdf", content=cv_content)
    print(f"st.session_state.cv_pdf_out_file_name: {st.session_state.cv_pdf_out_file_name}")
    # st.html(f'<a href="{out_file_name}" download="{out_file_name.split("/")[-1]}">Download</a>')
    # st.html(f'<a href="" download="sample_cv.pdf" target="_blank">Download</a>')


# Web Page Design
# st.session_state.sidebar_state = "collapsed" if st.session_state.sidebar_state == "expanded" else "expanded" 

st.title("TheDataFestAI - Create Your Own CV", anchor=False)
st.html("<hr>")

st.markdown("## Fillup With Your Own Details -")

# Personal Details
st.html("<p>Provide Your Personal Details.</p>")
col1, col2, col3 = st.columns([2,2,2])
col1.text_input("First Name", placeholder="Ramesh", key="diy_cv_first_name")
col2.text_input("Middle Name", placeholder="Mohan", key="diy_cv_middle_name")
col3.text_input("Last Name", placeholder="Gupta", key="diy_cv_last_name")
    
col1, col2 = st.columns([2,4])
col1.text_input("Primary Mobile Number", placeholder="88****6464")
col2.text_input("Primary Email Id", placeholder="ramesh_g@gmail.com")

col1, col2 = st.columns([2,4])
col1.text_input("Secondary Mobile Number", placeholder="88****6464")
col2.text_input("Secondary Email Id", placeholder="ramesh_g@gmail.com")

col1, col2, col3 = st.columns([2,2,2])
col1._date_input("Date Of Birth")
col2.radio("Gender", ["Male", "Female", "Others"], horizontal=True)
col3.text_input("Nationality", placeholder="Indian")

col1, col2, col3 = st.columns([2,2,2])
col1.text_input("Religion", placeholder="Hinduism")
col2.text_input("Caste", placeholder="General")
col3.number_input("Yrs of Experience", step=1)

# Education Details
st.html("<p>Provide Your Education Details.</p>")
for i in range(5):
    if i == 0:
        edu_expander_name = "10th Standard"
    elif i == 1:
        edu_expander_name = "12th Standard"
    elif i == 2:
        edu_expander_name = "Bachelor's Degree"
    elif i == 3:
        edu_expander_name = "Master's Degree"
    elif i == 4:
        edu_expander_name = "PHD/Other Master's Degree"
        
    with st.expander(f"Education Details - **{edu_expander_name}**",
                     expanded= True if i == 0 else False):
        col1, col2 = st.columns([4,2])
        col1.text_input("School/College Name", key ="edu_sch_clg_name_"+str(i))
        col2.text_input("Years (From - To)", placeholder="Mar, 2020 - Feb, 2021", key ="edu_from_to_"+str(i))
        
        col1, col2 = st.columns([4,2])
        col1.text_input("Board/University Name", key ="edu_brd_uni_name_"+str(i))
        col2.text_input("Grade in Percentage",key ="edu_grade_"+str(i))    

# organisation Details
st.html("<p>Provide Your Current/Previous Organisation Details.</p>")
num_of_prev_organisation = st.slider("Number Of Previous Organisation", value=2, min_value=0, max_value=25)

if num_of_prev_organisation > 0:    
    for i in range(num_of_prev_organisation):
        with st.expander("Current Organisation Details" if i == 0 else str(i) + " Previous Organization Details", 
                         expanded= True if i == 0 else False):
            # st.caption("Organisation - " + "current" if i == 0 else "prev_"+str(i))
            col1, col2, col3 = st.columns([2,2,2])
            col1.text_input("Company/Organisation Name", placeholder="TCS or Wipro or HCL Tech etc.", key ="org_name_"+str(i))
            col2._date_input("Start Date", key ="org_start_date_"+str(i))
            col3._date_input("End Date", key ="org_end_date_"+str(i))
            # st.markdown("<br>", unsafe_allow_html=True)
            
            col1, col2, col3 = st.columns([2,2,2])
            col1.text_input("Project Name", placeholder="Data Analytics Project", key ="org_proj_name_"+str(i))
            col2.text_input("Client Name", placeholder="HSBC Bank", key ="org_proj_client_name_"+str(i))
            col3.text_input("No: of Team Member", placeholder="5", key ="org_proj_count_teammember_"+str(i))
            # st.markdown("<br>", unsafe_allow_html=True)
            
            st.text_area("Provide Job Summary", key ="org_job_summary_"+str(i))

col1, col2, col3 = st.columns([2,2,2]) 
col1.button("Generate CV", on_click=add_cv_details, key="diy_cv_submit")
# submitted = st.form_submit_button("Submit")
col2.write("")
col3.write("")

col1, col2, col3 = st.columns([2,2,2]) 
with col1:  
    if st.session_state.cv_pdf_out_file_name:
        with open(st.session_state.cv_pdf_out_file_name, "rb") as pdf_fp:
            btn = st.download_button(
                label="Download CV in PDF",
                data = pdf_fp,
                file_name="sample_cv.pdf",
                mime="application/octet-stream"
            )

# st.dataframe(st.session_state.diy_cv_data)
