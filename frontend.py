import streamlit as st
import httpx
import time

st.title("Code Generator")

# To create streaming effect


def streaming_effect(message):
    for word in message.split():
        yield word + " "
        time.sleep(0.05)


# Streamed response emulator
def response_generator(user_input):
    with httpx.Client() as client:
        response = client.post(
            "http://127.0.0.1:8000/generate_code",
            json={"description": user_input},  # noqa
        )

    if response.status_code == 200:
        generated_code = response.json()["code"]
        generated_message = response.json()["message"]

        return generated_code, generated_message


if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])


# Accept user input
if prompt := st.chat_input("Input coding problem description"):
    # Display user message in chat message container
    with st.chat_message("user"):
        st.markdown(prompt)
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})

    with st.chat_message("assistant"):
        code, message = response_generator(prompt)
        st.write_stream(streaming_effect(message))
        st.code(code, language="python")

    st.session_state.messages.append({"role": "assistant", "content": code})
