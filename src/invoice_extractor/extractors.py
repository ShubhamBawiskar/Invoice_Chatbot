# *************************************
# import json
# import os
# import traceback
# from langchain_ollama.chat_models import ChatOllama
# from langchain.prompts import PromptTemplate
# from langchain.chains import LLMChain

# # Initialize ChatOllama
# llm = ChatOllama(model="llama3.1", temperature=0.3)

# # Your template for invoice data extraction
# template = """
#     You are an invoice data extractor. Please extract the relevant information from the following invoice text:
#     {invoice_text}
#     Return the extracted information in a structured JSON format with the following keys:
#     - InvoiceDetails
#     - CustomerInfo
#     - SellerInfo
#     - ShippingInfo
#     - ProductInfo
#     - TaxInfo

#     Make sure the JSON is valid and formatted correctly. Don't give any extra character or any extra explanation other than the extracted data, don't even give it in strings.
#     """

# # Create a PromptTemplate
# invoice_prompt = PromptTemplate(
#     input_variables=["invoice_text"],
#     template=template
# )

# # Create the chain for invoice extraction
# invoice_chain = LLMChain(llm=llm, prompt=invoice_prompt, output_key="extracted_data", verbose=True)

# def extract_invoice_data(invoice_text: str):
#     """
#     Function to extract invoice data using LLMChain.
#     :param invoice_text: The text extracted from the invoice
#     :return: The raw response from the LLM (could be JSON or plain text)
#     """
#     try:
#         # Pass the extracted text to the invoice chain
#         response = invoice_chain({"invoice_text": invoice_text})

#         # Get the extracted data from the response
#         extracted_data = response.get("extracted_data")

#         if extracted_data:
#             # Return the raw extracted data (as-is, without parsing to JSON)
#             return extracted_data

#         return None

#     except Exception as e:
#         traceback.print_exc()
#         raise Exception("Error during invoice extraction")

# def save_llm_response(response_data: str, filename: str):
#     """
#     Function to save the extracted LLM response into the 'llm_responses' folder.
#     :param response_data: The raw response (string) from LLM
#     :param filename: The name of the file (without extension) to save the response
#     """
#     folder = "llm_responses"
#     os.makedirs(folder, exist_ok=True)  # Create the folder if it doesn't exist
#     filepath = os.path.join(folder, f"{filename}.txt")  # Save as a text file

#     # Save the raw response as a text file
#     with open(filepath, 'w') as f:
#         f.write(response_data)

#     return filepath
# ****************************************


import os
import traceback
from langchain_ollama.chat_models import ChatOllama
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

# Initialize ChatOllama
llm = ChatOllama(model="llama3.1", temperature=0.3)

# Your template for invoice data extraction
template = """
    You are an invoice data extractor. Please extract the relevant information from the following invoice text:
    {invoice_text}
    Return the extracted information in a structured JSON format with the following keys:
    - InvoiceDetails
    - CustomerInfo
    - SellerInfo
    - ShippingInfo
    - ProductInfo
    - TaxInfo

    Make sure the JSON is valid and formatted correctly. Don't give any extra character or any extra explanation other than the extracted data, don't even give it in strings.
    """

# Create a PromptTemplate
invoice_prompt = PromptTemplate(
    input_variables=["invoice_text"],
    template=template
)

# Create the chain for invoice extraction
invoice_chain = LLMChain(llm=llm, prompt=invoice_prompt, output_key="extracted_data", verbose=True)

def extract_invoice_data(invoice_text: str):
    """
    Function to extract invoice data using LLMChain.
    :param invoice_text: The text extracted from the invoice
    :return: The raw response from the LLM (could be JSON or plain text)
    """
    try:
        # Pass the extracted text to the invoice chain
        response = invoice_chain({"invoice_text": invoice_text})

        # Get the extracted data from the response
        extracted_data = response.get("extracted_data")

        if extracted_data:
            return extracted_data  # Return the raw extracted data (as-is)

        return None

    except Exception as e:
        traceback.print_exc()
        raise Exception("Error during invoice extraction")

def save_llm_response(response_data: str, filename: str):
    """
    Function to save the extracted LLM response into the 'llm_responses' folder.
    :param response_data: The raw response (string) from LLM
    :param filename: The name of the file (without extension) to save the response
    """
    folder = "llm_responses"
    os.makedirs(folder, exist_ok=True)  # Create the folder if it doesn't exist
    filepath = os.path.join(folder, f"{filename}.txt")  # Save as a text file

    # Save the raw response as a text file
    with open(filepath, 'w') as f:
        f.write(response_data)

    return filepath
