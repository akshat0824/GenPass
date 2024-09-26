import tkinter as tk
from tkinter import ttk
from password_manager import generate_password, save_password_to_file, retrieve_password
from user_auth import verify_user, save_user_credentials, is_username_taken

def create_login_gui():
    def login_gui():
        username = username_entry.get()
        password = password_entry.get()

        if verify_user(username, password):
            login_window.destroy()
            create_main_gui()  # Proceed to main GUI after successful login
        else:
            status_label.config(text="Invalid username or password", fg="red")

    def register_gui():
        username = username_entry.get()
        password = password_entry.get()
        if username and password:
            if not is_username_taken(username):
                save_user_credentials(username, password)
                status_label.config(text="User registered successfully. You can log in now.", fg="green")
            else:
                status_label.config(text="Username already taken. Please choose another.", fg="red")
        else:
            status_label.config(text="Please enter a username and password.", fg="red")

    login_window = tk.Tk()
    login_window.title("Login")
    login_window.geometry("400x300")  # Set a fixed size
    login_window.configure(bg="#f0f0f0")

    font = ("Helvetica", 12)

    username_label = tk.Label(login_window, text="Username:", font=font, bg="#f0f0f0")
    username_entry = tk.Entry(login_window, font=font)
    password_label = tk.Label(login_window, text="Password:", font=font, bg="#f0f0f0")
    password_entry = tk.Entry(login_window, font=font, show="*")
    status_label = tk.Label(login_window, text="", font=font, bg="#f0f0f0")

    login_button = tk.Button(login_window, text="Login", command=login_gui, font=font)
    register_button = tk.Button(login_window, text="Register", command=register_gui, font=font)

    username_label.grid(row=0, column=0, padx=20, pady=10, sticky="e")
    username_entry.grid(row=0, column=1, padx=20, pady=10)
    password_label.grid(row=1, column=0, padx=20, pady=10, sticky="e")
    password_entry.grid(row=1, column=1, padx=20, pady=10)
    login_button.grid(row=2, column=0, padx=20, pady=10)
    register_button.grid(row=2, column=1, padx=20, pady=10)
    status_label.grid(row=3, columnspan=2, padx=20, pady=10)

    login_window.mainloop()

def create_main_gui():
    def generate_password_gui():
        try:
            length = int(length_entry.get())
            strength_choice_str = strength_var.get()
            strength_choice = strength_options.get(strength_choice_str, None)
            if strength_choice is None:
                raise ValueError("Invalid strength choice selected")
            password = generate_password(length, strength_choice)
            password_display.delete(1.0, tk.END)
            password_display.insert(tk.END, password)
            status_display.config(text="Password copied to clipboard.", fg="blue")
        except ValueError as e:
            password_display.delete(1.0, tk.END)
            password_display.insert(tk.END, f"Error: {e}")
            status_display.config(text="")

    def save_password_gui():
        username = username_entry.get()
        site = site_entry.get()
        password = password_display.get(1.0, tk.END).strip()
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

    def clear_fields():
        length_entry.delete(0, tk.END)
        strength_dropdown.set("Select Strength")
        username_entry.delete(0, tk.END)
        site_entry.delete(0, tk.END)
        password_display.delete(1.0, tk.END)
        result_display.config(text="Result:")
        status_display.config(text="")

    def logout_gui():
        window.destroy()
        create_login_gui()  # Go back to the login screen

    window = tk.Tk()
    window.title("Password Manager")
    window.attributes('-fullscreen', True)
    window.configure(bg="#f0f0f0")

    font = ("Helvetica", 12)
    entry_width = 30

    frame = tk.Frame(window, bg="#f0f0f0")
    frame.place(relx=0.5, rely=0.5, anchor="center")

    length_label = tk.Label(frame, text="Password Length:", font=font, bg="#f0f0f0")
    length_entry = tk.Entry(frame, font=font, width=entry_width, bd=2, relief="solid")
    strength_label = tk.Label(frame, text="Password Strength:", font=font, bg="#f0f0f0")

    strength_var = tk.StringVar()
    strength_options = {
        "Low (letters only)": 1,
        "Medium (letters and uppercase)": 2,
        "High (letters and numbers)": 3,
        "Very High (letters, numbers, and symbols)": 4
    }
    strength_dropdown = ttk.Combobox(frame, textvariable=strength_var, values=list(strength_options.keys()), font=font, width=entry_width)
    strength_dropdown.set("Select Strength")

    username_label = tk.Label(frame, text="Username:", font=font, bg="#f0f0f0")
    username_entry = tk.Entry(frame, font=font, width=entry_width, bd=2, relief="solid")
    site_label = tk.Label(frame, text="Site:", font=font, bg="#f0f0f0")
    site_entry = tk.Entry(frame, font=font, width=entry_width, bd=2, relief="solid")

    password_display = tk.Text(frame, font=font, width=entry_width, height=2, bd=2, relief="solid")
    result_display = tk.Label(frame, text="Result:", font=font, bg="#f0f0f0")
    status_display = tk.Label(frame, text="", font=font, bg="#f0f0f0")

    button_font = ("Helvetica", 12, "bold")
    button_width = 20

    generate_button = tk.Button(frame, text="Generate Password", command=generate_password_gui, font=button_font, width=button_width, bg="#3f51b5", fg="white", bd=2, relief="raised")
    save_button = tk.Button(frame, text="Save Password", command=save_password_gui, font=button_font, width=button_width, bg="#3f51b5", fg="white", bd=2, relief="raised")
    fetch_button = tk.Button(frame, text="Fetch Password", command=fetch_password_gui, font=button_font, width=button_width, bg="#3f51b5", fg="white", bd=2, relief="raised")
    clear_button = tk.Button(frame, text="Clear", command=clear_fields, font=button_font, width=button_width, bg="#3f51b5", fg="white", bd=2, relief="raised")
    logout_button = tk.Button(frame, text="Logout", command=logout_gui, font=button_font, width=button_width, bg="#f44336", fg="white", bd=2, relief="raised")

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
    clear_button.grid(row=7, column=0, columnspan=2, padx=20, pady=10)
    password_display.grid(row=8, column=0, columnspan=2, padx=20, pady=10)
    result_display.grid(row=9, column=0, columnspan=2, padx=20, pady=10)
    status_display.grid(row=10, column=0, columnspan=2, padx=20, pady=10)
    logout_button.grid(row=11, column=0, columnspan=2, padx=20, pady=10)

    window.mainloop()
