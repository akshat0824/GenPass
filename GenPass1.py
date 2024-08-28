import random
import pyperclip
import secrets


def print_welcome_message():
    print("Alright, starting up the Password Generator...")


def get_password_length():
    # gets the length of password
    while True:
        try:
            length = int(input("\tHow long do you want your password? (e.g., 16): "))
            if length > 0:
                return length
            else:
                print("Length needs to be more than 0, come on.")
        except ValueError:
            print("That’s not a number. Try again.")


def get_password_strength():
    # Asks user for the password strength
    while True:
        print("\nPick how strong you want the password:")
        print("1: Basic (Uppercase and Lowercase letters)")
        print("2: Medium (Uppercase, Lowercase, and Numbers)")
        print("3: Strong (Uppercase, Lowercase, Numbers, and Symbols)")
        try:
            choice = int(input("Enter 1, 2, or 3: "))
            if choice in [1, 2, 3]:
                return choice
            else:
                print("Come on, pick 1, 2, or 3.")
        except ValueError:
            print("Not a number. Just enter 1, 2, or 3.")


def get_username():
    # asks user for the username to be saved with password
    return input("Username to save the password under: ").strip()


def get_site():
    # asks user for the site of usage for the password
    return input("Which site is this password for? ").strip()


def generate_password(length, strength_choice):
    # generates a password
    # Character sets for the password
    character_sets = {
        "Uppercases": 'ABCDEFGHIJKLMNOPQRSTUVWXYZ',
        "Lowercases": 'abcdefghijklmnopqrstuvwxyz',
        "Numbers": '0123456789',
        "Symbols": '!@#$&*?_-',
    }

    # Decide which character sets to use
    if strength_choice == 1:
        chosen_character_types = ("Uppercases", "Lowercases")
    elif strength_choice == 2:
        chosen_character_types = ("Uppercases", "Lowercases", "Numbers")
    else:  # strength_choice == 3
        chosen_character_types = ("Uppercases", "Lowercases", "Numbers", "Symbols")

    # Print out what character types we are using
    character_type_list = [char_type for char_type in chosen_character_types]
    print(f"Using these types: {character_type_list}")

    # Figure out how many characters to take from each set
    num_types = len(character_type_list)
    chars_per_type = length // num_types
    additional_chars = length - (chars_per_type * num_types)

    # Build the password
    password_characters = []
    all_characters = []

    # Pick characters from each type
    for char_type in character_type_list:
        char_set = character_sets[char_type]
        all_characters.extend(char_set)
        selected_chars = [secrets.choice(char_set) for _ in range(chars_per_type)]
        password_characters.extend(selected_chars)

    # Add extra random characters if needed
    extra_random_chars = [secrets.choice(all_characters) for _ in range(additional_chars)]
    password_characters.extend(extra_random_chars)

    # Shuffle and create the final password
    random.shuffle(password_characters)
    password = "".join(password_characters)

    # Print the password and copy it to the clipboard
    print("Here's your password: " + password)
    pyperclip.copy(password)
    print("Password copied to clipboard.")

    # Ask if the user wants to save this password
    save_to_file = input("Want to save this password? (yes/no): ").strip().lower()
    if save_to_file in ["yes", "y"]:
        username = get_username()
        site = get_site()
        save_password_to_file(username, site, password)


def save_password_to_file(username, site, password):
    """Saves the password to a file. Just appends it if the file already exists."""
    filename = "passwords.txt"
    entry = f"Site: {site}\nUsername: {username}\nPassword: {password}\n\n"

    # Append to the file
    with open(filename, "a") as file:
        file.write(entry)
    print(f"Password saved to '{filename}'.")


if __name__ == "__main__":
    print_welcome_message()
    password_length = get_password_length()
    password_strength = get_password_strength()
    generate_password(password_length, password_strength)