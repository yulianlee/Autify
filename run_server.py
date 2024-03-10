import subprocess
import argparse


def run_fastapi_server(model_name_or_path):
    cmd = f"uvicorn main:app --host --reload --model {model_name_or_path}"
    subprocess.run(cmd, shell=True)


def launch_streamlit_frontend():
    cmd = "streamlit run frontend.py"
    subprocess.run(cmd, shell=True)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--model",
        type=str,
        default="HuggingFaceH4/starchat-beta",
        help="Hugging Face model name or local path",
    )
    args = parser.parse_args()

    # Run FastAPI server with arguments
    run_fastapi_server(args.model)

    # Launch Streamlit frontend
    launch_streamlit_frontend()
