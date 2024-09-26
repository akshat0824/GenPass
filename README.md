## GenPass


### Description
GenPass is a Python application designed to securely generate, store, and manage passwords. The application features a user-friendly graphical interface built with Tkinter, allowing users to create passwords of varying lengths and strengths, save them along with usernames and site details to a text file, and retrieve stored credentials with ease. The application also integrates clipboard functionality for quick access to generated passwords.

### Packages and Their Usage
#### 1. tkinter
: tkinter is the standard Python interface to the Tk GUI toolkit. It is used to create the graphical user interface (GUI) for GenPass.
Usage: In GenPass, tkinter is utilized to build and manage the application’s window, labels, buttons, and other interactive elements. It handles user inputs for generating passwords, displaying results, and saving or fetching credentials.

#### 2. ttk
: ttk (Themed Tk) is a module within tkinter that provides access to advanced widgets and styles.
Usage: ttk is used in GenPass to create the dropdown menu (ComboBox) that allows users to select password strength options. It enhances the visual appearance of the GUI components.


#### 3. pyperclip
Description: pyperclip is a cross-platform Python module for clipboard operations.
Usage: In GenPass, pyperclip is used to copy generated passwords to the clipboard. This allows users to easily paste the passwords into other applications or fields without manually copying them.

#### 4. os
Description: os is a module that provides a way to interact with the operating system, including file operations.
Usage: The os module is used in GenPass to check for the existence of the password storage file (passwords.txt) and handle file operations for saving and retrieving passwords.

### Installation 
 #### 1. Clone the repository
     git clone https://github.com/akshat0824/GenPass.git
     cd GenPass
     
 #### 2. Install required packages
     pip install pyperclip cryptography
 #### 3. Run the application
     python main.py


### Contributing
Contributions are welcome! Feel free to submit issues or pull requests. For questions or suggestions, open an issue or contact me directly.


### Acknowledgements
1.Tkinter Documentation 
2.Cryptography Documentation
3.JSON Documentation
