from datetime import datetime
import json
filename = "data.json"
with open(filename, "r") as file:
  data = json.load(file)
possible_formats = [
    "%m/%d/%Y",  # 04/12/2025 (Month/Day/Year)
    "%Y-%m-%d",  # 2025-12-01 (ISO standard)
    "%b %d, %Y",  # Nov 15, 2025 (Abbreviated Month Day, Year)
    "%Y/%m/%d",  #2026/01/10 (Year/Month/Day with slashes)
    "%d-%m-%Y",  #13-03-2026 (Day-Month-Year)
]
for customer in data.get("customers", []):
  raw_date = customer.get("signup_date")
  parsed_date = None
if raw_date and raw_date != "Invalid date":
    for fmt in possible_formats:
        try:
            dt_obj = datetime.strptime(raw_date, fmt)
            parsed_date = dt_obj.strftime("%Y-%m-%d")
            break
        except ValueError:
            continue
    customer["signup_date"] = parsed_date
with open("cleaned_dates.json","w") as file:
    json.dump(data, file, indent =4)
print("Date standardization complete! Invalid dates safely converted to null.")
