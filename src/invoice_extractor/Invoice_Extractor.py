
import os
import json
import traceback
import asyncio
import streamlit as st
from langchain_ollama.chat_models import ChatOllama
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from utils import read_file  # Function to read and extract text from the uploaded file
from extractors import extract_invoice_data, save_llm_response  # Import functions for extraction and saving
from convert import convert_llm_responses_to_json  # Import the conversion function

# Initialize ChatOllama
llm = ChatOllama(model="llama3.1", temperature=0.3)

# Define the prompt template for invoice data extraction
invoice_prompt = PromptTemplate(
    input_variables=["invoice_text"],
    template="""
        You are an invoice data extractor. Please extract the relevant information from the following invoice text:
        {invoice_text}
        Return the extracted information in a structured JSON format with the following keys:
        - InvoiceDetails
        - CustomerInfo
        - SellerInfo
        - ShippingInfo
        - ProductInfo
        - TaxInfo
        Make sure the JSON is valid and formatted correctly.
    """
)

# Create the chain for invoice extraction
invoice_chain = LLMChain(llm=llm, prompt=invoice_prompt, output_key="extracted_data", verbose=True)

# Define the prompt template for answering questions based on extracted data
question_prompt = PromptTemplate(
    input_variables=["context", "question"],
    template="""
    You are a virtual assistant knowledgeable about invoices.
    Here is the invoice data:
    {context}
    Based on the above data, answer the following question: {question}
    """
)

# Create the LLMChain for answering questions
llm_chain = LLMChain(llm=llm, prompt=question_prompt)

# Streamlit app setup
st.title("Invoice Data Extractor")

# File uploader
uploaded_files = st.file_uploader("Upload Invoices (PDF or TXT)", type=["pdf", "txt"], accept_multiple_files=True)

# Dictionary to hold extracted data for the current session
extracted_data_dict = {}

async def process_file(uploaded_file):
    """Process a single uploaded file asynchronously."""
    text = read_file(uploaded_file)
    extracted_data = extract_invoice_data(text)
    if extracted_data:
        filename = uploaded_file.name.split(".")[0]
        save_llm_response(extracted_data, filename)
        return uploaded_file.name, extracted_data
    return uploaded_file.name, None

async def process_uploaded_files(files):
    """Process uploaded files and extract invoice data asynchronously."""
    tasks = [process_file(uploaded_file) for uploaded_file in files]
    results = await asyncio.gather(*tasks)

    for filename, extracted_data in results:
        if extracted_data:
            extracted_data_dict[filename] = extracted_data

    # Convert all responses to JSON after processing
    convert_llm_responses_to_json()

# q&a function
def answer_query(question: str, extracted_data_dict: dict) -> str:
    """
    Function to get an answer to a user query based on extracted invoice data.
    :param question: The user's question.
    :param extracted_data_dict: Dictionary of extracted data for the session.
    :return: The response from the LLM.
    """
    try:
        # Combine all extracted data into a single context for the LLM
        context = "\n".join([f"File: {file_name}\nData: {json.dumps(data)}"
                             for file_name, data in extracted_data_dict.items()])

        # Use the LLMChain to format the prompt and get the response
        response = llm_chain.run({"context": context, "question": question})

        return response

    except Exception as e:
        raise Exception(f"Error in answering query: {e}")

if uploaded_files:
    try:
        asyncio.run(process_uploaded_files(uploaded_files))
        st.success("All files processed successfully.")

    except Exception as e:
        st.error(f"An error occurred while processing the invoices: {e}")
        traceback.print_exc()

# Question/Answer Section
st.subheader("Ask Questions About the Invoice Data")

if extracted_data_dict:
    question = st.text_input("Enter your question:")
    
    if st.button("Get Answer"):
        try:
            response = answer_query(question, extracted_data_dict)
            st.text_area("Answer", value=response, height=300)
        except Exception as e:
            st.error(f"An error occurred while getting the answer: {e}")
            traceback.print_exc()


