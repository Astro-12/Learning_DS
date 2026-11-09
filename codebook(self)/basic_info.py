
import json

filename = "data.json"
try:
    with open(filename, "r") as file:
        data = json.load(file)
    print(f"Successfully loaded {filename}!")
except FileNotFoundError:
    print(f"Error: Could not find {filename} in the current directory.")
    exit()

for customer in data.get("customers", []):

    if customer.get("id"):
        customer['id'] = customer['id'].strip().upper()

    if customer.get("full_name"):
        customer["full_name"] = customer["full_name"].strip().title()

    if customer.get("status"):
        customer["status"] = customer["status"].strip().capitalize()

output_filename = "cleaned_names_status.json"
with open(output_filename, "w") as file:
    json.dump(data, file, indent=4)

print(f"Cleanup complete! Saved updated data to {output_filename}.")
