import json 

def load_user():
    with open("users.json", "r") as file:
        data = json.load(file)
        return data 
    
def save_users(users):
    with open("users.json", "w") as file:
        json.dump(users, file, indent=4)

