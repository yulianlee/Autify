from fastapi import FastAPI
from pydantic import BaseModel
from model import load_pipeline, generate_code, improve_code
import argparse

app = FastAPI()


class CodeRequest(BaseModel):
    description: str


parser = argparse.ArgumentParser()
parser.add_argument(
    "--model_path",
    type=str,
    default="HuggingFaceH4/starchat-beta",
    help="Hugging Face model name or local path",
)
args = parser.parse_args()


@app.on_event("startup")
def load_language_model(model_name_or_path: str = args.model_path):
    global pipe  # Use a global variable to store the pipeline
    pipe = load_pipeline(model_name_or_path)
    return


@app.post("/generate_code")
def generate_code_from_llm(request: CodeRequest):
    # Code for LLM to generate code
    generated_code = generate_code(pipe, request.user_input)
    return {"output": generated_code}


@app.post("/improve_code")
def improve_code_from_llm(request: CodeRequest):
    # Code for LLM to generate code
    generated_code = improve_code(pipe, request.user_input)
    return {"output": generated_code}
