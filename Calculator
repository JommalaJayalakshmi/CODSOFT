import tkinter as tk
import math
import re

# Function to safely evaluate expressions
def calculate():
    try:
        expression = entry.get().replace('^', '**')
        # Replace √n or √(expr) with math.sqrt(...)
        expression = re.sub(r'√(\d+(\.\d+)?|\([^)]+\))', r'math.sqrt(\1)', expression)
        result = eval(expression)

        # Show integer if result like 2.0
        if isinstance(result, float) and result.is_integer():
            result = int(result)

        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except ZeroDivisionError:
        entry.delete(0, tk.END)
        entry.insert(0, "Error: Div by 0")
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Invalid Input")

# Function to insert characters
def on_click(char):
    entry.insert(tk.END, char)

# Clear all input
def clear():
    entry.delete(0, tk.END)

# Delete last character
def backspace():
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current[:-1])

# Colors for dark mode
BG = "#2e2e2e"
BTN_BG = "#3c3c3c"
BTN_TEXT = "#ffffff"
ENTRY_BG = "#1e1e1e"

# Create main window
root = tk.Tk()
root.title("Advanced Calculator")
root.geometry("340x500")
root.config(bg=BG)
root.resizable(False, False)

# Entry field
entry = tk.Entry(root, font=("Arial", 24), bg=ENTRY_BG, fg="white", bd=0, justify='right')
entry.pack(padx=10, pady=20, fill="both", ipady=15)

# Button layout
buttons = [
    ['7', '8', '9', '/', '√'],
    ['4', '5', '6', '*', '^'],
    ['1', '2', '3', '-', '←'],
    ['0', '.', '=', '+', 'C']
]

# Create buttons
for row in buttons:
    frame = tk.Frame(root, bg=BG)
    frame.pack(expand=True, fill="both", padx=5, pady=3)
    for btn in row:
        if btn == '=':
            action = calculate
        elif btn == 'C':
            action = clear
        elif btn == '←':
            action = backspace
        else:
            action = lambda x=btn: on_click(x)

        tk.Button(
            frame, text=btn, command=action,
            font=("Arial", 16), bg=BTN_BG, fg=BTN_TEXT,
            relief='flat', height=2, width=5
        ).pack(side="left", expand=True, fill="both", padx=2, pady=2)

# Run the application
root.mainloop()
