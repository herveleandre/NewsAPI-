import streamlit as st
from send_email import send_email
import pandas

df = pandas.read_csv('pages/topics.csv')
row = df["topic"]
st.header("Contact Me!")


with st.form(key='emailForm'):
    user_input = st.text_input("Your email address")
    option = st.selectbox(
        'Choose a topic:',
        row)

    userMessage = st.text_area("Your Message")
    message = f"""\
Subject: New email from {user_input}

From: {user_input}

Topic: {option}

{userMessage}

"""
    button = st.form_submit_button("Submit")

    if button:
        send_email(message)
        st.info("Your email was sent successfully!")