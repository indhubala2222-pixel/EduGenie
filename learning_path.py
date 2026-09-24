import google.generativeai as genai

def get_learning_path(topic: str):
    model = genai.GenerativeModel("gemini-1.5-flash")
    prompt = f"Provide a step-by-step learning path from beginner to advanced level for:\n{topic}"
    response = model.generate_content(prompt)
    return response.text
