import streamlit as st
from datetime import datetime

def resource_page():
    st.divider()
    st.markdown("<h3 style='text-align: center; color: black;'>TRG Request Resource</h3>", unsafe_allow_html=True)
    
    email_confirmation = st.text_input("Email confirmation to")
    full_name = st.text_input("Full Name")
    project_name = st.text_input("Project Name")
    manager_pm_mails = st.text_input("Manager / PM Mails")
    
    description = st.text_area("Description:")

    change_type_options = ["Option 1", "Option 2", "Option 3"]
    selected_change_type = st.selectbox("Change type", change_type_options)

    change_reason_options = ["Option 1", "Option 2", "Option 3"]
    selected_change_reason = st.selectbox("Change reason", change_reason_options)

    planned_start = st.date_input("Planned Start")
    planned_start_time = st.time_input("Planned Start Time")

    planned_end = st.date_input("Planned End")
    planned_end_time = st.time_input("Planned End Time")

    uploaded_file = st.file_uploader("Project Plan:")

    # Tạo không gian cho nút gửi ở giữa trang
    st.markdown("<div style='text-align: center;'>", unsafe_allow_html=True)
    if st.button("Send Request"):
        if (email_confirmation and full_name and project_name and manager_pm_mails and 
            selected_change_type and selected_change_reason and description and 
            uploaded_file and planned_start and planned_start_time and 
            planned_end and planned_end_time):
            st.success("Form submitted successfully!")
            st.write(f"Email confirmation to: {email_confirmation}")
            st.write(f"Full Name: {full_name}")
            st.write(f"Project Name: {project_name}")
            st.write(f"Manager / PM Mails: {manager_pm_mails}")
            st.write(f"Change Type: {selected_change_type}")
            st.write(f"Change Reason: {selected_change_reason}")
            st.write(f"Planned Start: {planned_start} {planned_start_time}")
            st.write(f"Planned End: {planned_end} {planned_end_time}")
            st.write(f"Description: {description}")
            st.write(f"Uploaded file: {uploaded_file.name}")
        else:
            st.error("Please fill in all fields and upload a file.")
    st.markdown("</div>", unsafe_allow_html=True)


