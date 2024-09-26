# user_auth.py
import hashlib
import json
import os

def save_user_credentials(username, password):
    filename = "users.json"
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    entry = {"username": username, "password": hashed_password}

    if os.path.exists(filename):
        with open(filename, "r") as file:
            data = json.load(file)
    else:
        data = []

    data.append(entry)
    with open(filename, "w") as file:
        json.dump(data, file, indent=4)

def is_username_taken(username):
    filename = "users.json"
    if not os.path.isfile(filename):
        return False

    with open(filename, "r") as file:
        data = json.load(file)
        for user in data:
            if user["username"] == username:
                return True
    return False

def verify_user(username, password):
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    filename = "users.json"
    if not os.path.isfile(filename):
        return False

    with open(filename, "r") as file:
        data = json.load(file)
        for user in data:
            if user["username"] == username and user["password"] == hashed_password:
                return True
    return False
