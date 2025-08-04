# Task 4 - To-Do List - GUI Version using Tkinter
# Internship: CodSoft - Python Programming Domain

import tkinter as tk
from tkinter import messagebox
import json
import os

TASK_FILE = 'tasks.json'

# Load tasks from file
def load_tasks():
    if os.path.exists(TASK_FILE):
        with open(TASK_FILE, 'r') as f:
            return json.load(f)
    return []

# Save tasks to file
def save_tasks():
    with open(TASK_FILE, 'w') as f:
        json.dump(tasks, f, indent=4)

# Add task
def add_task():
    title = task_entry.get().strip()
    if title:
        tasks.append({"title": title, "done": False})
        task_entry.delete(0, tk.END)
        update_task_list()
        save_tasks()
    else:
        messagebox.showwarning("Input Error", "Please enter a task title.")

# Mark selected task as done
def complete_task():
    try:
        index = task_listbox.curselection()[0]
        tasks[index]['done'] = True
        update_task_list()
        save_tasks()
    except IndexError:
        messagebox.showerror("Selection Error", "Please select a task to mark as completed.")

# Delete selected task
def delete_task():
    try:
        index = task_listbox.curselection()[0]
        removed_task = tasks.pop(index)
        update_task_list()
        save_tasks()
        messagebox.showinfo("Deleted", f"Task '{removed_task['title']}' deleted.")
    except IndexError:
        messagebox.showerror("Selection Error", "Please select a task to delete.")

# Update task list in the Listbox
def update_task_list():
    task_listbox.delete(0, tk.END)
    for task in tasks:
        status = "✅" if task["done"] else "❌"
        display_text = f"[{status}] {task['title']}"
        task_listbox.insert(tk.END, display_text)

        # Color highlight: green if done, red otherwise
        color = "#8BC34A" if task["done"] else "#FFCDD2"
        task_listbox.itemconfig(tk.END, {'bg': color})

# Main GUI setup
tasks = load_tasks()
root = tk.Tk()
root.title("📝 To-Do List - CodSoft Task")
root.geometry("450x500")
root.configure(bg="#F5F5F5")

# Title
title_label = tk.Label(root, text="My To-Do List", font=("Helvetica", 18, "bold"), fg="#333", bg="#F5F5F5")
title_label.pack(pady=10)

# Task Entry
entry_frame = tk.Frame(root, bg="#F5F5F5")
entry_frame.pack(pady=10)
task_entry = tk.Entry(entry_frame, width=35, font=("Helvetica", 12))
task_entry.pack(side=tk.LEFT, padx=5)
add_btn = tk.Button(entry_frame, text="Add", bg="#4CAF50", fg="white", font=("Helvetica", 10, "bold"), command=add_task)
add_btn.pack(side=tk.LEFT)

# Buttons
btn_frame = tk.Frame(root, bg="#F5F5F5")
btn_frame.pack(pady=10)

complete_btn = tk.Button(btn_frame, text="Mark as Completed", bg="#03A9F4", fg="white", width=20, font=("Helvetica", 10, "bold"), command=complete_task)
complete_btn.pack(pady=5)

delete_btn = tk.Button(btn_frame, text="Delete Task", bg="#F44336", fg="white", width=20, font=("Helvetica", 10, "bold"), command=delete_task)
delete_btn.pack(pady=5)

# Task List
task_label = tk.Label(root, text="Your Tasks", font=("Helvetica", 14), fg="#333", bg="#F5F5F5")
task_label.pack(pady=5)

task_listbox = tk.Listbox(root, width=50, height=15, font=("Helvetica", 12), selectbackground="#FFEB3B")
task_listbox.pack(pady=10)

# Initial update
update_task_list()

# Start GUI loop
root.mainloop()
