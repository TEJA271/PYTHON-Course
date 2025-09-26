import tkinter as tk
import random

choices = ["Rock", "Paper", "Scissors"]

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a Draw!"
    elif (
        (user_choice == "Rock" and computer_choice == "Scissors") or
        (user_choice == "Paper" and computer_choice == "Rock") or
        (user_choice == "Scissors" and computer_choice == "Paper")
    ):
        return "You Win!"
    else:
        return "Computer Wins!"

def make_choice(user_choice):
    computer_choice = random.choice(choices)
    result = determine_winner(user_choice, computer_choice)
    user_choice_label.config(text=f"You chose: {user_choice}")
    computer_choice_label.config(text=f"Computer chose: {computer_choice}")
    result_label.config(text=f"Result: {result}")

root = tk.Tk()
root.title("Rock Paper Scissors Game")
root.geometry("400x300")
root.resizable(False, False)

title_label = tk.Label(root, text="Rock Paper Scissors", font=("Arial", 18, "bold"))
title_label.pack(pady=10)

user_choice_label = tk.Label(root, text="You chose: ", font=("Arial", 12))
user_choice_label.pack()

computer_choice_label = tk.Label(root, text="Computer chose: ", font=("Arial", 12))
computer_choice_label.pack()

result_label = tk.Label(root, text="Result: ", font=("Arial", 14, "bold"))
result_label.pack(pady=10)

button_frame = tk.Frame(root)
button_frame.pack(pady=20)

rock_button = tk.Button(button_frame, text="Rock", width=10, command=lambda: make_choice("Rock"))
rock_button.grid(row=0, column=0, padx=10)

paper_button = tk.Button(button_frame, text="Paper", width=10, command=lambda: make_choice("Paper"))
paper_button.grid(row=0, column=1, padx=10)

scissors_button = tk.Button(button_frame, text="Scissors", width=10, command=lambda: make_choice("Scissors"))
scissors_button.grid(row=0, column=2, padx=10)

root.mainloop()
