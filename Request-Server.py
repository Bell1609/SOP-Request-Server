import hydralit_components as hc
import platform
import pandas as pd
import requests
import streamlit as st

# import streamlit_analytics
from streamlit_modal import Modal
import streamlit_lottie
import time
import json

from navigation.contact import contact_page
from navigation.home import home_page
from navigation.resource import resource_page
from utils.components import footer_style, footer
try:
    from streamlit import rerun as rerun
except ImportError:
    # conditional import for streamlit version <1.27
    from streamlit import experimental_rerun as rerun

import os

# Load Lottie file
def load_lottiefile(filepath: str):
    with open(filepath, "r") as f:
        return json.load(f)

# Set page config
st.set_page_config(
    page_title='SOP Request Server',
    page_icon="img/TRG_logo_page.png",
    initial_sidebar_state="expanded"
)

if 'lottie' not in st.session_state:
    st.session_state.lottie = False

if not st.session_state.lottie:
    st.lottie(load_lottiefile(".streamlit/loading.json"), speed=1.3, loop=False, width=600, height=600)
    time.sleep(2)
    st.session_state.lottie = True
    rerun()


max_width_str = f"max-width: {75}%;"

st.markdown(f"""
        <style>
        .appview-container .main .block-container{{{max_width_str}}}
        </style>
        """,
            unsafe_allow_html=True,
            )

st.markdown("""
        <style>
               .block-container {
                    padding-top: 0rem;
                    padding-bottom: 0rem;
                    
                }
        </style>
        """, unsafe_allow_html=True)

# Footer

st.markdown(footer_style, unsafe_allow_html=True)

# NavBar

HOME = 'Home'
REQUESTS = 'Requests'
CONTACT = 'Contact'

tabs = [
    HOME,
    REQUESTS,
    CONTACT,
]

option_data = [
    {'icon': "🏠", 'label': HOME},
    {'icon': "📑", 'label': REQUESTS},
    {'icon': "✉️", 'label': CONTACT},
]

over_theme = {'txc_inactive': 'black', 'menu_background': '#D6E5FA', 'txc_active': 'white', 'option_active': '#749BC2'}
font_fmt = {'font-class': 'h3', 'font-size': '50%'}

chosen_tab = hc.option_bar(
    option_definition=option_data,
    title='',
    key='PrimaryOptionx',
    override_theme=over_theme,
    horizontal_orientation=True)

st.success("Hello everyone, Welcome to our application! This platform is designed to simplify the process of raising requests for TRG Resource. "
           "With just a few clicks, you can select from the available options and submit your request quickly and efficiently. "
           "Whether you need specific resources for your projects or additional support, our app will guide you through each step, ensuring that you provide all necessary details. "
           "Thank you for using our app, and we look forward to helping you with your requests! 🥰")

st.success("If the application does not work, here are the people you can contact:\n"
           f"   - Nguyen Thuy Duong - Customer Support: duong.nguyen@trginternational.com\n"
           f"   - Tran Son Giang - Delivery - Cloud / Technical: giang.tran2@trginternational.com\n")

if chosen_tab == HOME:
    home_page()


elif chosen_tab == REQUESTS:
    resource_page()

elif chosen_tab == CONTACT:
    contact_page()

for i in range(4):
    st.markdown('#')
st.markdown(footer, unsafe_allow_html=True)

# Credit
st.sidebar.image("img/TRG_logo_site.png")

# How it works
st.sidebar.title("How it works")

with st.sidebar.expander("**Step 1: Fill your request**"):
    st.subheader("Please fill all of information for your request.")
    st.write(
        "Ensure that you fill out all required information for your request. " 
        "This helps us process your inquiry efficiently and address your needs promptly.")
    st.subheader("NOTE:")
    st.write("- Required fields are marked with an asterisk *")
    st.write(
        "- Please make sure to double-check all the information you have filled out after completing the form, including your email, name, planned details, and any other information. "
        "Ensuring there are no errors will help us process your request quickly and accurately!") 
    st.write("- Please remember that everything must be written in English.")


with st.sidebar.expander("**Step 2: Cloud Team Check**"):
    st.subheader("Request is approved by the Cloud Team")
    st.write("**✅ Your request has been successfully approved by the Cloud Team.** ")
    st.write("Cloud Team have reviewed the details and confirmed that everything meets the necessary requirements")
    st.write("**❌ Your request has been denied by the Cloud Team.** ")
    st.write("Cloud Team informed you that your request does not meet the necessary requirements.")

with st.sidebar.expander("**Step 3: Access Requests**"):
    st.subheader("Cloud Team implemented the user access request")
    st.write("Cloud Team send new user/user update information to Requester when completed.")

with st.sidebar.expander("**Step 4: Check information**"):
    st.subheader("Your request is completed, please check the information")
    st.write("Cloud Team revise User Access request if you have any questions or concerns.")

# Request status   
st.sidebar.title("Request status",
                 help='✅: Request has been approved \n\n❌: The request was not approved \n\n⚠️: You don\'t have any request')

# Check email
def check_email(email):
    if not email:
        return "Email is required."
    if not email.endswith("@trginternational.com"):
        return "Email must end with @trginternational.com."
    return None

# email input
email = st.sidebar.text_input("Enter your email:", placeholder="example@trginternational.com")
email_error = check_email(email)

if email_error:
    st.sidebar.error(email_error)

# if email is valid and button is clicked
if not email_error and st.sidebar.button("Check"):
    with st.sidebar:
        with st.spinner('Please wait...'):
            try:
                response = requests.get(f"https://trgrequest.herokuapp.com/request/{email}")
                if response.status_code == 200:
                    data = response.json()
                    if data:
                        for i in data:
                            if i['status'] == 'Approved':
                                st.write(f"✅ {i['status']} - {i['date']}")
                            elif i['status'] == 'Denied':
                                st.write(f"❌ {i['status']} - {i['date']}")
                    else:
                        st.write("⚠️ You don't have any request")
                else:
                    st.error("Error: Unable to retrieve requests.")
            except Exception as e:
                st.error("Error: Please try again later")
                print(e)

# Unique users
try:
    local_test = platform.processor()
    if local_test == "":
        unique_users = st.secrets['unique_users']
        st.sidebar.markdown(f"Unique users 👥: {unique_users}")
        st.session_state["LOCAL"] = 'False'
except Exception as e:
    st.session_state["LOCAL"] = 'True'
    st.sidebar.markdown(f"TFinder Local Version")
