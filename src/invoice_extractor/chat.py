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

# import json
# from langchain_ollama.chat_models import ChatOllama

# # Initialize ChatOllama
# llm = ChatOllama(model="llama3.1", temperature=0.7)

# def answer_query(question: str, extracted_data_dict: dict) -> str:
#     """
#     Function to get an answer to a user query based on extracted invoice data.
#     :param question: The user's question.
#     :param extracted_data_dict: Dictionary of extracted data for the session.
#     :return: The response from the LLM.
#     """
#     try:
#         # Combine all extracted data into a single context for the LLM
#         context = "\n".join([f"File: {file_name}\nData: {json.dumps(data)}" 
#                               for file_name, data in extracted_data_dict.items()])

#         # Prepare the prompt
#         prompt_template = f"""
#         You are a virtual assistant knowledgeable about invoices.
#         Here is the invoice data:
#         {context}
#         Based on the above data, answer the following question: {question}
#         """

#         # Get the response from the LLM
#         response = llm.invoke(prompt_template)
#         return response

#     except Exception as e:
#         raise Exception(f"Error in answering query: {e}")



# import json
# from langchain_ollama.chat_models import ChatOllama
# from langchain.prompts import PromptTemplate

# # Initialize ChatOllama
# llm = ChatOllama(model="llama3.1", temperature=0.7)

# def answer_query(question: str, extracted_data_dict: dict) -> str:
#     """
#     Function to get an answer to a user query based on extracted invoice data.
#     :param question: The user's question.
#     :param extracted_data_dict: Dictionary of extracted data for the session.
#     :return: The response from the LLM.
#     """
#     try:
#         # Combine all extracted data into a single context for the LLM
#         context = "\n".join([f"File: {file_name}\nData: {json.dumps(data)}" 
#                               for file_name, data in extracted_data_dict.items()])

#         # Prepare the prompt
#         prompt_template = f"""
#         You are a virtual assistant knowledgeable about invoices.
#         Here is the invoice data:
#         {context}
#         Based on the above data, answer the following question: {question}
#         """

#         prompt_template = PromptTemplate(
#         input_variables=["invoice_data", "question"],
#         template=prompt_template)
        
#         # Get the response from the LLM
#         response = llm.invoke(prompt_template)
#         return response

#     except Exception as e:
#         raise Exception(f"Error in answering query: {e}")




import json
from langchain_ollama.chat_models import ChatOllama
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

# Initialize ChatOllama
llm = ChatOllama(model="llama3.1", temperature=0.7)

# Define the prompt template for LangChain
prompt = PromptTemplate(
    input_variables=["context", "question"],
    template="""
    You are a virtual assistant knowledgeable about invoices.
    Here is the invoice data:
    {context}
    Based on the above data, answer the following question: {question}
    """
)

# Create the LLMChain using the template and the LLM model
llm_chain = LLMChain(llm=llm, prompt=prompt)

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
