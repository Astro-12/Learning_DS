from datetime import datetime
import json

filename = "data.json"
with open(filename, "r") as file:
  data = json.load(file)

possible formats = [
    "%m/%d/%Y",  # 04/12/2025 (Month/Day/Year)
    "%Y-%m-%d",  # 2025-12-01 (ISO standard)
    "%b %d, %Y",  # Nov 15, 2025 (Abbreviated Month Day, Year)
    "%Y/%m/%d",  #2026/01/10 (Year/Month/Day with slashes)
    "%d-%m-%Y",  #13-03-2026 (Day-Month-Year)
]
