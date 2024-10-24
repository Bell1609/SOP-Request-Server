import streamlit as st
import pandas as pd
import os
import smtplib

# Cấu hình email
port = 465 
smtp_server = "secure.emailsrvr.com"
login = "nam.tran@trginternational.com"
password = "Nam.trg16092002"
sender = "nam.tran@trginternational.com"

def validate_form(email_confirmation, full_name, project_name, manager_pm_mails, 
                  selected_change_type, selected_change_reason, description, 
                  implementation, uploaded_file, planned_start, planned_start_time, 
                  planned_end, planned_end_time):
    # Kiểm tra các trường bắt buộc
    required_fields = {
        "Email Confirmation": email_confirmation,
        "Full Name": full_name,
        "Project Name": project_name,
        "Manager / PM Mails": manager_pm_mails,
        "Description": description,
        "Implementation Plan": implementation,
        "Uploaded File": uploaded_file,
        "Planned Start": planned_start,
        "Planned Start Time": planned_start_time,
        "Planned End": planned_end,
        "Planned End Time": planned_end_time,
    }

    for field, value in required_fields.items():
        if not value:
            st.error(f"{field} is required.")
            return False
    
    return True

def save_to_csv(data):
    output_dir = "./output"
    filename = os.path.join(output_dir, "Request.csv")
    
    # Đảm bảo thư mục đầu ra tồn tại
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    # Kiểm tra xem tệp có tồn tại không
    if os.path.exists(filename):
        existing_data = pd.read_csv(filename)
        if any(existing_data['Email Confirmation'] == data['Email Confirmation']):
            st.warning("A request with this email confirmation already exists.")
            return
        
        # Sử dụng pd.concat thay vì append
        combined_data = pd.concat([existing_data, data], ignore_index=True)
        combined_data.to_csv(filename, index=False)
    else:
        data.to_csv(filename, index=False)

def resource_page():
    st.divider()
    st.markdown("<h3 style='text-align: center; color: black;'>TRG Request Resource</h3>", unsafe_allow_html=True)

    # CSS cho định dạng
    st.markdown("""
        <style>
            .form-label {
                margin-bottom: 5px;
                display: block;
            }
            .form-input {
                margin-bottom: 15px;
            }
        </style>
    """, unsafe_allow_html=True)

    # Nhập liệu
    email_confirmation = st.text_input("Email confirmation to *", key="email_confirmation")
    full_name = st.text_input("Your Full Name *", key="full_name")
    project_name = st.text_input("Project Name *", key="project_name")
    manager_pm_mails = st.text_input("Manager / PM Mails *", key="manager_pm_mails")
    description = st.text_area("Description *", key="description")
    
    change_type_options = ["Standard", "Normal", "Emergency"]
    selected_change_type = st.selectbox("Change type *", change_type_options, key="change_type")
    
    change_reason_options = ["Repair", "Upgrade", "Maintenance", "New functionality", "Other"]
    selected_change_reason = st.selectbox("Change reason *", change_reason_options, key="change_reason")
    
    implementation = st.text_area("Implementation plan *", key="implementation")
    
    planned_start = st.date_input("Planned Start *", key="planned_start")
    planned_start_time = st.time_input("Planned Start Time *", key="planned_start_time")
    
    planned_end = st.date_input("Planned End *", key="planned_end")
    planned_end_time = st.time_input("Planned End Time *", key="planned_end_time")
    
    uploaded_file = st.file_uploader("Project Plan", key="uploaded_file")

    # Nút gửi yêu cầu
    if st.button("Send Request"):
        if validate_form(email_confirmation, full_name, project_name, manager_pm_mails, 
                         selected_change_type, selected_change_reason, description, 
                         implementation, uploaded_file, planned_start, planned_start_time, 
                         planned_end, planned_end_time):
            
            # Chuẩn bị nội dung email
            message = f"""\
Subject: New TRG Request Submission
To: {email_confirmation}
From: {sender}

You have a new request submitted with the following details:

Email Confirmation: {email_confirmation}
Full Name: {full_name}
Project Name: {project_name}
Manager / PM Mails: {manager_pm_mails}
Change Type: {selected_change_type}
Change Reason: {selected_change_reason}
Planned Start: {planned_start} {planned_start_time}
Planned End: {planned_end} {planned_end_time}
Description: {description}
Implementation Plan: {implementation}
Uploaded file: {uploaded_file.name if uploaded_file else "No file uploaded"}
"""

            # Gửi email
            try:
                with smtplib.SMTP(smtp_server, port) as server:
                    server.login(login, password)
                    server.sendmail(sender, email_confirmation, message)

                st.success("Form submitted successfully and email sent!")
            except Exception as e:
                st.error(f"Error sending email: {str(e)}")

            # Lưu dữ liệu vào CSV
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
