import streamlit as st

st.set_page_config(layout="wide")
st.header("Contact me")

with st.form(key="email_form"):
    st.text_input("Your email address here...")
    st.text_area("Your message here...")
    st.form_submit_button("Submit")