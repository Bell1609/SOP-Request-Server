
import streamlit as st
from PIL import Image
import datetime


def home_page():
    st.divider()
    st.markdown(
        "<h3 style='text-align: center; color: black;'>🏢SOP Request Server🏢</h1>",
        unsafe_allow_html=True)
    with open('./clock.time', 'r') as f:
        last_updated_on = f.readlines()[0]
    st.caption(last_updated_on)
    st.markdown('')
    st.image('img/workflow.png')
    st.markdown('')
    st.markdown('**Overview**')
    st.markdown(
        '<div style="text-align: justify;">The SOP Request Server is a system designed to optimize the process of creating, managing, and retrieving Standard Operating Procedures (SOPs) within an organization. This system includes features such as an approval workflow that allows users to submit new SOP requests or revisions, along with a centralized repository that makes information easily accessible to relevant stakeholders. It also integrates version control to track changes over time, search and filtering tools for quickly finding necessary SOPs, and user role management to control access. Additionally, the system maintains an audit trail to ensure compliance and accountability, along with reminder notifications to help keep SOPs current and up to date.</div>',
        unsafe_allow_html=True)
    st.divider()
    st.markdown('**How it work**')
    st.markdown(
        '<div style="text-align: justify;"><p style="text-indent: 2em;">DEMO</p></div>',
        unsafe_allow_html=True)
 

