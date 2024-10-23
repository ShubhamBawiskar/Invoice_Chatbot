# import os
# import json
# from langchain_ollama.chat_models import ChatOllama
# from langchain.prompts import PromptTemplate
# from langchain.chains import LLMChain

# # Initialize ChatOllama
# llm = ChatOllama(model="llama3.1", temperature=0.7)

# # Function to load all JSON data
# def load_invoice_data(invoice_json_folder):
#     all_data = {}
#     for filename in os.listdir(invoice_json_folder):
#         if filename.endswith('.json'):
#             with open(os.path.join(invoice_json_folder, filename), 'r') as file:
#                 data = json.load(file)
#                 all_data.update(data)  # Combine data from multiple files
#     return all_data

# def create_chat_prompt(user_question, extracted_data):
#     """
#     Create a prompt for the LLM based on user question and invoice data.

#     :param user_question: The user's question
#     :param extracted_data: The structured data extracted from the invoices
#     :return: A formatted prompt for the LLM
#     """
#     prompt_template = f"""
#     You are a virtual assistant knowledgeable about invoices. 
#     Here is the invoice data: {json.dumps(extracted_data)}
    
#     Based on the above data, answer the following question: {user_question}
#     """
#     return prompt_template

# def get_llm_answer(prompt):
#     """
#     Get an answer from the LLM based on the generated prompt.

#     :param prompt: The prompt to send to the LLM
#     :return: The response from the LLM
#     """
#     response = llm({"prompt": prompt})
#     return response.get("response", "Sorry, I couldn't understand that.")

# def start_chat(invoice_json_folder):
#     extracted_data = load_invoice_data(invoice_json_folder)

#     return extracted_data  # Return the extracted data for further processing

# ********************************************************

# src/chat.py
import json
import os
from langchain_ollama.chat_models import ChatOllama
from langchain.prompts import PromptTemplate

# Initialize the LLM
llm = ChatOllama(model="llama3.1", temperature=0.7)

def get_invoice_data_as_json(filename):
    """
    Retrieve the invoice data from a JSON file.
    :param filename: The name of the JSON file to read
    :return: Parsed JSON data
    """
    filepath = os.path.join("invoice_json", filename)
    with open(filepath, "r") as file:
        return json.load(file)

def ask_question_about_invoice(invoice_data, question):
    """
    Ask a question about the invoice data using LLM.
    :param invoice_data: The invoice data to refer to
    :param question: The user's question
    :return: The LLM's response
    """
    prompt_template = f"""
        You are a virtual assistant knowledgeable about invoices.
        Here is the invoice data: {json.dumps(invoice_data)}
        User question: {question}
        Please provide a clear and concise answer based on the invoice data.
    """

    # Get the response from LLM
    response = llm(prompt_template)
    return response
