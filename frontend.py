import streamlit as st
import httpx
import time

st.title("Code Generator")


def streaming_effect(message):
    """
    Render characters sequentially in the user interface.
    """
    for word in message.split():
        yield word + " "
        time.sleep(0.05)


def response_generator(user_input, mode=False):
    """
    Sends HTTP request to FastAPI backend and retrieves message from LLM.
    """
    if mode:
        with httpx.Client() as client:
            response = client.post(
                "http://127.0.0.1:8000/improve_code",
                json={"user_input": user_input},  # noqa
            )
    else:
        with httpx.Client() as client:
            response = client.post(
                "http://127.0.0.1:8000/generate_code",
                json={"user_input": user_input},  # noqa
            )

    if response.status_code == 200:
        output = response.json()["code"]

        return output


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

    # Display assistant response in message container
    with st.chat_message("assistant"):
        output = response_generator(
            prompt, mode=len(st.session_state.messages) >= 2
        )  # noqa: E501
        st.write_stream(streaming_effect(message))
        st.code(output, language="python")

    st.session_state.messages.append({"role": "assistant", "content": output})
