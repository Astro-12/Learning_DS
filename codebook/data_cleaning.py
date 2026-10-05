import json

def clean_data(data):
    data["users"] = [user for user in data["users"] if user['name'.strip()]]
    
data = json.load(open("data2.json"))
data = clean_data(data)
json.dump(data, open("cleaned_data2.json", "w"), index = 4)
print('Data has been cleaned.')
