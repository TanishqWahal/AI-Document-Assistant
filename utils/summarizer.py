import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

# Load environment variables
load_dotenv()

# Initialize Gemini model
llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature=0.3,
    google_api_key=os.getenv("GOOGLE_API_KEY")
)


def generate_summary(text):
    """
    Generates a structured summary of the uploaded document.
    """

    # Limit input size
    text = text[:30000]

    prompt = f"""
You are an expert document analyst.

Analyze the following document and generate:

1. Executive Summary
2. Key Points (Bullet List)
3. Important Topics
4. Conclusion

Document:
{text}
"""

    response = llm.invoke(prompt)

    return response.content