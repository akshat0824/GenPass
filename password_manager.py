import random
import string
import pyperclip
from storage import save_password_to_file, retrieve_password

def generate_password(length, strength_choice):
    if strength_choice == 1:
        chars = string.ascii_lowercase
    elif strength_choice == 2:
        chars = string.ascii_letters
    elif strength_choice == 3:
        chars = string.ascii_letters + string.digits
    elif strength_choice == 4:
        chars = string.ascii_letters + string.digits + string.punctuation
    else:
        raise ValueError("Invalid strength choice")

    password = ''.join(random.choice(chars) for _ in range(length))
    pyperclip.copy(password)
    return password
