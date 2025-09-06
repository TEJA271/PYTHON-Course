import tkinter as tk
from datetime import date

def calculate_age():
    name = name_entry.get()
    day = int(day_entry.get())
    month = int(month_entry.get())
    year = int(year_entry.get())
    today = date.today()
    age = today.year - year - ((today.month, today.day) < (month, day))
    result_label.config(text=f"Hello {name}, you are {age} years old!")

root = tk.Tk()
root.geometry("400x400")
root.title("Age Calculator App")

frame = tk.Frame(root)
frame.pack(pady=40)

tk.Label(frame, text="Name:").grid(row=0, column=0, padx=10, pady=5, sticky='e')
name_entry = tk.Entry(frame)
name_entry.grid(row=0, column=1, pady=5)

tk.Label(frame, text="Day:").grid(row=1, column=0, padx=10, pady=5, sticky='e')
day_entry = tk.Entry(frame)
day_entry.grid(row=1, column=1, pady=5)

tk.Label(frame, text="Month:").grid(row=2, column=0, padx=10, pady=5, sticky='e')
month_entry = tk.Entry(frame)
month_entry.grid(row=2, column=1, pady=5)

tk.Label(frame, text="Year:").grid(row=3, column=0, padx=10, pady=5, sticky='e')
year_entry = tk.Entry(frame)
year_entry.grid(row=3, column=1, pady=5)

calculate_btn = tk.Button(root, text="Calculate Age", command=calculate_age)
calculate_btn.pack(pady=20)

result_label = tk.Label(root, text="", font=("Arial", 12))
result_label.pack()

root.mainloop()
