import tkinter as tk
from tkinter import messagebox
import random
import string


def generate_password():
    length = int(length_entry.get())
    
    if length < 8:
        messagebox.showwarning("Warning", "Password should be at least 8 characters long.")
        return
    
    
    lower = random.choice(string.ascii_lowercase)
    upper = random.choice(string.ascii_uppercase)
    digit = random.choice(string.digits)
    symbol = random.choice(string.punctuation)

   
    remaining_length = length - 4
    all_characters = string.ascii_letters + string.digits + string.punctuation
    remaining_characters = ''.join(random.choice(all_characters) for _ in range(remaining_length))

    
    password = list(lower + upper + digit + symbol + remaining_characters)
    random.shuffle(password)

    
    password_entry.delete(0, tk.END)
    password_entry.insert(0, ''.join(password))


def copy_to_clipboard():
    window.clipboard_clear()
    window.clipboard_append(password_entry.get())
    messagebox.showinfo("Copied", "Password copied to clipboard!")


window = tk.Tk()
window.title("Standard Password Generator")


tk.Label(window, text="Password Length:").grid(row=0, column=0, padx=10, pady=10)
length_entry = tk.Entry(window)
length_entry.grid(row=0, column=1, padx=10, pady=10)

tk.Label(window, text="Generated Password:").grid(row=1, column=0, padx=10, pady=10)
password_entry = tk.Entry(window, width=30)
password_entry.grid(row=1, column=1, padx=10, pady=10)

generate_button = tk.Button(window, text="Generate Password", command=generate_password)
generate_button.grid(row=2, column=0, columnspan=2, pady=10)

copy_button = tk.Button(window, text="Copy to Clipboard", command=copy_to_clipboard)
copy_button.grid(row=3, column=0, columnspan=2, pady=10)


window.mainloop()
