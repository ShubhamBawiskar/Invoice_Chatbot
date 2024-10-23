# import os
# import json

# def convert_llm_responses_to_json():
#     """
#     Convert the saved LLM response files to JSON.
#     Only considers files saved in the 'llm_responses' directory during the current session.
#     """
#     # Define the directory for raw responses and JSON output
#     raw_responses_dir = "llm_responses"  # Ensure this matches your structure
#     json_output_dir = "invoice_json"  # Output directory for JSON files

#     # Create the JSON output directory if it doesn't exist
#     os.makedirs(json_output_dir, exist_ok=True)

#     # List all files in the raw responses directory
#     for filename in os.listdir(raw_responses_dir):
#         if filename.endswith(".txt"):  # Assuming raw responses are saved as .txt files
#             file_path = os.path.join(raw_responses_dir, filename)

#             with open(file_path, "r") as file:
#                 raw_data = file.read()

#             # Attempt to extract JSON from the raw data
#             json_start = raw_data.find('{')  # Find the first '{' character
#             json_end = raw_data.rfind('}')  # Find the last '}' character

#             if json_start != -1 and json_end != -1 and json_end > json_start:
#                 json_str = raw_data[json_start:json_end + 1]  # Extract the valid JSON string
#                 try:
#                     # Load the JSON string to ensure it's valid
#                     extracted_json = json.loads(json_str)

#                     # If there are additional characters after the JSON object, handle them
#                     additional_data = raw_data[json_end + 1:].strip()
#                     if additional_data:
#                         print(f"Warning: Extra data found after JSON in {filename}. Data: {additional_data}")

#                     # Define the output path for the JSON file
#                     json_filename = f"{os.path.splitext(filename)[0]}.json"
#                     json_file_path = os.path.join(json_output_dir, json_filename)

#                     # Save the valid JSON data to a file
#                     with open(json_file_path, "w") as json_file:
#                         json.dump(extracted_json, json_file, indent=4)

#                     print(f"Converted {filename} to {json_filename} and saved in {json_output_dir}")

#                 except json.JSONDecodeError as e:
#                     print(f"Failed to decode JSON from {filename}: {e}")
#                 except Exception as e:
#                     print(f"An error occurred while saving JSON for {filename}: {e}")
#             else:
#                 print(f"No valid JSON found in {filename}")

#     print("Finished processing raw responses.")

# # Example usage
# if __name__ == "__main__":
#     convert_llm_responses_to_json()

# *****************************************

import os
import json

def convert_llm_responses_to_json():
    """
    Convert the saved LLM response files to JSON.
    Only considers files saved in the 'llm_responses' directory during the current session.
    """
    # Define the directory for raw responses and JSON output
    raw_responses_dir = "llm_responses"  # Ensure this matches your structure
    json_output_dir = "invoice_json"  # Output directory for JSON files

    # Create the JSON output directory if it doesn't exist
    os.makedirs(json_output_dir, exist_ok=True)

    # List all files in the raw responses directory
    for filename in os.listdir(raw_responses_dir):
        if filename.endswith(".txt"):  # Assuming raw responses are saved as .txt files
            file_path = os.path.join(raw_responses_dir, filename)

            with open(file_path, "r") as file:
                raw_data = file.read()

            # Attempt to extract JSON from the raw data
            json_start = raw_data.find('{')  # Find the first '{' character
            json_end = raw_data.rfind('}')  # Find the last '}' character

            if json_start != -1 and json_end != -1 and json_end > json_start:
                json_str = raw_data[json_start:json_end + 1]  # Extract the valid JSON string
                try:
                    # Load the JSON string to ensure it's valid
                    extracted_json = json.loads(json_str)

                    # If there are additional characters after the JSON object, handle them
                    additional_data = raw_data[json_end + 1:].strip()
                    if additional_data:
                        print(f"Warning: Extra data found after JSON in {filename}. Data: {additional_data}")

                    # Define the output path for the JSON file
                    json_filename = f"{os.path.splitext(filename)[0]}.json"
                    json_file_path = os.path.join(json_output_dir, json_filename)

                    # Save the valid JSON data to a file
                    with open(json_file_path, "w") as json_file:
                        json.dump(extracted_json, json_file, indent=4)

                    print(f"Converted {filename} to {json_filename} and saved in {json_output_dir}")

                except json.JSONDecodeError as e:
                    print(f"Failed to decode JSON from {filename}: {e}")
                except Exception as e:
                    print(f"An error occurred while saving JSON for {filename}: {e}")
            else:
                print(f"No valid JSON found in {filename}")

    print("Finished processing raw responses.")

# Example usage
if __name__ == "__main__":
    convert_llm_responses_to_json()

