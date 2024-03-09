from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class CodeRequest(BaseModel):
    description: str


@app.post("/generate_code")
def generate_code(request: CodeRequest):
    # Code for LLM to generate code
    generated_code = f"Generated code for: {request.description}"
    return {"code": generated_code}
