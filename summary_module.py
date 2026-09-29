from google import genai

client = genai.Client()


def summarize_text(text):

    try:
        response = client.models.generate_content(
            model="gemini-3.8-flash",
            contents=f"""
Summarize the following text in simple English for a college student.
Keep the important points and make it easy to understand.

Text:
{text}
"""
        )

        return response.text

    except Exception:

        return f"""EduGenie Summary

Original Text:
{text}

Summary:
This text contains important information about the given topic.
The main ideas can be understood by identifying the key points,
important concepts, and useful details.

Note: This is a demo summary because the Gemini service is temporarily unavailable."""