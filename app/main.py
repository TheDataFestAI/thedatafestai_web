import streamlit as st


from src.page_utils import add_custom_css
from src.pages import PAGE_MAP

add_custom_css()

def main():
    with st.sidebar:
        st.title("🧩 Learning Modules")
        current_page = st.radio("home page", list(PAGE_MAP), label_visibility = 'hidden')
        
        # with st.expander("✨ Learning Components", True):
        #     current_page = st.radio("learning Page", list(Learning_PAGE_MAP), label_visibility = 'hidden')
        
    # ALL_PAGE_MAP[current_page]().write()
    PAGE_MAP[current_page]().write()


if __name__ == "__main__":
    main()

