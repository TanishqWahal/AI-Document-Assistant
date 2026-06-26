import fitz

def extract_text_from_pdf(pdf_file):
    """
    Extracts text from a PDF file.

    Args:
        pdf_file (str): The path to the PDF file.

    Returns:
        str: The extracted text from the PDF file.
    """
    document = fitz.open(stream=pdf_file.read(), filetype="pdf")
    text = ""
    for page in document:
        text += page.get_text()+ "\n"
    document.close()
    return text