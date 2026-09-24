import google.generativeai as genai

def get_explanation(concept: str):
    model = genai.GenerativeModel("gemini-1.5-flash")
    prompt = f"Explain the following academic concept clearly with examples:\n{concept}"
    response = model.generate_content(prompt)
    return response.text
