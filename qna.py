import google.generativeai as genai

def get_qna_answer(question: str):
    model = genai.GenerativeModel("gemini-1.5-flash")
    prompt = f"Answer the following question accurately:\n{question}"
    response = model.generate_content(prompt)
    return response.text
