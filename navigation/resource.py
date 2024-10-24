import streamlit as st
import pandas as pd
import os
from datetime import datetime

def validate_form(email_confirmation, full_name, project_name, manager_pm_mails, 
                  selected_change_type, selected_change_reason, description, 
                  implementation, uploaded_file, planned_start, planned_start_time, 
                  planned_end, planned_end_time):
    # Check if all required fields are filled
    if not email_confirmation:
        st.error("Email confirmation is required.")
        return False
    if not full_name:
        st.error("Full Name is required.")
        return False
    if not project_name:
        st.error("Project Name is required.")
        return False
    if not manager_pm_mails:
        st.error("Manager / PM Mails are required.")
        return False
    if not description:
        st.error("Description is required.")
        return False
    if not implementation:
        st.error("Implementation plan is required.")
        return False
    if not uploaded_file:
        st.error("Project Plan upload is required.")
        return False
    if not planned_start:
        st.error("Planned Start date is required.")
        return False
    if not planned_start_time:
        st.error("Planned Start Time is required.")
        return False
    if not planned_end:
        st.error("Planned End date is required.")
        return False
    if not planned_end_time:
        st.error("Planned End Time is required.")
        return False
    
    return True

def save_to_csv(data):
    output_dir = "./output"
    filename = os.path.join(output_dir, "Request.csv")
    
    # Ensure the output directory exists
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    # Check if the file exists
    if os.path.exists(filename):
        # Load existing data
        existing_data = pd.read_csv(filename)
        # Check for duplicates
        if any(existing_data['Email Confirmation'] == data['Email Confirmation']):
            st.warning("A request with this email confirmation already exists.")
            return
        
        # Append the new data
        existing_data = existing_data.append(data, ignore_index=True)
        existing_data.to_csv(filename, index=False)
    else:
        # Create new CSV if not exists
        data.to_csv(filename, index=False)

def resource_page():
    st.divider()
    st.markdown("<h3 style='text-align: center; color: black;'>TRG Request Resource</h3>", unsafe_allow_html=True)

    # CSS để điều chỉnh khoảng cách
    st.markdown("""
        <style>
            .form-label {
                margin-bottom: 5px;  /* Giảm khoảng cách giữa label và input */
                display: block;  /* Đảm bảo mỗi label trên một dòng */
            }
            .form-input {
                margin-bottom: 15px;  /* Khoảng cách giữa các ô nhập */
            }
        </style>
    """, unsafe_allow_html=True)

    # st.markdown
    st.markdown("<label class='form-label'>Email confirmation to <span style='color:red;'>*</span></label>", unsafe_allow_html=True)
    email_confirmation = st.text_input("", key="email_confirmation", label_visibility='collapsed')
    
    st.markdown("<label class='form-label'>Your Full Name <span style='color:red;'>*</span></label>", unsafe_allow_html=True)
    full_name = st.text_input("", key="full_name", label_visibility='collapsed')
    
    st.markdown("<label class='form-label'>Project Name <span style='color:red;'>*</span></label>", unsafe_allow_html=True)
    project_name = st.text_input("", key="project_name", label_visibility='collapsed')
    
    st.markdown("<label class='form-label'>Manager / PM Mails <span style='color:red;'>*</span></label>", unsafe_allow_html=True)
    manager_pm_mails = st.text_input("", key="manager_pm_mails", label_visibility='collapsed')
    
    st.markdown("<label class='form-label'>Description <span style='color:red;'>*</span></label>", unsafe_allow_html=True)
    description = st.text_area("", key="description", label_visibility='collapsed')
    
    change_type_options = ["Standard", "Normal", "Emergency"]
    st.markdown("<label class='form-label'>Change type <span style='color:red;'>*</span></label>", unsafe_allow_html=True)
    selected_change_type = st.selectbox("", change_type_options, key="change_type", label_visibility='collapsed')
    
    change_reason_options = ["Repair", "Upgrade", "Maintenance", "New functionality", "Other"]
    st.markdown("<label class='form-label'>Change reason <span style='color:red;'>*</span></label>", unsafe_allow_html=True)
    selected_change_reason = st.selectbox("", change_reason_options, key="change_reason", label_visibility='collapsed')
    
    st.markdown("<label class='form-label'>Implementation plan <span style='color:red;'>*</span></label>", unsafe_allow_html=True)
    implementation = st.text_area("", key="implementation", label_visibility='collapsed')
    
    st.markdown("<label class='form-label'>Planned Start <span style='color:red;'>*</span></label>", unsafe_allow_html=True)
    planned_start = st.date_input("", key="planned_start", label_visibility='collapsed')
    st.markdown("<label class='form-label'>Planned Start Time <span style='color:red;'>*</span></label>", unsafe_allow_html=True)
    planned_start_time = st.time_input("", key="planned_start_time", label_visibility='collapsed')
    
    st.markdown("<label class='form-label'>Planned End <span style='color:red;'>*</span></label>", unsafe_allow_html=True)
    planned_end = st.date_input("", key="planned_end", label_visibility='collapsed')
    st.markdown("<label class='form-label'>Planned End Time <span style='color:red;'>*</span></label>", unsafe_allow_html=True)
    planned_end_time = st.time_input("", key="planned_end_time", label_visibility='collapsed')
    
    uploaded_file = st.file_uploader("Project Plan", key="uploaded_file")

    # Submit button
    st.markdown("<div style='text-align: center;'>", unsafe_allow_html=True)
    if st.button("Send Request"):
        if validate_form(email_confirmation, full_name, project_name, manager_pm_mails, 
                         selected_change_type, selected_change_reason, description, 
                         implementation, uploaded_file, planned_start, planned_start_time, 
                         planned_end, planned_end_time):
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
            st.write(f"Implementation plan: {implementation}")
            st.write(f"Uploaded file: {uploaded_file.name}")

            # Prepare data for CSV
            data = {
                "Email Confirmation": email_confirmation,
                "Full Name": full_name,
                "Project Name": project_name,
                "Manager / PM Mails": manager_pm_mails,
                "Change Type": selected_change_type,
                "Change Reason": selected_change_reason,
                "Planned Start": f"{planned_start} {planned_start_time}",
                "Planned End": f"{planned_end} {planned_end_time}",
                "Description": description,
                "Implementation Plan": implementation
            }
            df = pd.DataFrame([data])
            save_to_csv(df)
    
    st.markdown("</div>", unsafe_allow_html=True)

