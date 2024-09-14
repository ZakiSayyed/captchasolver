import streamlit as st
import asyncio
import websockets

# WebSocket connection logic
async def send_message(message):
    uri = "wss://a800-154-192-145-13.ngrok-free.app"
    try:
        async with websockets.connect(uri) as websocket:
            await websocket.send(message)
            response = await websocket.recv()  # Optionally receive a response
            return response
    except Exception as e:
        return f"An error occurred: {e}"

# Define a function to run asyncio event loop
def run_async_task(task):
    return asyncio.run(task)

st.title("WebSocket with Streamlit")

if st.button("Connect"):
    token = "token123"
    st.success("Token generated successfully!")

    # Send message to WebSocket server and print the response
    response = run_async_task(send_message(token))
    st.write(f"Response from WebSocket server: {response}")
