# storage.py
import os
import json
from cryptography.fernet import Fernet

def generate_key():
    return Fernet.generate_key()

def load_key():
    if os.path.exists("secret.key"):
        with open("secret.key", "rb") as key_file:
            return key_file.read()
    else:
        key = generate_key()
        with open("secret.key", "wb") as key_file:
            key_file.write(key)
        return key

def encrypt_password(password):
    fernet = Fernet(load_key())
    return fernet.encrypt(password.encode()).decode()

def decrypt_password(encrypted_password):
    fernet = Fernet(load_key())
    return fernet.decrypt(encrypted_password.encode()).decode()

def save_password_to_file(username, site, password):
    filename = "passwords.json"
    entry = {
        "site": site,
        "username": username,
        "password": encrypt_password(password)
    }

    if os.path.exists(filename):
        with open(filename, "r") as file:
            data = json.load(file)
    else:
        data = []

    data.append(entry)
    with open(filename, "w") as file:
        json.dump(data, file, indent=4)

def retrieve_password(site):
    filename = "passwords.json"
    if not os.path.isfile(filename):
        return None

    with open(filename, "r") as file:
        data = json.load(file)
        for entry in data:
            if entry["site"] == site:
                username = entry["username"]
                password = decrypt_password(entry["password"])
                return username, password
    return None
