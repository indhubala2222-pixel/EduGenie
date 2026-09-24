import google.generativeai as genai

def get_summary(text: str):
    model = genai.GenerativeModel("gemini-1.5-flash")
    prompt = f"Summarize the following content in concise bullet points:\n{text}"
    response = model.generate_content(prompt)
    return response.text
