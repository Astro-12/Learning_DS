import json

def clean_data(data):
    data["users"] = [user for user in data["users"] if user['name'.strip()]]
    #removing multiple duplicate friends
    for user in data["users"]:
        user["friends"] = list(set(user['friends']))
    #remove inactive users
    data['users'] = [user for user in data['users']if user ['friends']or user['liked_pages']]
    return data

    #removing duplicate pages
    unique_pages = {}
    for page in data['pages']:
        unique_pages[page['id']] = page
    data['pages'] = list(unique_pages.values())
    return data
#load the data
data = json.load(open("data2.json"))
data = clean_data(data)
json.dump(data, open("cleaned_data2.json", "w"), indent = 4)
print('Data has been cleaned successfully.')
