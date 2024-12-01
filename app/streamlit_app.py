import streamlit as st
from learning_module.python_module_pages import (
    python_class_pg,
    python_global_local_variable_pg,
    python_decorator_pg,
    python_unittest_pg,
    python_pandas_pg 
)
from learning_module.devops_module_pages import (
    devops_docker_pg
)
from learning_module.ds_module_pages import (
    ds_home_pg
)

# print(st.session_state)
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
# if "sidebar_state" not in st.session_state:
#     st.session_state.sidebar_state = "expanded"
    
def login():
    st.snow()
    st.markdown("### Please **Log In**:")
    col1, col2, col3 = st.columns([2, 2, 2])
    with col1:
        st.text_input("Full Name", placeholder="Ramesh Gupta")
        if st.button("Log In"):
            st.session_state.logged_in = True
            st.rerun()
    with col2:
        st.text_input("Mobile Number", placeholder="88****6464")
    with col3:
        st.text_input("Email Address", placeholder="something@gmail.com")
        
def logout():
    st.markdown("### Do you want to logout from TheDataFestAI?")
    st.html("<h4>If yes, then click on below button -</h4>")
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

python_class_page = st.Page(python_class_pg, title="Python Class", icon=":material/call_made:")
python_global_local_variable_page = st.Page(python_global_local_variable_pg, title="Python Global/Nonlocal Variable", icon=":material/call_made:")
python_decorator_page = st.Page(python_decorator_pg, title="Python Decorator", icon=":material/call_made:")
python_unittest_page = st.Page(python_unittest_pg, title="Python Unittest", icon=":material/call_made:")
python_pandas_page = st.Page(python_pandas_pg, title="Pandas", icon=":material/call_made:")

devops_docker_page = st.Page(devops_docker_pg, title="Docker", icon=":material/call_made:")

ds_home_page = st.Page(ds_home_pg, title="Data Science - Home", icon=":material/call_made:")

finance_home_page = st.Page("finance_module/finance_home_page.py", title="Finance - Home", icon=":material/call_made:")

create_your_own_cv_page = st.Page("others/create_your_own_cv.py", title="Create Your CV", icon=":material/thumb_up:")
data_links_page = st.Page("others/data_links_page.py", title="Free Data Source Links", icon=":material/thumb_up:")


if st.session_state.logged_in:
    pg = st.navigation(
        {
            "🏚️ Account -": [logout_page, home, developer_details],
            "🐍 Python Learning Module -": [python_class_page, 
                                            python_global_local_variable_page, 
                                            python_decorator_page,
                                            python_unittest_page,
                                            python_pandas_page
                                            ],
            "🎢 Dev-Ops -": [devops_docker_page],
            "🪐 Data Science -": [ds_home_page],
            "💲 Finance_Module -": [finance_home_page],
            "🎲 Data Sources -": [data_links_page],
            "🎯 Apps -": [create_your_own_cv_page]
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
    