import requests

API_BASE = "http://127.0.0.1:5000"

def login(username, password):
    response = requests.post(f"{API_BASE}/auth/login", json={"username": username, "password": password})
    return response

def get_users():
    return requests.get(f"{API_BASE}/users").json()

def get_events():
    return requests.get(f"{API_BASE}/events").json()

def get_logs():
    return requests.get(f"{API_BASE}/logs").json()
