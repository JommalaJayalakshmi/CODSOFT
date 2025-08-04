# Task 4 - Rock Paper Scissors Game
# Internship: CodSoft - Python Programming Domain
# Rock-Paper-Scissors GUI Game using Tkinter

import tkinter as tk
import random

# Choices and rules
choices = ['Rock', 'Paper', 'Scissors']
rules = {
    'Rock': 'Scissors',
    'Paper': 'Rock',
    'Scissors': 'Paper'
}

# Main game logic
def play(user_choice):
    computer_choice = random.choice(choices)
    result = ""

    if user_choice == computer_choice:
        result = "It's a Tie!"
    elif rules[user_choice] == computer_choice:
        result = "You Win!"
        scores["user"] += 1
    else:
        result = "You Lose!"
        scores["computer"] += 1

    # Update result
    result_label.config(text=f"You: {user_choice}\nComputer: {computer_choice}\nResult: {result}")
    score_label.config(text=f"Score ➤ You: {scores['user']}  |  Computer: {scores['computer']}")

# Reset game
def reset_game():
    scores["user"] = 0
    scores["computer"] = 0
    result_label.config(text="Make your move!")
    score_label.config(text="Score ➤ You: 0  |  Computer: 0")

# Initial scores
scores = {"user": 0, "computer": 0}

# Setup window
root = tk.Tk()
root.title("Rock Paper Scissors")
root.geometry("400x400")
root.resizable(False, False)
root.config(bg="#e6f2ff")

# Heading at the top
heading = tk.Label(root, text="🎮 Rock Paper Scissors", font=("Arial", 18, "bold"), bg="#e6f2ff", fg="#333")
heading.pack(pady=10)

# Result display
result_label = tk.Label(root, text="Make your move!", font=("Arial", 14), bg="#e6f2ff")
result_label.pack(pady=10)

# Score display
score_label = tk.Label(root, text="Score ➤ You: 0  |  Computer: 0", font=("Arial", 12), bg="#e6f2ff")
score_label.pack(pady=5)

# Buttons Frame
btn_frame = tk.Frame(root, bg="#e6f2ff")
btn_frame.pack(pady=20)

# Buttons
rock_btn = tk.Button(btn_frame, text="🪨 Rock", width=12, font=("Arial", 12), command=lambda: play("Rock"))
paper_btn = tk.Button(btn_frame, text="📄 Paper", width=12, font=("Arial", 12), command=lambda: play("Paper"))
scissors_btn = tk.Button(btn_frame, text="✂️ Scissors", width=12, font=("Arial", 12), command=lambda: play("Scissors"))

rock_btn.grid(row=0, column=0, padx=5)
paper_btn.grid(row=0, column=1, padx=5)
scissors_btn.grid(row=0, column=2, padx=5)

# Reset Button
reset_btn = tk.Button(root, text="🔁 Reset Game", font=("Arial", 12), bg="#f2f2f2", command=reset_game)
reset_btn.pack(pady=10)

# Start GUI loop
root.mainloop()
