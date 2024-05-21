import json
import re

#recursively find values of a specific key in JSON data
def find_values(id, json_repr):
    results = []

    def _decode_dict(a_dict):
        try:
            results.append(a_dict[id])
        except KeyError:
            pass
        return a_dict

    json.loads(json.dumps(json_repr), object_hook=_decode_dict)  # Return value is ignored.
    return results

#main function to extract text from the JSON file
def extract_text_from_json(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)
    #holds all the text we find
    texts = []
    #recursively find all 'text' values
    for text in find_values('text', data):
        if isinstance(text, list):  # If 'text' is a list of items
            texts.extend(text)
        else:
            texts.append(text)
    #join texts with a space between each item
    joined_text = ' '.join(texts)

    #use regex to replace multiple spaces with a single space
    cleaned_text = re.sub(r'\s+', ' ', joined_text)

    return cleaned_text
json_file_path = 'draft_content.json'
output_text_file = 'path_to_output_text_file.txt'

# Call the function and save the results to a file
extracted_text = extract_text_from_json(json_file_path)
with open(output_text_file, 'w', encoding='utf-8') as file:
    file.write(extracted_text)

print(f"Text has been extracted to {output_text_file}")
