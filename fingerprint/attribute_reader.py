import os
import json

def get_definitions():
    descriptions = []

    for subdir, dirs, files in os.walk("fingerprint/attributes"):
        for file in files:
            if file.endswith(".json"):
                path = os.path.join(subdir, file)
                with open(path) as json_file:
                    json_data = json.load(json_file)
                    descriptions.append(json_data)

    return descriptions

def get_files_and_variables():

    sources = []
    variables = []

    attributes_folder = "fingerprint/attributes"

    for subdir, dirs, files in os.walk(attributes_folder):
        for file in files:
            if file.endswith(".json"):
                path = os.path.join(subdir, file)
                with open(path) as json_file:
                    json_data = json.load(json_file)
                    if len(json_data["files"]) > 0:
                        print(json_data["files"])
                        for f in json_data["files"]:
                            sources.append(os.path.join(subdir, f)[len(attributes_folder) + 1:])
                        variables.append(json_data["variables"])

    return sources,variables

if __name__ == '__main__':
    get_definitions()