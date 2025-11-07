import streamlit as st

st.set_page_config(page_title="Admin Portal", page_icon="🧠", layout="wide")

if "logged_in" not in st.session_state or not st.session_state["logged_in"]:
    st.warning("⚠️ Please log in first.")
    st.stop()

st.title("🧠 Admin Dashboard")
st.write(f"Welcome, **{st.session_state['username']}** 👋")
st.markdown("---")
st.info("You are now inside the Admin Portal!")

# Add your dashboard widgets below
st.metric("Total Notifications", 42)
st.metric("Active Users", 7)
st.metric("System Status", "✅ Running Smoothly")
