
import json
import re

filename = "cleaned_duplicated.json"
with open(filename, "r") as file:
    data = json.load(file)

for customer in data.get("customers", []):
    purchase_history = customer.get("purachase_history")

    if purchase_history and isinstance(purchase_history, dict):
        raw_spent = purchase_history.get('total_spent')

        if raw_spent is not None:
            if isinstance(raw_spent, (int, float)):
                purchase_history["total_spent"] = float(raw_spent)

            elif isinstance(raw_spent, str):
        # Regex pattern: look for digits, an optional decimal point, and more digits
        match = re.search(r"\d+\.\d+|\d+", raw_spent)

        if match:
          # Extract the matched number string and convert to float
          purchase_history["total_spent"] = float(match.group())
        else:
          # Fallback if no number is found
          purchase_history["total_spent"] = 0.0
  else:
    # If purchase_history was null, give them a clean default structure
    customer["purchase_history"] = {"total_spent": 0.0, "items_bought": []}

# 3. Save progress
output_filename = "cleaned_spent.json"
with open(output_filename, "w") as file:
  json.dump(data, file, indent=4)

print("Total spent normalization complete! All values converted to clean floats.")
