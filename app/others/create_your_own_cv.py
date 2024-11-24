import streamlit as st

st.title("TheDataFestAI - Create Your Own CV", anchor=False)
st.html("<hr>")


col1, col2, col3 = st.columns([2,2,2])
col1.text_input("First Name", placeholder="Ramesh")
col2.text_input("Middle Name", placeholder="Mohan")
col3.text_input("Last Name", placeholder="Gupta")
    
col1, col2 = st.columns([2,4])
col1.text_input("Primary Mobile Number", placeholder="88****6464")
col2.text_input("Primary Email Id", placeholder="ramesh_g@gmail.com")

col1, col2, col3 = st.columns([2,2,2])
col1._date_input("Date Of Birth")
col2.radio("Gender", ["Male", "Female", "Others"], horizontal=True)

col1, col2, col3 = st.columns([2,2,2])
col1.text_input("Nationality", placeholder="Indian")
col2.text_input("Religion", placeholder="Hinduism")
col3.text_input("Caste", placeholder="General")

num_of_prev_organisation = st.slider("Number Of Previous Organisation", value=2, min_value=0, max_value=25)

if num_of_prev_organisation > 0:
    for i in range(num_of_prev_organisation):
        st.caption("Organisation - " + str(i))
        col1, col2, col3 = st.columns([2,2,2])
        col1.text_input("Company/Organisation Name", placeholder="TCS or Wipro or HCL Tech etc.", key ="org_name_"+str(i))
        col2._date_input("Start Date", key ="org_start_date_"+str(i))
        col3._date_input("End Date", key ="org_end_date_"+str(i))
        st.text_area("Provide Job Summary", key ="org_job_summary_"+str(i))

col1, col2, col3 = st.columns([2,2,2])   
col1.button("Generate CV")
    # submitted = st.form_submit_button("Submit")