import pdfplumber
from io import BytesIO

def extract_text_from_pdf(file) -> str:
    text = ""
    with pdfplumber.open(BytesIO(file.read())) as pdf:
        for page in pdf.pages:
            text += page.extract_text() + "\n"
    return text
