# Task 3 - Password Generator
# Internship: CodSoft - Python Programming Domain

import tkinter as tk
from tkinter import ttk, messagebox
import random
import string

def generate_password():
    try:
        length = int(length_entry.get())
        if length < 4:
            raise ValueError("Length must be at least 4")

        complexity = complexity_var.get()

        lower = string.ascii_lowercase
        upper = string.ascii_uppercase
        digits = string.digits
        symbols = string.punctuation

        if complexity == "Letters Only":
            all_chars = lower + upper
        elif complexity == "Letters + Digits":
            all_chars = lower + upper + digits
        else:
            all_chars = lower + upper + digits + symbols

        password = [
            random.choice(lower),
            random.choice(upper),
            random.choice(digits if complexity != "Letters Only" else lower),
        ]
        if complexity == "Letters + Digits + Symbols":
            password.append(random.choice(symbols))

        password += random.choices(all_chars, k=length - len(password))
        random.shuffle(password)

        result.set("".join(password))

    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid number (minimum 4).")

def copy_to_clipboard():
    root.clipboard_clear()
    root.clipboard_append(result.get())
    messagebox.showinfo("Copied", "Password copied to clipboard!")

# GUI Setup
root = tk.Tk()
root.title("🔐 Password Generator")
root.geometry("420x360")
root.config(bg="#f0f4f7")
root.resizable(False, False)

# Style Configuration 
style = ttk.Style()
style.theme_use("clam")
style.configure("TButton", font=("Segoe UI", 11, "bold"), padding=6)
style.configure("TLabel", background="#f0f4f7", font=("Segoe UI", 11))
style.configure("TEntry", font=("Segoe UI", 12))
style.configure("TMenubutton", font=("Segoe UI", 10), padding=4)

#Widgets 
ttk.Label(root, text="🔐 Password Generator", font=("Segoe UI", 16, "bold")).pack(pady=15)

ttk.Label(root, text="Enter Password Length:").pack()
length_entry = ttk.Entry(root, width=10, justify="center")
length_entry.pack(pady=6)

ttk.Label(root, text="Select Complexity:").pack()
complexity_var = tk.StringVar(value="Letters + Digits + Symbols")
ttk.OptionMenu(root, complexity_var, "Letters + Digits + Symbols", "Letters Only", "Letters + Digits", "Letters + Digits + Symbols").pack(pady=6)

ttk.Button(root, text="Generate Password", command=generate_password).pack(pady=10)

result = tk.StringVar()
ttk.Entry(root, textvariable=result, width=30, font=("Segoe UI", 12), justify='center', state='readonly').pack(pady=6)

ttk.Button(root, text="Copy to Clipboard", command=copy_to_clipboard).pack(pady=6)

#Run GUI 
root.mainloop()
