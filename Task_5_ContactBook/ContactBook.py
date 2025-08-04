# Task 5 - Contact Book
# Internship: CodSoft - Python Programming Domain

import tkinter as tk
from tkinter import messagebox, simpledialog
import json
import os
import re

CONTACT_FILE = 'contacts.json'

def load_contacts():
    if os.path.exists(CONTACT_FILE):
        with open(CONTACT_FILE, 'r') as file:
            return json.load(file)
    return {}

def save_contacts():
    with open(CONTACT_FILE, 'w') as file:
        json.dump(contacts, file, indent=4)

def add_contact():
    name = name_entry.get().strip()
    phone = phone_entry.get().strip()
    email = email_entry.get().strip()
    address = address_entry.get().strip()

    if name == '' or phone == '':
        messagebox.showwarning("Input Error", "Name and Phone are required.")
        return

    if not (phone.isdigit() and len(phone) == 10):
        messagebox.showerror("Invalid Phone", "Phone number must be exactly 10 digits.")
        return

    if email and not re.match(r"^[\w\.-]+@gmail\.com$", email):
        messagebox.showerror("Invalid Email", "Email must be in format username@gmail.com.")
        return

    contacts[name.lower()] = {
        "Name": name,
        "Phone": phone,
        "Email": email,
        "Address": address
    }
    save_contacts()
    clear_entries()
    messagebox.showinfo("Success", f"Contact '{name}' added!")
    view_contacts()

def view_contacts():
    contact_list.delete(0, tk.END)
    for c in contacts.values():
        contact_list.insert(tk.END, f"{c['Name']} - {c['Phone']}")

def search_contact():
    keyword = simpledialog.askstring("Search", "Enter name or phone:")
    if not keyword:
        return
    contact_list.delete(0, tk.END)
    keyword = keyword.lower()
    for c in contacts.values():
        if keyword in c['Name'].lower() or keyword in c['Phone']:
            contact_list.insert(tk.END, f"{c['Name']} - {c['Phone']}")

def update_contact():
    name = simpledialog.askstring("Update", "Enter contact name to update:")
    if not name or name.lower() not in contacts:
        messagebox.showerror("Not Found", "Contact not found.")
        return

    c = contacts[name.lower()]
    phone = simpledialog.askstring("Phone", "New phone number:", initialvalue=c['Phone'])
    email = simpledialog.askstring("Email", "New email:", initialvalue=c['Email'])
    address = simpledialog.askstring("Address", "New address:", initialvalue=c['Address'])

    if not (phone.isdigit() and len(phone) == 10):
        messagebox.showerror("Invalid Phone", "Phone number must be exactly 10 digits.")
        return

    if email and not re.match(r"^[\w\.-]+@gmail\.com$", email):
        messagebox.showerror("Invalid Email", "Email must be in format username@gmail.com.")
        return

    contacts[name.lower()] = {
        "Name": name,
        "Phone": phone,
        "Email": email,
        "Address": address
    }
    save_contacts()
    messagebox.showinfo("Updated", f"Contact '{name}' updated.")
    view_contacts()

def delete_contact():
    name = simpledialog.askstring("Delete", "Enter contact name to delete:")
    if not name or name.lower() not in contacts:
        messagebox.showerror("Not Found", "Contact not found.")
        return
    del contacts[name.lower()]
    save_contacts()
    messagebox.showinfo("Deleted", f"Contact '{name}' deleted.")
    view_contacts()

def clear_entries():
    name_entry.delete(0, tk.END)
    phone_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)
    address_entry.delete(0, tk.END)

# Initialize
contacts = load_contacts()
root = tk.Tk()
root.title("Contact Book")
root.geometry("420x580")
root.configure(bg="#f0f8ff")

tk.Label(root, text="Contact Book", font=("Helvetica", 18, "bold"), bg="#f0f8ff", fg="#2f4f4f").pack(pady=10)

input_frame = tk.Frame(root, bg="#f0f8ff")
input_frame.pack(pady=5)

tk.Label(input_frame, text="Name", bg="#f0f8ff").grid(row=0, column=0, sticky="w")
name_entry = tk.Entry(input_frame, width=30)
name_entry.grid(row=0, column=1, pady=2)

tk.Label(input_frame, text="Phone", bg="#f0f8ff").grid(row=1, column=0, sticky="w")
phone_entry = tk.Entry(input_frame, width=30)
phone_entry.grid(row=1, column=1, pady=2)

tk.Label(input_frame, text="Email", bg="#f0f8ff").grid(row=2, column=0, sticky="w")
email_entry = tk.Entry(input_frame, width=30)
email_entry.grid(row=2, column=1, pady=2)

tk.Label(input_frame, text="Address", bg="#f0f8ff").grid(row=3, column=0, sticky="w")
address_entry = tk.Entry(input_frame, width=30)
address_entry.grid(row=3, column=1, pady=2)

button_frame = tk.Frame(root, bg="#f0f8ff")
button_frame.pack(pady=10)

tk.Button(button_frame, text="Add", bg="#20b2aa", fg="white", width=12, command=add_contact).grid(row=0, column=0, padx=5)
tk.Button(button_frame, text="View", bg="#4682b4", fg="white", width=12, command=view_contacts).grid(row=0, column=1, padx=5)
tk.Button(button_frame, text="Search", bg="#9370db", fg="white", width=12, command=search_contact).grid(row=1, column=0, pady=5, padx=5)
tk.Button(button_frame, text="Update", bg="#ff8c00", fg="white", width=12, command=update_contact).grid(row=1, column=1, pady=5, padx=5)
tk.Button(button_frame, text="Delete", bg="#dc143c", fg="white", width=12, command=delete_contact).grid(row=2, column=0, pady=5, padx=5)
tk.Button(button_frame, text="Clear Fields", bg="#708090", fg="white", width=12, command=clear_entries).grid(row=2, column=1, pady=5, padx=5)

tk.Label(root, text="Saved Contacts", font=("Helvetica", 12, "bold"), bg="#f0f8ff", fg="#333").pack(pady=(15, 0))
list_frame = tk.Frame(root)
list_frame.pack(pady=5)

scrollbar = tk.Scrollbar(list_frame)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

contact_list = tk.Listbox(list_frame, width=45, height=10, yscrollcommand=scrollbar.set, bg="white", fg="black", font=("Arial", 10))
contact_list.pack(side=tk.LEFT, fill=tk.BOTH)
scrollbar.config(command=contact_list.yview)

view_contacts()
root.mainloop()
