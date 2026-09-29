from google import genai

client = genai.Client()


def get_learning_recommendation(topic):

    try:
        response = client.models.generate_content(
            model="gemini-3.8-flash",
            contents=f"""
Create a simple learning path for a college student who wants to learn {topic}.

Include:
1. Basic concepts
2. Important topics to study
3. Practical practice
4. Mini project idea
5. Final revision

Keep it simple and easy to follow.
"""
        )

        return response.text

    except Exception:

        return f"""EduGenie Learning Recommendation

Topic: {topic}

Learning Path:

1. Basic Concepts
Learn the basic definitions and fundamentals of {topic}.

2. Important Topics
Study the main concepts and important features of {topic}.

3. Practical Practice
Practice simple examples and small exercises.

4. Mini Project
Create a small project using the concepts you have learned.

5. Final Revision
Revise the important concepts and practice questions before completing the topic.

Note: This is a demo learning path because the Gemini service is temporarily unavailable."""