#to remove the duplicated entries with the help of customer id
import json

filename = "data.json"
with open(filename, "r") as file:
    data = json.load(file)

seen_ids = set()
unique_customers = []

for customer in data.get("customers", []):
    cust_id = customer.get("id")

    if cust_id not in seen_ids:
        seen_ids.add(cust_id)
        unique_customers.append(customer)

    else:
        print(f"Duplicate detected and removed: {cust_id}")

data["customers"] = unique_customers

output_filename = "cleaned_duplicated.json"
with open(output_filename, "w") as file:
    json.dump(data, file, indent =4)

print(
    f"Deduplication complete! Total unique records remaining:"
    f" {len(unique_customers)}"
)
