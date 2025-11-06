import streamlit as st
import requests

API_URL = "http://127.0.0.1:5000/auth/login"

st.title("Admin Portal - Notification System")

# Login Page
username = st.text_input("Username")
password = st.text_input("Password", type="password")

if st.button("Login"):
    response = requests.post(API_URL, json={"username": username, "password": password})
    if response.status_code == 200:
        st.success("Login Successful")
        st.write("You can now manage events and view notification logs")
        st.write("---")
        # Event management and logs can be implemented here
    else:
        st.error("Invalid credentials")
