from google import genai

client = genai.Client()


def explain_topic(topic):

    try:
        response = client.models.generate_content(
            model="gemini-3.8-flash",
            contents=f"Explain this topic in simple English for a college student: {topic}"
        )

        return response.text

    except Exception:

        return f"""EduGenie Explanation

Topic:
{topic}

Explanation:
{topic} is an important concept that can be understood through its basic definition, key features, examples, and practical applications.

This is a demo explanation because the Gemini service is temporarily unavailable."""