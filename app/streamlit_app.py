import streamlit as st

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
    
def login():
    if st.button("Log In"):
        st.snow()
        st.session_state.logged_in = True
        st.rerun()
        
def logout():
    if st.button("Log Out"):
        st.session_state.logged_in = False
        st.rerun()

st.set_page_config(page_title="TheDataFestAI",
                   page_icon="https://streamlit.io/favicon.svg",
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
home = st.Page("home_page.py", title="Home", icon=":material/thumb_up:", default=True)
python_abstruct_page = st.Page("learning_module/python_abstruct_class.py", title="Python Abstruct Class", icon=":material/thumb_up:")
finance_home_page = st.Page("finance_module/finance_home_page.py", title="Finance - Home", icon=":material/thumb_up:")
developer_details = st.Page("others/developer_details_page.py", title="Developer Details", icon=":material/thumb_up:")

if st.session_state.logged_in:
    pg = st.navigation(
        {
            "🌏 Account": [home, logout_page],
            "⚓ Python Learning Module": [python_abstruct_page],
            "✨ Finance_Module": [finance_home_page],
            "🎈 Others": [developer_details]
        }
    )
else:
    # pg = st.navigation([login_page])
    pg = st.navigation(
        {
            "Account": [home, login_page]
        }
    )
    
pg.run()