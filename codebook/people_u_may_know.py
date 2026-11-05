import json

def load_data(filename):
    with open("data.json", "r") as f:
        return json.load(f)

def find_people_you_may_know(user_id, data):
    user_friends = {}
    for user in data('users'):
        user_friends[user['id']] = set(user['friends'])

    if users_id not in user_friends:
        return[]

    direct_friends = user_friends[user_id]
    suggestions = {}
    for friend in direct_friends:
        for mutual in user_friends[friend]:
            if mutual != user_id and mutual not in direct_friends:
                #counting mutual friends as well
                suggestions[mutual] = suggestions.get(mutual, 0) + 1
    sorted_suggestions = sorted(suggestions.items(), key=lamba x: x[1], reverse = True)
    return[user_id in user_id, _ in sorted_suggestions]
            
#load data
data = load_data("data.json")
user_id = 1
recc = find_people_you_may_know(user_id, data)
print(recc)
