import streamlit as st

st.title("Developers and Maintainers Details", anchor=False)
st.html("<hr>")

col1, col2, col3 = st.columns([1, 2, 3])
with col1:
    st.image("./assets/images/indra.png", width=150)
with col2:
    st.markdown("### Owner & Developer [Indranil Pal](https://www.linkedin.com/in/indranil-pal-ai/)")
with col3:
    st.markdown("### Data Engineer - Python, SQL, GCP")