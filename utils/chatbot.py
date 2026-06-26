import os
from dotenv import load_dotenv

from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()

llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature=0.2,
    google_api_key=os.getenv("GOOGLE_API_KEY")
)


def ask_pdf(question, vector_store):
    """
    Answer questions using the uploaded PDF.
    """

    # Better retriever than similarity_search
    retriever = vector_store.as_retriever(
        search_type="mmr",
        search_kwargs={
            "k": 8,
            "fetch_k": 20
        }
    )

    docs = retriever.invoke(question)

    context = "\n\n".join(
        doc.page_content for doc in docs
    )

    # Debug (prints retrieved chunks in terminal)
    print("\n==========================")
    print("Retrieved Context")
    print("==========================")
    print(context[:3000])
    print("==========================")

    prompt = f"""
You are an intelligent AI assistant.

Your ONLY knowledge source is the document context below.

DOCUMENT CONTEXT
----------------
{context}

----------------

QUESTION:
{question}

Instructions:

1. Read the document context carefully.

2. If the answer exists, answer in detail.

3. If only part of the answer exists, answer with the available information.

4. Do NOT say
"I couldn't find that information"
unless the context is completely unrelated.

5. Keep the answer clear and well formatted.

ANSWER:
"""

    response = llm.invoke(prompt)

    return response.content