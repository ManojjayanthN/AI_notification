import streamlit as st
import requests

st.set_page_config(page_title="AI Notification Login", page_icon="🔐", layout="centered")

API_URL = "http://127.0.0.1:5000/auth/login"

st.title("🔐 Admin Login")
st.write("Welcome to the AI Notification System. Please log in to continue.")

# Login Form
with st.form("login_form"):
    username = st.text_input("👤 Username")
    password = st.text_input("🔑 Password", type="password")
    submitted = st.form_submit_button("Login")

if submitted:
    if not username or not password:
        st.warning("Please enter both username and password.")
    else:
        try:
            response = requests.post(API_URL, json={"username": username, "password": password})
            if response.status_code == 200:
                data = response.json()
                if data.get("message") == "Login successful":
                    st.success("✅ Login successful! Redirecting to Admin Portal...")
                    st.session_state["logged_in"] = True
                    st.session_state["username"] = username
                    st.balloons()
                    st.switch_page("pages/admin_dashboard.py")  # 👈 Redirect to dashboard
                else:
                    st.error("❌ Invalid credentials.")
            else:
                st.error(f"⚠️ Server returned status code {response.status_code}")
        except requests.exceptions.ConnectionError:
            st.error("🚫 Could not connect to backend. Make sure Flask backend is running.")
