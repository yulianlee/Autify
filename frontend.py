import streamlit as st
import httpx

st.title("Code Generator")

# User input form
user_input = st.text_area("Describe your coding problem:")

if st.button("Generate Code"):
    with httpx.Client() as client:
        response = client.post(
            "http://127.0.0.1:8000/generate_code",
            json={"description": user_input},  # noqa
        )

    # Display generated code
    if response.status_code == 200:
        generated_code = response.json()["code"]
        st.code(generated_code, language="python")
    else:
        st.error(f"Error generating code. Status code: {response.status_code}")
