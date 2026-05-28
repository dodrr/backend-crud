from database import load_user, save_users


def get_user(name):
    users = load_user()

    for user in users:
        if user["name"] == name:
            return user
        
def add_user(name, age):
    users = load_user()

    new_user = {
        "name": name, 
        "age": age
    }

    users.append(new_user)

    save_users(users)

def update_user(name, age):
    users = load_user()

    for user in users:
        if user["name"] == name:
            user["age"] = age

    save_users(users)


def delete_user(name):
    users = load_user()

    new_user = []

    for user in users:
        if user["name"] != name:
            new_user.append(user)

    save_users(new_user)

def get_all_users():
    users = load_user()

    return users

def count_users():
    users = load_user()

    count = len(users)

    return count





