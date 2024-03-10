# Autify

Autify coding assessment solution

## Local Setup

To run the application locally, follow these steps:

1. **Clone the repository:**

    ```bash
    git clone https://github.com/your-username/Autify.git
    cd Autify
    ```

2. **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

3. **Run the FastAPI server and launch the Streamlit frontend:**

    ```bash
    python run_server.py --model "model_path"
    ```

    Replace `model_path` with the local path to your Language Model (LLM) or provide the model card path to a Hugging Face model.

4. **Access the application:**

   - **FastAPI server:** Not necessary to open, but if you want to see the API endspoints, head to http://localhost:8000/docs
   - **Streamlit frontend:** The script will automatically open a Streamlit app in a new window. If not, open the following url: http://localhost:8501/

## Notes

- The default model used for testing was StarChat-beta
