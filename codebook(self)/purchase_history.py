
import json
import re

filename = "cleaned_duplicated.json"
with open(filename, "r") as file:
    data = json.load(file)

for customer in data.get("customers", []):
    purchase_history = customer.get("purachase_history")

    if purchase_history and isinstance(purchase_history, dict):
        raw_spent = purchase_history
