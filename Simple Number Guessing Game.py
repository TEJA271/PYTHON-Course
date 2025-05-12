import tkinter as tk
from tkinter import messagebox
import random

def check_guess():
    try:
        guess = int(entry.get())
        if guess < number_to_guess:
            label.config(text="Too low! Try again.")
        elif guess > number_to_guess:
            label.config(text="Too high! Try again.")
        else:
            label.config(text=f"Congratulations! You guessed the number.")
            play_again_button.pack(pady=10)
    except ValueError:
        messagebox.showwarning("Invalid Input", "Please enter a valid number.")

def play_again():
    global number_to_guess
    number_to_guess = random.randint(1, 100)
    label.config(text="Guess a number between 1 and 100")
    play_again_button.pack_forget()

number_to_guess = random.randint(1, 100)

root = tk.Tk()
root.title("Number Guessing Game")

label = tk.Label(root, text="Guess a number between 1 and 100", font=("Arial", 14))
label.pack(pady=20)

entry = tk.Entry(root, font=("Arial", 14), width=10)
entry.pack(pady=10)

guess_button = tk.Button(root, text="Check Guess", command=check_guess, font=("Arial", 14))
guess_button.pack(pady=5)

play_again_button = tk.Button(root, text="Play Again", command=play_again, font=("Arial", 14))

root.mainloop()
