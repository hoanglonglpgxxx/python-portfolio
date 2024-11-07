import streamlit as st
import send_email

st.header('Contact Us')


with st.form(key='contact_form'):
    user_email = st.text_input('Enter your email', key='email')
    user_message = st.text_area('Enter your message')

    message = f"""\
Subject: New email from {user_email}
From: {user_message}
Topic testtest
{user_message}
"""
    submit_button = st.form_submit_button(label='Submit')
    if submit_button:
        send_email.send(user_email, message)
        st.write(f'Send email success')
