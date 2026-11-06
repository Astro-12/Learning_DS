import json

def load_data(filename):
    with open(filename, "r") as file:
        return json.load(file)

def find_pages_you_might_like(user_id, data):

    user_pages = {}
    for user in data["users"]:
        user_pages[user["id"]] = set(user["liked_pages"])# dict: user_pages, key: user['id'], value[set(user['liked_pages'])]
        
    if user_id not in user_pages:
        return []
    
    user_liked_pages = user_pages[user_id]
    page_suggestions = {}
    
    for other_user, pages in user_pages.items():
        if other_user != user_id:
            shared_pages = user_liked_pages.intersection(pages)
            for page in pages:
                if page not in user_liked_pages:
                    page_suggestions[page] = page_suggestions.get(page, 0) + len(shared_pages)
                    
    sorted_pages = sorted(page_suggestions.items(), key=lambda x: x[1], reverse=True)
    return [page_id for page_id, _ in sorted_pages]

# Load data
data = load_data("massive_data.json")
user_id = 1  # Example: Finding recommendations for Amit
page_recommendations = find_pages_you_might_like(user_id, data)
print(f"Pages You Might Like for User {user_id}: {page_recommendations}")
