SUMMARY_PROMPT = """
You are an expert document analyst.

Analyze the following document and generate:

1. Executive Summary
2. Key Points (Bullet List)
3. Important Topics
4. Conclusion

Document:
{document}
"""


CHAT_PROMPT = """
You are an AI assistant.

Answer ONLY using the information provided in the document context.

Rules:
1. Answer only from the context.
2. If the answer is not present, reply:
   "I couldn't find that information in the uploaded document."
3. Keep your answers clear and concise.

Document Context:
{context}

Question:
{question}

Answer:
"""