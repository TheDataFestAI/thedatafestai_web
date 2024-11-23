import streamlit as st
from learning_module.python_module_pages import (
    python_abstract_class_pg,
    python_global_local_variable_pg,
    python_decorator_pg 
)

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
    
def login():
    st.snow()
    st.markdown("### Please **Log In**:")
    col1, col2, col3 = st.columns([2, 2, 2])
    with col1:
        st.text_input("Full Name")
        if st.button("Log In"):
            st.session_state.logged_in = True
            st.rerun()
    with col2:
        st.text_input("Mobile Number")
    with col3:
        st.text_input("Email Address")
        
def logout():
    if st.button("Log Out"):
        st.session_state.logged_in = False
        st.rerun()

st.set_page_config(page_title="TheDataFestAI",
                   page_icon="🛎️",
                   layout="wide",
                   menu_items={
                       'Get Help': "https://github.com/TheDataFestAI/thedatafestai_web/discussions",
                        'Report a bug': "https://github.com/TheDataFestAI/thedatafestai_web/issues",
                        'About': "https://github.com/TheDataFestAI/thedatafestai_web/wiki"
                   }
                   )

st.markdown(
    """
    <style>
    </style>
    """,
    unsafe_allow_html=True
)

login_page = st.Page(login, title="Log In", icon=":material/login:")
logout_page = st.Page(logout, title="Log Out", icon=":material/logout:")

# Multiple Web Pages 
home = st.Page("others/home_page.py", title="Home", icon=":material/thumb_up:", default=True)
developer_details = st.Page("others/developer_details_page.py", title="Developer Details", icon=":material/thumb_up:")

python_abstract_page = st.Page(python_abstract_class_pg, 
                               title="Python Abstract Class", 
                               icon=":material/call_made:")
python_global_local_variable_page = st.Page(python_global_local_variable_pg, 
                                            title="Python Variable", 
                                            icon=":material/call_made:")
python_decorator_page = st.Page(python_decorator_pg, 
                                title="Python Decorator", 
                                icon=":material/call_made:")

finance_home_page = st.Page("finance_module/finance_home_page.py", title="Finance - Home", icon=":material/thumb_up:")

data_links_page = st.Page("others/data_links_page.py", title="Data Links", icon=":material/thumb_up:")

if st.session_state.logged_in:
    pg = st.navigation(
        {
            "🏨 Account": [logout_page, home, developer_details],
            "🏷️ Python Learning Module": [python_abstract_page, python_global_local_variable_page, python_decorator_page],
            "🪐 Data Science": [],
            "💲 Finance_Module": [finance_home_page],
            "*️⃣ Data Links": [data_links_page]
        },
        # position="hidden"      
    )
else:
    # pg = st.navigation([login_page])
    pg = st.navigation(
        {
            "Account": [login_page, home, developer_details]
        }
    )

pg.run()
    