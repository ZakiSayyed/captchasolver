import streamlit as st
import requests

# Define the Flask server URL
FLASK_URL = 'http://localhost:5000/verify'

def generate_token():
    return "token123"

st.title("ADB Remote Trigger")

# Use Streamlit widgets for user input
if st.button("Connect"):
    token = generate_token()
    st.success("Token generated successfully!")

    # Use requests to communicate with Flask
    response = requests.post(FLASK_URL, json={"token": token})
    
    if response.status_code == 200:
        st.write("Request was successful")
    else:
        st.write("Request failed with status code:", response.status_code)
