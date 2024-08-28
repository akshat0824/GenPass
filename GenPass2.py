import tkinter as tk
from tkinter import ttk
import pyperclip
import random
import string
import os


def generate_password(length, strength_choice):
    """Generates a random password based on length and strength choice."""
    strength_desc = ""
    if strength_choice == 1:
        chars = string.ascii_lowercase
        strength_desc = "Low (letters only)"
    elif strength_choice == 2:
        chars = string.ascii_letters
        strength_desc = "Medium (letters and uppercase)"
    elif strength_choice == 3:
        chars = string.ascii_letters + string.digits
        strength_desc = "High (letters and numbers)"
    elif strength_choice == 4:
        chars = string.ascii_letters + string.digits + string.punctuation
        strength_desc = "Very High (letters, numbers, and symbols)"
    else:
        raise ValueError("Invalid strength choice")

    password = ''.join(random.choice(chars) for _ in range(length))
    pyperclip.copy(password)
    return password, strength_desc


def save_password_to_file(username, site, password):
    """Saves the password to a file. Just appends it if the file already exists."""
    filename = "passwords.txt"
    entry = f"Site: {site}\nUsername: {username}\nPassword: {password}\n\n"

    # Append to the file
    with open(filename, "a") as file:
        file.write(entry)
    print(f"Password saved to '{filename}'.")


def retrieve_password(site):
    """Retrieves the password for a given site from the file."""
    filename = "passwords.txt"
    if not os.path.isfile(filename):
        return None

    with open(filename, "r") as file:
        entries = file.read().split("\n\n")
        for entry in entries:
            if entry.startswith(f"Site: {site}"):
                lines = entry.split("\n")
                username = lines[1].split(": ")[1]
                password = lines[2].split(": ")[1]
                return username, password
    return None


def create_gui():


    def generate_password_gui():
        try:
            length = int(length_entry.get())
            strength_choice = strength_var.get()
            password, strength_desc = generate_password(length, strength_choice)
            password_display.config(text=f"Generated Password: {password}")
            strength_display.config(text=f"Password Strength: {strength_desc}")
        except ValueError as e:
            password_display.config(text=f"Error: {e}")
            strength_display.config(text="")

    def save_password_gui():
        username = username_entry.get()
        site = site_entry.get()
        password = password_display.cget("text").replace("Generated Password: ", "")
        if username and site and password:
            save_password_to_file(username, site, password)
            status_display.config(text="Password saved successfully.", fg="green")
        else:
            status_display.config(text="Error: Missing information", fg="red")

    def fetch_password_gui():
        site = site_entry.get()
        result = retrieve_password(site)
        if result:
            username, password = result
            result_display.config(text=f"Username: {username}\nPassword: {password}", fg="blue")
        else:
            result_display.config(text="No credentials found for the specified site", fg="red")

    # Create the main window
    window = tk.Tk()
    window.title("Password Manager")
    window.geometry("600x500")  # Set the size of the window
    window.configure(bg="#f0f0f0")

    # Create labels and entry fields with larger text and padding
    font = ("Helvetica", 12)
    entry_width = 30

    length_label = tk.Label(window, text="Password Length:", font=font, bg="#f0f0f0")
    length_entry = tk.Entry(window, font=font, width=entry_width, bd=2, relief="solid")
    strength_label = tk.Label(window, text="Password Strength:", font=font, bg="#f0f0f0")

    # Create dropdown for password strength
    strength_var = tk.IntVar()
    strength_options = {
        "Low (letters only)": 1,
        "Medium (letters and uppercase)": 2,
        "High (letters and numbers)": 3,
        "Very High (letters, numbers, and symbols)": 4
    }
    strength_dropdown = ttk.Combobox(window, textvariable=strength_var, values=list(strength_options.keys()), font=font,
                                     width=entry_width)
    strength_dropdown.set("Select Strength")

    username_label = tk.Label(window, text="Username:", font=font, bg="#f0f0f0")
    username_entry = tk.Entry(window, font=font, width=entry_width, bd=2, relief="solid")
    site_label = tk.Label(window, text="Site:", font=font, bg="#f0f0f0")
    site_entry = tk.Entry(window, font=font, width=entry_width, bd=2, relief="solid")

    # Labels to display the generated password, strength, and results
    password_display = tk.Label(window, text="Generated Password: ", font=font, bg="#f0f0f0")
    strength_display = tk.Label(window, text="Password Strength: ", font=font, bg="#f0f0f0")
    result_display = tk.Label(window, text="Result:", font=font, bg="#f0f0f0")
    status_display = tk.Label(window, text="", font=font, bg="#f0f0f0")


    button_font = ("Helvetica", 12, "bold")
    button_width = 20

    generate_button = tk.Button(window, text="Generate Password", command=generate_password_gui, font=button_font,
                                width=button_width, bg="#4CAF50", fg="white", bd=0, relief="raised")
    save_button = tk.Button(window, text="Save Password", command=save_password_gui, font=button_font,
                            width=button_width, bg="#2196F3", fg="white", bd=0, relief="raised")
    fetch_button = tk.Button(window, text="Fetch Password", command=fetch_password_gui, font=button_font,
                             width=button_width, bg="#FF5722", fg="white", bd=0, relief="raised")

    # Grid layout with padding
    length_label.grid(row=0, column=0, padx=20, pady=10, sticky="e")
    length_entry.grid(row=0, column=1, padx=20, pady=10)
    strength_label.grid(row=1, column=0, padx=20, pady=10, sticky="e")
    strength_dropdown.grid(row=1, column=1, padx=20, pady=10)
    username_label.grid(row=2, column=0, padx=20, pady=10, sticky="e")
    username_entry.grid(row=2, column=1, padx=20, pady=10)
    site_label.grid(row=3, column=0, padx=20, pady=10, sticky="e")
    site_entry.grid(row=3, column=1, padx=20, pady=10)
    generate_button.grid(row=4, column=0, columnspan=2, padx=20, pady=10)
    save_button.grid(row=5, column=0, columnspan=2, padx=20, pady=10)
    fetch_button.grid(row=6, column=0, columnspan=2, padx=20, pady=10)
    password_display.grid(row=7, column=0, columnspan=2, padx=20, pady=10)
    strength_display.grid(row=8, column=0, columnspan=2, padx=20, pady=10)
    result_display.grid(row=9, column=0, columnspan=2, padx=20, pady=10)
    status_display.grid(row=10, column=0, columnspan=2, padx=20, pady=10)

    # Start the event loop
    window.mainloop()


def print_welcome_message():
    """Prints a welcome message."""
    print("Welcome to the Password Manager!")


if __name__ == "__main__":
    print_welcome_message()
    create_gui()
