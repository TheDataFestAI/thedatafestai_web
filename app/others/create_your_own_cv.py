import streamlit as st

st.title("TheDataFestAI - Create Your Own CV", anchor=False)
st.html("<hr>")

st.markdown("## Fillup With Your Own Details -")

# Personal Details
st.html("<p>Provide Your Personal Details.</p>")
col1, col2, col3 = st.columns([2,2,2])
col1.text_input("First Name", placeholder="Ramesh")
col2.text_input("Middle Name", placeholder="Mohan")
col3.text_input("Last Name", placeholder="Gupta")
    
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
for i in range(3):
    if i == 0:
        edu_expander_name = "10th Standard"
    elif i == 1:
        edu_expander_name = "12th Standard"
    else:
        edu_expander_name = "Bachelor's Degree"
        
    with st.expander(f"Education Details - {edu_expander_name}",
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
col1.button("Generate CV")
# submitted = st.form_submit_button("Submit")