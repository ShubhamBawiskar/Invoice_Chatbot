# import PyPDF2

# def read_file(file):
#     if file.name.endswith(".pdf"):
#         try:
#             pdf_reader = PyPDF2.PdfReader(file)
#             text = ""
#             for page in pdf_reader.pages:
#                 text += page.extract_text()
#             return text
#         except Exception as e:
#             raise Exception("Error reading the PDF file")
    
#     elif file.name.endswith(".txt"):
#         return file.read().decode("utf-8")
    
#     else:
#         raise Exception("Unsupported file format. Only PDF and text files are supported.")




import PyPDF2
import io

def read_file(uploaded_file):
    """
    Read the uploaded invoice file and extract text from it.
    
    :param uploaded_file: Uploaded file (PDF or TXT)
    :return: Extracted text from the invoice
    """
    if uploaded_file.type == "application/pdf":
        # If the file is a PDF
        reader = PyPDF2.PdfReader(uploaded_file)
        text = ""
        for page in reader.pages:
            text += page.extract_text() + "\n"
        return text.strip()
    
    elif uploaded_file.type == "text/plain":
        # If the file is a TXT
        return uploaded_file.getvalue().decode("utf-8").strip()

    return ""
