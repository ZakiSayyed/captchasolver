import streamlit as st
import asyncio
import websockets

async def send_message(message):
    uri = "ws://localhost:8765"
    async with websockets.connect(uri) as websocket:
        await websocket.send(message)

def generate_token():
    return "token123"

st.title("ADB Remote Trigger")

if st.button("Connect"):
    token = generate_token()
    st.success("Token generated successfully!")
    
    # Send message to WebSocket server
    asyncio.run(send_message(token))
    st.write("Message sent to WebSocket server")
