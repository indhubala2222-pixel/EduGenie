from google import genai

client = genai.Client()


def generate_quiz(topic):

    try:
        response = client.models.generate_content(
            model="gemini-3.8-flash",
            contents=f"""
Create 5 simple multiple-choice questions about {topic}.
Give 4 options for each question and clearly mention the correct answer.
Keep the questions suitable for a college student.
"""
        )

        return response.text

    except Exception:

        return f"""EduGenie Quiz

Topic: {topic}

1. What is the basic purpose of {topic}?
A) Learning and understanding concepts
B) Playing games
C) Watching movies
D) Sending messages

Correct Answer: A

2. Which is important when learning {topic}?
A) Practice
B) Ignoring examples
C) Avoiding revision
D) Skipping basics

Correct Answer: A

3. What helps improve knowledge of {topic}?
A) Regular practice
B) No practice
C) Memorizing without understanding
D) Avoiding questions

Correct Answer: A

4. Why are examples useful in {topic}?
A) They help understand concepts
B) They make learning impossible
C) They remove all concepts
D) They are unnecessary

Correct Answer: A

5. What should a student do after learning {topic}?
A) Revise and practice
B) Stop studying
C) Avoid exercises
D) Forget the concepts

Correct Answer: A

Note: This is a demo quiz because the Gemini service is temporarily unavailable."""