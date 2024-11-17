from pathlib import Path
import streamlit as st


from src.page_utils import add_custom_css
from src.pages import PAGE_MAP, Finance_PAGE_MAP

add_custom_css()

def main():
    
    with st.sidebar:
        # st.html("<img src='.//assets//images//indra.png' alt='Indranil Pal' width='300' height='300'>")
        
        _, col2, _ = st.columns([1, 2, 1])
        with col2:
            st.image("./assets/images/indra.png", width=150)
        st.caption("Developed/Mainted By [Indranil Pal](https://www.linkedin.com/in/indranil-pal-ai/)")
        # st.title("🧩 Learning Modules")
        
        with st.expander("🧩 Learning Modules"):
            current_page = st.radio("home page", list(PAGE_MAP), label_visibility = 'hidden')
            
        # with st.expander("🧩 Finance Modules"):
        #     current_page = st.radio("finance page", list(Finance_PAGE_MAP), label_visibility = 'hidden')
    
    # for i in PAGE_MAP.keys():
    #     if i == current_page:
    #         print(i, current_page)
    
    
    PAGE_MAP[current_page]().write()
    

if __name__ == "__main__":
    main()

