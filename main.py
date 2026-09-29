from fastapi import FastAPI, Request

from qna import answer_question
from explanation_module import explain_topic
from quiz_module import generate_quiz
from summary_module import summarize_text
from learning_path import get_learning_recommendation

from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles


app = FastAPI()

templates = Jinja2Templates(directory="templates")

app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/", response_class=HTMLResponse)
def home(request: Request):

    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={"request": request}
    )


@app.get("/qa")
def qa(question: str):

    return {"answer": answer_question(question)}


@app.get("/explain")
def explain(topic: str):

    return {"answer": explain_topic(topic)}


@app.get("/quiz")
def quiz(topic: str):

    return {"answer": generate_quiz(topic)}


@app.get("/summarize")
def summarize(text: str):

    return {"answer": summarize_text(text)}


@app.get("/learn/recommendations")
def learning_recommendations(topic: str):

    return {"answer": get_learning_recommendation(topic)}