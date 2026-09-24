import google.generativeai as genai

def generate_quiz(topic: str):
    model = genai.GenerativeModel("gemini-1.5-flash")
    prompt = f"Generate 3 multiple choice questions with 4 options and mark the correct answer for:\n{topic}"
    response = model.generate_content(prompt)
    return response.text
