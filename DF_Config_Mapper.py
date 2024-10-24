import json
import pandas as pd
import json
import csv
import os
from datetime import datetime
def convert_timestamp(timestamp):
    return datetime.utcfromtimestamp(timestamp).strftime('%Y-%m-%d %H:%M:%S')

def function_one():
    for path, dir, files in os.walk(input_path_po):
        if len(files) == 0:
            print("Please place json file in the correct format into the /input folder")
        for file in files:
            if file.endswith(".tgz") or file.endswith(".zip"):
                try:
                    print("zip/tgz file support to be added later: " + file)
                except Exception as err:
                    print(f'Error processing {input_path_po + file} {err}')
            elif file.endswith(".json"):
                json_file = input_path_po + file
                with open(json_file, 'r') as f:
                    json_data = json.load(f)
                protected_objects = json_data["protectedObjects"]
                df = pd.json_normalize(protected_objects)
            csv_file = output_path + 'PO_Config.csv'
            df.to_csv(csv_file, index=False)
            print(f'Protected Objects configuration was successfully exported to {json_file}')
            return 'Succesfully executed'

def function_two():
    for path, dir, files in os.walk(input_path_st):
        if len(files) == 0:
            print("Please place json file in the correct format into the /input folder")
        for file in files:
            if file.endswith(".tgz") or file.endswith(".zip"):
                try:
                    print("zip/tgz file support to be added later: " + file)
                except Exception as err:
                    print(f'Error processing {input_path_st + file} {err}')
            elif file.endswith(".json"):
                json_file = input_path_st + file
                with open(json_file, 'r') as f:
                    data = json.load(f)
                policy_templates = data["policyTemplates"]
                csv_columns = ['Name', 'Version', 'Creator', 'Protections', 'TemplateText', 'TemplateObject', 'CreatedTimestamp']
                csv_file = output_path + 'ST_Config.csv'
                with open(csv_file, 'w', newline='') as csvfile:
                    writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
                    writer.writeheader()
                    for template in policy_templates:
                        row = {
                            'Name': template['id']['name'],
                            'Version': template['id']['version'],
                            'Creator': template['metadata']['creator'],
                            'Protections': json.dumps(template['protections']),  # Convert protections to JSON string
                            'TemplateText': template['templateText'],
                            'TemplateObject': template['templateObject'],
                            'CreatedTimestamp': convert_timestamp(template['createdTimestamp'])
                        }
                        writer.writerow(row)
                    # Add more logic for function two
                    print(f'Security Templates configuration was successfully exported to {json_file}')
                    return 'Succesfully executed'

def wizard_menu():
    print("Welcome to the DF config mapper script!")
    print("Please select one of the following options:")
    print("1. Get CSV for Protected Objects configuration")
    print("2. Get CSV for Security Template configuration")
    print("3. Get CSV for all the JSON files")
    
    # Get user's selection
    choice = input("Enter the number of your choice (1, 2 or 3): ")

    # Call the appropriate function based on the user's selection
    if choice == '1':
        result = function_one()
    elif choice == '2':
        result = function_two()
    elif choice == '3':
        result = function_one()
        result = function_two()
    else:
        print("Invalid selection. Please choose 1, 2 or 3.")
        return wizard_menu()  # Re-run the menu if the input is invalid

    # Print the result from the selected function
    print(f"Result: {result}")



# Run the wizard menu
input_path_po = "./input_po/"
input_path_st = "./input_st/"
output_path = "./output/"
replaceExistingFile = False
wizard_menu()