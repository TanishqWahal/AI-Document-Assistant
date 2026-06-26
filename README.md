#  AI Document Assistant

An AI-powered document assistant that allows users to upload PDF files, generate concise summaries, and ask questions based on the document content using Retrieval-Augmented Generation (RAG).

---

##  Features

*  Upload PDF documents
*  Generate AI-powered summaries
*  Ask questions about the uploaded document
*  Semantic search using FAISS Vector Database
*  Context-aware responses using Google's Gemini API
*  Interactive Streamlit web interface

---

##  Tech Stack

* Python
* Streamlit
* Google Gemini API
* LangChain
* FAISS
* PyMuPDF (fitz)
* Sentence Transformers
* Hugging Face Embeddings

---

##  Project Structure

```
AI-Document-Assistant/
│
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
├── .env
│
├── utils/
│   ├── pdf_loader.py
│   ├── summarizer.py
│   ├── chatbot.py
│   ├── vector_store.py
│   └── prompts.py
```

---

##  Installation

### Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/AI-Document-Assistant.git
```

### Navigate to the project

```bash
cd AI-Document-Assistant
```

### Create a virtual environment

```bash
python -m venv venv
```

### Activate the virtual environment

Windows

```bash
venv\Scripts\activate
```

macOS/Linux

```bash
source venv/bin/activate
```

### Install dependencies

```bash
pip install -r requirements.txt
```

---

##  Environment Variables

Create a `.env` file in the project root.

```env
GOOGLE_API_KEY=YOUR_GEMINI_API_KEY
```

---

##  Run the Application

```bash
streamlit run app.py
```

---

##  Application Workflow

1. Upload a PDF.
2. Generate an AI summary.
3. Build the vector database.
4. Ask questions related to the uploaded document.
5. Receive context-aware AI responses.

---

##  Future Improvements

* Multi-PDF support
* Chat history
* Source citations
* OCR support for scanned PDFs
* Export summaries
* Multiple LLM support (Gemini, Groq, OpenAI)

---

##  Known Limitations

* Requires a valid Google Gemini API key.
* The free Gemini API has request quotas and rate limits.
* Performance depends on the quality of extracted PDF text.

---

##  Author

**Tanishq Wahal**

B.Tech CSE (AI & ML)

Passionate about Artificial Intelligence, Machine Learning, and Data Science.

---

##  If you found this project useful, consider giving it a star!
