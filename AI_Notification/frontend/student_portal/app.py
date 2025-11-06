import streamlit as st
import pandas as pd

st.title("Student Portal - Notifications")

# Load notification logs
logs = pd.read_csv("../../logs/notification_logs.csv")
st.subheader("Notifications Received")
st.dataframe(logs)
