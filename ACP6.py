import tkinter as tk
from tkinter import messagebox
import random

# Function to play the game
def play(user_choice):
    choices = ["Rock", "Paper", "Scissors"]
    computer_choice = random.choice(choices)
    
    if user_choice == computer_choice:
        result = "It's a Tie!"
    elif (user_choice == "Rock" and computer_choice == "Scissors") or \
         (user_choice == "Paper" and computer_choice == "Rock") or \
         (user_choice == "Scissors" and computer_choice == "Paper"):
        result = "You Win!"
    else:
        result = "Computer Wins!"
    
    computer_label.config(text=f"Computer chose: {computer_choice}")
    result_label.config(text=f"Result: {result}")

# Create main window
root = tk.Tk()
root.title("Rock Paper Scissors Game")
root.geometry("400x300")

# Instructions label
instruction_label = tk.Label(root, text="Choose Rock, Paper, or Scissors:", font=("Helvetica", 12))
instruction_label.pack(pady=10)

# Buttons for user choices
button_frame = tk.Frame(root)
button_frame.pack(pady=10)

rock_button = tk.Button(button_frame, text="Rock", width=10, command=lambda: play("Rock"))
rock_button.grid(row=0, column=0, padx=5)

paper_button = tk.Button(button_frame, text="Paper", width=10, command=lambda: play("Paper"))
paper_button.grid(row=0, column=1, padx=5)

scissors_button = tk.Button(button_frame, text="Scissors", width=10, command=lambda: play("Scissors"))
scissors_button.grid(row=0, column=2, padx=5)

# Label to show computer's choice
computer_label = tk.Label(root, text="", font=("Helvetica", 12))
computer_label.pack(pady=10)

# Label to show result
result_label = tk.Label(root, text="", font=("Helvetica", 14, "bold"))
result_label.pack(pady=10)

# Run the application
root.mainloop()
