import streamlit as st
import asyncio
import websockets

# WebSocket connection logic
async def send_message(message):
    uri = "ws:https://e980-154-192-145-13.ngrok-free.app:8183"
    async with websockets.connect(uri) as websocket:
        await websocket.send(message)

# Define a function to run asyncio event loop
def run_async_task(task):
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(task)

st.title("WebSocket with Streamlit")

if st.button("Connect"):
    token = "token123"
    st.success("Token generated successfully!")
    
    # Send message to WebSocket server
    try:
        run_async_task(send_message(token))
        st.write("Message sent to WebSocket server")
    except Exception as e:
        st.error(f"An error occurred: {e}")
