import tkinter as tk
from tkinter import filedialog, messagebox
import string
import random
from cryptography.fernet import Fernet
import os
import customtkinter
from PIL  import Image

def generate_password():
    length = 12
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    messagebox.showinfo("Generated Password", f"Password: {password}")

    with open('Mypassword.txt', 'w') as file:
        file.write(password)

def select_file():
    selected_file = filedialog.askopenfilename(initialdir="/", title="Select file",
                                               filetypes=(("Text files", "*.txt"), ("All files", "*.*")))
    if selected_file:
        messagebox.showinfo("File Selected", f"Selected File: {selected_file}")
        return selected_file
    else:
        messagebox.showinfo("File Selection", "No file selected.")
        return None

def encrypt_file():
    selected_file = select_file()
    if not selected_file:
        return

    # Generate key
    key = Fernet.generate_key()
    with open('myTopSecret.key', 'wb') as file:
        file.write(key)

    # Read data from file
    with open(selected_file, 'rb') as file:
        data = file.read()

    # Encrypt data
    f = Fernet(key)
    encrypted_data = f.encrypt(data)

    # Save the encrypted data into a file
    with open('mytopSecretInfo.txt', 'wb') as file:
        file.write(encrypted_data)

    messagebox.showinfo("Encryption", "File encrypted successfully.")

def decrypt_file():
    selected_file = select_file()
    if not selected_file:
        return

    # Read key from file
    with open('myTopSecret.key', 'rb') as file:
        key = file.read().strip()

    # Read the encrypted data from the file
    with open(selected_file, 'rb') as file:
        encrypted_data = file.read()

    # Decrypt the data 

        f = Fernet(key)
        decrypted_data = f.decrypt(encrypted_data)

        # Save decrypted data to a new file
        decrypted_filename = os.path.splitext(selected_file)[0] + "_decrypted.txt" 
        with open(decrypted_filename, 'wb') as file:
            file.write(decrypted_data)

        messagebox.showinfo("Decryption", f"File successfully Decrypted, file saved as {decrypted_filename}.")

if __name__ == "__main__":

    root = customtkinter.CTk()
    root.title("Password Generator ")
    root.config(bg="#C9AFF7")
    root.resizable(False, False)


   # canvas = customtkinter.CTkCanvas(root, bg="#C9AFF7", highlightthickness=0)
   # canvas.grid(row=0, column=0, rowspan=3, padx=(20, 0), pady=(20, 0))
    # Background image
    bg_img = customtkinter.CTkImage(light_image=Image.open("foto1.png").convert("RGBA"), size=(400, 300))
    bg_lab = customtkinter.CTkLabel(root, image=bg_img, text="")
    bg_lab.grid(row=0, column=0, rowspan=3, padx=(20, 0), pady=(20, 0))

    # Frame for buttons
    frame1 = customtkinter.CTkFrame(root, fg_color="#C9AFF7", bg_color="#C9AFF7", height=300, width=300, corner_radius=20)
    frame1.grid(row=0, column=1, rowspan=3, padx=(0, 20), pady=(20, 0))

    # Button for generating password
    generate_password_button = customtkinter.CTkButton(frame1, text="Generate Password", fg_color="#7E5ABE", corner_radius=32, command=generate_password)
    generate_password_button.grid(row=0, column=0, pady=(50, 10), padx=10, sticky="ew")

    # Button for encrypting file
    encrypt_button = customtkinter.CTkButton(frame1, text="Encrypt File",fg_color="#7E5ABE", corner_radius=32, command=encrypt_file)
    encrypt_button.grid(row=1, column=0, pady=10, padx=10, sticky="ew")

    # Button for decrypting file
    decrypt_button = customtkinter.CTkButton(frame1, text="Decrypt File", fg_color="#7E5ABE", corner_radius=32, command=decrypt_file)
    decrypt_button.grid(row=2, column=0, pady=(10, 50), padx=10, sticky="ew")

    root.mainloop()