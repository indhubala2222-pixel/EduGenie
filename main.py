import os
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import google.generativeai as genai

from explanation_module import get_explanation
from qna import get_qna_answer
from quiz_module import generate_quiz
from summary_module import get_summary
from learning_path import get_learning_path

app = FastAPI(title="EduGenie API")

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY", "YOUR_API_KEY")
genai.configure(api_key=GEMINI_API_KEY)

class RequestModel(BaseModel):
    task: str
    user_input: str

@app.get("/")
def home():
    return {"message": "EduGenie API is active!"}

@app.post("/generate")
def generate_response(data: RequestModel):
    task = data.task
    user_input = data.user_input

    if task == "Explain":
        res = get_explanation(user_input)
    elif task == "QnA":
        res = get_qna_answer(user_input)
    elif task == "Quiz":
        res = generate_quiz(user_input)
    elif task == "Summary":
        res = get_summary(user_input)
    elif task == "Recommend Path":
        res = get_learning_path(user_input)
    else:
        res = "Invalid Task"

    return {"status": "success", "task": task, "result": res}
