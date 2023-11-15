import json


file_path = "api-docs/ehub-backend-api-docs.json"
loaded_data = load_json_file(file_path)
def load_json_file(loaded_data):
    with open(loaded_data, 'r') as json_file:
        data = json.load(loaded_data)
    return data
