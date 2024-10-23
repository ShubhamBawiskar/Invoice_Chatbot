# #************************************
# import streamlit as st
# import traceback
# from utils import read_file  # Function to read and extract text from the uploaded file
# from extractors import extract_invoice_data, save_llm_response  # Import functions for extraction and saving

# # Streamlit app setup
# st.title("Invoice Data Extractor")

# uploaded_file = st.file_uploader("Upload an Invoice (PDF or TXT)", type=["pdf", "txt"])

# if uploaded_file is not None:
#     try:
#         # Ensure the read_file function correctly reads and extracts text from the file
#         text = read_file(uploaded_file)

#         # Extract the invoice data using the LLM
#         extracted_data = extract_invoice_data(text)

#         if extracted_data:
#             # Display the raw extracted data
#             st.text_area("Raw Extracted Data", value=extracted_data, height=300)

#             # Save the response to the folder
#             filename = uploaded_file.name.split(".")[0]  # Use the filename without extension
#             saved_path = save_llm_response(extracted_data, filename)
#             st.success(f"Extracted data has been saved to: {saved_path}")
#         else:
#             st.error("No data extracted from the invoice.")

#     except Exception as e:
#         traceback.print_exc()  # Print the stack trace for debugging
#         st.error(f"An error occurred while processing the invoice: {e}")
# # *********************************


###########################################

###****************************************************
# import streamlit as st
# import traceback
# import json
# from utils import read_file  # Function to read and extract text from the uploaded file
# from extractors import extract_invoice_data, save_llm_response  # Import functions for extraction and saving
# from convert import convert_llm_responses_to_json  # Import the conversion function
# from chat import start_chat

# # Streamlit app setup
# st.title("Invoice Data Extractor")

# uploaded_file = st.file_uploader("Upload an Invoice (PDF or TXT)", type=["pdf", "txt"])

# if uploaded_file is not None:
#     try:
#         # Ensure the read_Extracted data harectly reads and extracts text from the file
#         text = read_file(uploaded_file)

#         # Extract the invoice data using the LLM
#         extracted_data = extract_invoice_data(text)

#         if extracted_data:
            
#             # Save the raw response to the folder
#             filename = uploaded_file.name.split(".")[0]  # Use the filename without extension
#             saved_path = save_llm_response(extracted_data, filename)
#             # st.success(f"Extraction coompleted!")

#             # Convert the raw LLM responses to JSON files
#             convert_llm_responses_to_json()  # Call the function to convert raw responses to JSON

#             if extracted_data:
#                 filename = uploaded_file.name.split(".")[0]
#                 saved_path = save_llm_response(extracted_data, filename)
                
#                 # Start the chat functionality, pointing to the invoice_json folder
#                 start_chat("invoice_json")

#         else:
#             st.error("No data extracted from the invoice.")

#     except Exception as e:
#         st.error(f"An error occurred while processing the invoice: {e}")
#*****************************************************


# # main.py
# import streamlit as st
# import traceback
# import json
# from utils import read_file
# from extractors import extract_invoice_data, save_llm_response
# from convert import convert_llm_responses_to_json
# from chat import start_chat, create_chat_prompt, get_llm_answer  # Import the chat functionality

# # Streamlit app setup
# st.title("Invoice Data Extractor⛏️")

# uploaded_file = st.file_uploader("Upload an Invoice (PDF or TXT)", type=["pdf", "txt"])

# if uploaded_file is not None:
#     try:
#         # Read and extract text from the uploaded file
#         text = read_file(uploaded_file)

#         # Extract the invoice data using the LLM
#         extracted_data = extract_invoice_data(text)

#         if extracted_data:
#             # Save the raw response to the folder
#             filename = uploaded_file.name.split(".")[0]  # Use the filename without extension
#             saved_path = save_llm_response(extracted_data, filename)

#             # Convert the raw LLM responses to JSON files
#             convert_llm_responses_to_json()  # Call the function to convert raw responses to JSON

#             # Start the chat functionality
#             invoice_json_folder = "invoice_json"
#             extracted_invoice_data = start_chat(invoice_json_folder)

#             # Add a prompt for the user to ask questions
#             user_question = st.text_input("Ask a question about the invoice data:")
            
#             if st.button("Get Answer"):
#                 if user_question:
#                     # Create the prompt for the LLM
#                     prompt = create_chat_prompt(user_question, extracted_invoice_data)
                    
#                     # Get the answer from the LLM
#                     answer = get_llm_answer(prompt)
                    
#                     # Display the answer
#                     st.text_area("Answer", value=answer, height=300)
#                 else:
#                     st.error("Please enter a question.")

#         else:
#             st.error("No data extracted from the invoice.")

#     except Exception as e:
#         st.error(f"An error occurred while processing the invoice: {e}")

# ********************************************************

# import streamlit as st
# import traceback
# import json
# from utils import read_file  # Function to read and extract text from the uploaded file
# from extractors import extract_invoice_data, save_llm_response  # Import functions for extraction and saving
# from convert import convert_llm_responses_to_json  # Import the conversion function


# # Streamlit app setup
# st.title("Invoice Data Extractor")

# # Allow uploading multiple PDF files
# uploaded_files = st.file_uploader("Upload Invoices (PDF)", type=["pdf"], accept_multiple_files=True)

# if uploaded_files:
#     for uploaded_file in uploaded_files:
#         try:
#             # Read the content of each uploaded PDF
#             text = read_file(uploaded_file)

#             # Extract the invoice data using the LLM
#             extracted_data = extract_invoice_data(text)

#             if extracted_data:
#                 # Save the raw response to the folder
#                 filename = uploaded_file.name.split(".")[0]  # Use the filename without extension
#                 saved_path = save_llm_response(extracted_data, filename)

#             else:
#                 st.error(f"No data extracted from the invoice: {uploaded_file.name}")

#         except Exception as e:
#             st.error(f"An error occurred while processing the invoice: {e}")

#     # Convert the raw LLM responses to JSON files
#     convert_llm_responses_to_json()  # This function can now handle all saved response files


# *************************************

import os
import asyncio
import traceback
import streamlit as st
from utils import read_file
from extractors import process_uploaded_files
from chat import answer_query

# Streamlit app setup
st.title("Invoice Data Extractor")

# File uploader
uploaded_files = st.file_uploader("Upload Invoices (PDF or TXT)", type=["pdf", "txt"], accept_multiple_files=True)

# Dictionary to hold extracted data for the current session
extracted_data_dict = {}

# Main logic for handling uploaded files and user queries
if uploaded_files:
    try:
        asyncio.run(process_uploaded_files(uploaded_files, extracted_data_dict))
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
            st.text_area("Answer", value=response, height=300)  # Display only the 'text' part
        except Exception as e:
            st.error(f"An error occurred while getting the answer: {e}")
            traceback.print_exc()

