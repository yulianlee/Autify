from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class CodeRequest(BaseModel):
    description: str


class FeedbackRequest(BaseModel):
    code: str
    feedback: str


@app.post("/generate_code")
def generate_code(request: CodeRequest):
    # Code for LLM to generate code
    generated_code = f"Generated code for: {request.description}"
    return {"code": generated_code, "message": "Updated code"}


@app.post("/submit_feedback")
def submit_feedback(request: FeedbackRequest):
    print(f"Received feedback: {request.feedback}")
    print(f"Generated code: {request.code}")
    return {"message": "Feedback received and noted."}
