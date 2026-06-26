import streamlit as st

from utils.pdf_loader import extract_text_from_pdf
from utils.summarizer import generate_summary
from utils.vector_store import create_vector_store
from utils.chatbot import ask_pdf

# ----------------------------------------------------
# PAGE CONFIG
# ----------------------------------------------------

st.set_page_config(
    page_title="AI Document Assistant",
    
    layout="wide"
)

st.title(" AI Document Assistant")
st.write("Upload a PDF, generate its summary, then chat with it.")

st.divider()

# ----------------------------------------------------
# SESSION STATE
# ----------------------------------------------------

if "document_text" not in st.session_state:
    st.session_state.document_text = ""

if "summary" not in st.session_state:
    st.session_state.summary = ""

if "vector_store" not in st.session_state:
    st.session_state.vector_store = None

# ----------------------------------------------------
# PDF UPLOAD
# ----------------------------------------------------

uploaded_file = st.file_uploader(
    "Upload PDF",
    type=["pdf"]
)

if uploaded_file:

    if st.session_state.document_text == "":

        with st.spinner("Extracting PDF Text..."):

            st.session_state.document_text = extract_text_from_pdf(uploaded_file)

        st.success(" PDF Uploaded Successfully!")

# ----------------------------------------------------
# GENERATE SUMMARY
# ----------------------------------------------------

if st.session_state.document_text != "":

    if st.button(" Generate Summary"):

        with st.spinner("Generating Summary..."):

            st.session_state.summary = generate_summary(
                st.session_state.document_text
            )

# ----------------------------------------------------
# DISPLAY SUMMARY
# ----------------------------------------------------

if st.session_state.summary != "":

    st.subheader(" AI Summary")

    st.markdown(st.session_state.summary)

    st.divider()

# ----------------------------------------------------
# CREATE VECTOR DATABASE
# ----------------------------------------------------

if st.session_state.summary != "":

    if st.session_state.vector_store is None:

        if st.button(" Start Chat with PDF"):

            with st.spinner("Creating Vector Database..."):

                try:

                    st.session_state.vector_store = create_vector_store(
                        st.session_state.document_text
                    )

                    st.success("Vector Database Created Successfully!")

                except Exception as e:

                    st.error(f"Error: {e}")

# ----------------------------------------------------
# CHAT SECTION
# ----------------------------------------------------

if st.session_state.vector_store is not None:

    st.subheader(" Ask Questions")

    question = st.text_input(
        "Enter your question"
    )

    if st.button("Ask AI"):

        if question.strip():

            with st.spinner("Thinking..."):

                answer = ask_pdf(
                    question,
                    st.session_state.vector_store
                )

            st.markdown("### AI Answer")

            st.write(answer)

st.divider()

st.caption(" Gemini • LangChain • FAISS • Streamlit")