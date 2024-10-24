
import streamlit as st


def contact_page():
    a, b = st.columns([0.9, 1.4], gap='large')
    a.image('https://salt.topdev.vn/8xPw49ViPvG-FBnUtQH869vGqVzti_zrYiGbgWVF4rU/fit/828/1000/ce/1/aHR0cHM6Ly9hc3NldHMudG9wZGV2LnZuL2ltYWdlcy8yMDIyLzA0LzE0L1RvcERldi1UUkcyLTE2NDk5MjQ2NTkuanBlZw')
    a.markdown("""<span style="font-size:20px;">TRG International</span>""", unsafe_allow_html=True)

    a.markdown('##### If you have any questions or feedback, please feel free to contact us:')
    a.markdown("""<span style="font-size:18px;">**Nguyen Thuy Duong**<br>Customer Support<br>✉️ duong.nguyen@trginternational.com</span>""", unsafe_allow_html=True)
    a.markdown("""<span style="font-size:18px;">**Tran Son Giang**<br>Delivery - Cloud / Technical<br>✉️ giang.tran2@trginternational.com</span>""", unsafe_allow_html=True)

    b.markdown("""
        <div style="width: 100%">
            <iframe src="https://www.google.com/maps/embed?pb=!1m14!1m8!1m3!1d15678.093362666863!2d106.7235676!3d10.7711713!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x317525f5ffe3db4b%3A0xfa5be4ba8cdb7816!2sTRG%20International!5e0!3m2!1svi!2s!4v1729743350154!5m2!1svi!2s"
                width="500" height="450" style="border:0;" allowfullscreen="" loading="lazy" referrerpolicy="no-referrer-when-downgrade">
            </iframe>
        </div>
        """, unsafe_allow_html=True)
