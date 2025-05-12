import tkinter as tk
import random

def generate_quote():
    quotes = [
        "The only way to do great work is to love what you do.",
        "Success is not final, failure is not fatal: It is the courage to continue that counts.",
        "The best time to plant a tree was 20 years ago. The second best time is now.",
        "Life is what happens when you're busy making other plans.",
        "In the middle of every difficulty lies opportunity.",
        "You miss 100% of the shots you don’t take.",
        "It always seems impossible until it's done.",
        "The future belongs to those who believe in the beauty of their dreams.",
        "Don’t watch the clock; do what it does. Keep going.",
        "Believe you can and you're halfway there.",
        "Do not go where the path may lead, go instead where there is no path and leave a trail.",
        "What lies behind us and what lies before us are tiny matters compared to what lies within us.",
        "Success usually comes to those who are too busy to be looking for it.",
        "The way to get started is to quit talking and begin doing.",
        "Your time is limited, so don’t waste it living someone else’s life.",
        "Opportunities don't happen, you create them.",
        "The only limit to our realization of tomorrow is our doubts of today.",
        "The purpose of life is not to be happy. It is to be useful, to be honorable, to be compassionate, to have it make some difference that you have lived and lived well.",
        "Act as if what you do makes a difference. It does.",
        "You have to be odd to be number one.",
        "It does not matter how slowly you go as long as you do not stop.",
        "Success is walking from failure to failure with no loss of enthusiasm.",
        "Don’t wait. The time will never be just right.",
        "The harder you work for something, the greater you’ll feel when you achieve it.",
        "Nothing in the world can take the place of Persistence. Talent will not; nothing is more common than unsuccessful men with talent.",
        "Do what you can with all you have, wherever you are.",
        "You must be the change you wish to see in the world.",
        "Your life does not get better by chance, it gets better by change.",
        "The only impossible journey is the one you never begin.",
        "When you have a dream, you’ve got to grab it and never let go.",
        "Everything you can imagine is real.",
        "Don’t be afraid to give up the good to go for the great.",
        "The best way to predict your future is to create it.",
        "The only thing standing between you and your goal is the story you keep telling yourself as to why you can’t achieve it.",
        "It always seems impossible until it’s done.",
        "We may encounter many defeats but we must not be defeated.",
        "You are never too old to set another goal or to dream a new dream.",
        "Do not wait to strike till the iron is hot, but make it hot by striking.",
        "The greatest glory in living lies not in never falling, but in rising every time we fall.",
        "The purpose of life is to live it, to taste experience to the utmost, to reach out eagerly and without fear for newer and richer experience."
    ]
    
    random_quote = random.choice(quotes)
    label.config(text=random_quote)

root = tk.Tk()
root.title("Random Quote Generator")

label = tk.Label(root, text="Click to get a quote", font=("Arial", 14), wraplength=300)
label.pack(pady=10)

generate_button = tk.Button(root, text="Generate Quote", command=generate_quote, font=("Arial", 14))
generate_button.pack(pady=10)

root.mainloop()
